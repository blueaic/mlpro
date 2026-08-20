.. _target_bf_streams_tasks:

Stream Tasks
============

Ready-to-use StreamTasks implement common DSP transformations while following the same instance-flow contract as custom tasks. They can be added directly to a StreamWorkflow, combined through predecessor relations, and mixed with own StreamTask implementations.

The current pool covers fixed-size windows through RingBuffer, feature/label-space transformation through Rearranger, and numerical feature derivation through Deriver.

.. toctree::
   :maxdepth: 1
   :glob:

   tasks/*
