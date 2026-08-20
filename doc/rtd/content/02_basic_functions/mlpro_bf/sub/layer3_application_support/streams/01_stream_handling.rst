.. _target_bf_streams_handling:

Stream Handling
===============

A stream is MLPro's standardized interface to sequentially available data. Instead of assuming that the complete dataset can be scanned at any time, a Stream behaves like an iterator and delivers the next Instance when requested.

The basic data model is:

``Feature / Label -> Instance -> Stream -> StreamProvider``

An **Instance** contains feature data and optional label data, together with an id, a time stamp, and optional metadata. A **Stream** defines the feature and label spaces and controls sequential access. A **StreamProvider** groups or discovers related streams and provides a uniform lookup interface.

Streams can optionally use a **Sampler** to omit selected instances during iteration. **MultiStream** combines several streams into one sequence and can switch between them in configurable batches.

A compact example using MLPro's native stream provider looks like this:

.. code-block:: python

    from mlpro.bf.streams.streams import StreamProviderMLPro

    provider = StreamProviderMLPro()
    streams = provider.get_stream_list()

    stream = streams[0]
    instance = next(iter(stream))

    print(instance.id)
    print(instance.feature_values)

The detailed page explains stream providers, streams, instances, samplers, and multi-streams as extension points for own data sources.

.. image::
    images/stream_processor.png
    :width: 700 px


**Learn more**

.. toctree::
   :maxdepth: 1

   stream_handling/stream_handling.rst


**Cross reference**
    + :ref:`Howto BF-STREAMS-101: Basics of Streams <Howto BF STREAMS 101>`
    + :ref:`API reference: Streams <target_ap_bf_streams>`
