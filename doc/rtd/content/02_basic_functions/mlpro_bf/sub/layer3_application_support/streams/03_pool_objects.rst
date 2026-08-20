.. _target_stream_tasks_pool:

Ready-to-Use Stream Objects and Tasks
=====================================

MLPro-BF ships with reusable stream sources and processing tasks that can be plugged directly into StreamWorkflows. They are useful both as application components and as reference implementations for own Stream and StreamTask classes.

The native stream pool contains generated and file-based streams such as CSV streams, random high-dimensional data, double spirals, point-outlier streams, and configurable random clouds. These sources make DSP workflows reproducible without depending on an external live system.

The task pool currently contains three core processing patterns:

* **RingBuffer / Window** for maintaining a fixed-size active subset and forwarding explicit deletions,
* **Rearranger** for selecting and reordering features into a new feature space,
* **Deriver** for extending selected stream features by numerical derivatives.

These tasks follow the same ``InstTypeNew`` / ``InstTypeDel`` contract as custom StreamTasks and can therefore be freely combined with own processing steps.

.. toctree::
   :maxdepth: 1
   :glob:

   stream_pool_objects/*
