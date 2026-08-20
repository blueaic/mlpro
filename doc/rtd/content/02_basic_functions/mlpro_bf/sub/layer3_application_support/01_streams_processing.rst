.. _target_bf_streams:

Data Stream Processing
======================

Why data stream processing?
---------------------------

Many applications do not work on a fixed dataset. Measurements, sensor values, transactions, events, or simulation results arrive continuously and have to be processed in the order in which they become available.

MLPro-BF provides a standardized architecture for this kind of **Data Stream Processing (DSP)**. It separates the data source from the processing logic and combines both through reusable stream tasks, workflows, and scenarios.

The central processing chain is:

``Stream -> Instance -> StreamTask -> StreamWorkflow -> StreamScenario``

A **Stream** delivers one **Instance** after another. A **StreamTask** performs one processing operation on the current instance set. Several tasks can be connected in a **StreamWorkflow**, including predecessor relations and parallel branches. A **StreamScenario** finally combines a stream with a workflow and controls the processing cycles.

A second concept is equally important. Stream processing does not only propagate newly arriving instances. MLPro explicitly distinguishes between instances that become available and instances that become obsolete:

``InstTypeNew ('+')   /   InstTypeDel ('-')``

This allows tasks such as sliding windows to remove old data explicitly and enables dependent tasks to keep their own state synchronized with the current stream state.

DSP is deliberately separated from Online Machine Learning. DSP provides the generic infrastructure for sequential data handling and processing; online learning algorithms can build on top of it. Likewise, a data stream is not necessarily a real-time system: *streaming* describes the sequential availability of data, while *real-time* additionally imposes timing constraints.

Stream Handling and Processing
------------------------------

The stream subsystem is organized around two perspectives. **Stream handling** describes how streams, instances, providers, samplers, and multi-streams expose sequential data. **Stream processing** describes how StreamTasks, StreamWorkflows, shared data, and StreamScenarios transform and orchestrate these data flows.

The following pages introduce both perspectives, the pool of ready-to-use stream objects and tasks, and integration points for third-party data sources.

.. toctree::
   :maxdepth: 1
   :glob:

   streams/*


**Cross reference**
    + :ref:`Howto BF-STREAMS-101: Basics of Streams <Howto BF STREAMS 101>`
    + :ref:`Howto BF-STREAMS-102: Tasks, Workflows and Stream Scenarios <Howto BF STREAMS 102>`
    + :ref:`API reference: Streams <target_ap_bf_streams>`
