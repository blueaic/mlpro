.. _target_bf_streams_processing:

Stream Processing
=================

Stream handling defines how sequential data enters MLPro. Stream processing defines what happens to that data afterwards.

The processing architecture is built from three reusable levels:

``StreamTask -> StreamWorkflow -> StreamScenario``

A **StreamTask** performs one operation on a dictionary of stream instances. A **StreamWorkflow** connects several tasks through predecessor relations and manages the shared processing state. A **StreamScenario** combines one Stream with one StreamWorkflow and repeatedly feeds the next stream instance into the workflow.

The instance dictionary carried through a workflow does not only contain data objects. Every entry also carries an instance type:

``instance_id -> (InstTypeNew | InstTypeDel, Instance)``

``InstTypeNew`` marks data that has become available. ``InstTypeDel`` marks data that has become obsolete. This explicit deletion signal is essential for stateful online processing: a window can evict an old sample, and all dependent tasks can update their own state accordingly instead of silently accumulating stale data.

.. image::
    images/stream_processing.png
    :width: 800 px

A StreamWorkflow builds on MLPro's multitasking layer. Independent branches can therefore be executed according to their predecessor dependencies and configured range of asynchronicity, while the shared object provides task-specific results and instance sets.

The detailed page shows how to implement own StreamTasks, connect them to workflows, and orchestrate them with StreamScenario.


**Learn more**

.. toctree::
   :maxdepth: 1

   stream_processing/stream_processing.rst


**Cross references**
    + :ref:`Howto BF-STREAMS-102: Tasks, Workflows and Stream Scenarios <Howto BF STREAMS 102>`
    + :ref:`BF-MT - Multitasking <target_bf_mt>`
    + :ref:`API reference: Streams <target_ap_bf_streams>`
