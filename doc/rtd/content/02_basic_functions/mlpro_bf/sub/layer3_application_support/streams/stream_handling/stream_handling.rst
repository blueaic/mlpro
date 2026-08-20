.. _target_bf_streams_handling_01:

Streams Handling
================

Core data model
---------------

MLPro models sequential data with a small set of reusable abstractions. The same model can represent generated test data, files, external datasets, simulations, sensor feeds, or other sources as long as they can provide instances one after another.

``Feature / Label -> Instance -> Stream -> StreamProvider``

**Feature and Label.** Both classes specialize MLPro's mathematical Dimension abstraction. A stream therefore describes its data through the same spaces and elements that are used throughout MLPro-BF-MATH.

**Instance.** An Instance combines feature data with optional label data. It additionally carries an id, a time stamp, and optional keyword metadata. The convenience properties ``num_features`` and ``feature_values`` provide direct access to frequently used feature information.

.. code-block:: python

    instance = next(iter(stream))

    print(instance.id)
    print(instance.tstamp)
    print(instance.feature_values)

An instance id is assigned by the stream during iteration. If no explicit time stamp is available, the id can also serve as the time index. This makes the same processing architecture usable for physical time stamps and for ordered pseudo-time data.

**Stream.** A Stream is an iterator over Instance objects. It owns the feature and optional label space, controls reset and iteration behavior, manages instance ids, and may optionally apply a sampler. Concrete stream classes implement how the next instance is obtained from the underlying source.

A stream can therefore be consumed with standard Python iteration:

.. code-block:: python

    for instance in stream:
        process(instance)

Whether all data already exists in memory is irrelevant to the consumer. This is the key abstraction boundary: client code works with sequential instances instead of depending on the original storage or transport technology.

**Sampler.** A Sampler is attached to a Stream and decides for every incoming instance whether it should be omitted. Custom samplers implement ``_omit_instance(p_instance)``. This keeps sampling separate from the stream source and makes sampling strategies reusable across different streams.

**MultiStream.** MultiStream combines several Stream objects into a single sequence. Streams can be consumed in configurable batches before switching to the next source, which is useful for mixed training/evaluation streams or scenarios that combine several sequential sources.

Connecting data sources
-----------------------

A **StreamProvider** groups streams behind a common discovery and lookup interface. Providers implement ``_get_stream_list()`` and ``_get_stream()``; users can then list available streams or request one by id or name without knowing how the provider creates or accesses it.

MLPro's built-in provider can be used as follows:

.. code-block:: python

    from mlpro.bf.streams.streams import StreamProviderMLPro

    provider = StreamProviderMLPro()

    for stream in provider.get_stream_list():
        print(stream.get_name())

    stream = provider.get_stream(p_id='Rnd10Dx1000')

.. image::
    images/stream_providers.drawio.png
    :width: 650 px

For own live or external data, there are two common extension paths. If one concrete source shall be exposed directly, derive from **Stream** and implement the source-specific reset and next-instance logic. If several related streams shall be discoverable through one integration, add a **StreamProvider** around them. Feature and label spaces remain expressed with MLPro's normal Dimension/Space abstractions, so downstream StreamTasks do not need source-specific code.

Approved integrations such as OpenML, scikit-learn, and River use this wrapper pattern. See :ref:`3rd party support <target_bf_streams_3rd_party_support>` for the corresponding extension projects.


**Cross references**
    + :ref:`Howto BF-STREAMS-101: Basics of Streams <Howto BF STREAMS 101>`
    + :ref:`3rd party support <target_bf_streams_3rd_party_support>`
    + :ref:`API Reference: Streams <target_ap_bf_streams>`
