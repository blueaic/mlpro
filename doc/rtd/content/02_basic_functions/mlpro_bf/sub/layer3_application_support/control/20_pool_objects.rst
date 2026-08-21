.. _target_bf_control_pool_objects:

Ready-to-use control objects
============================

Overview
--------

The BF-Control pool contains reusable components for assembling control workflows without implementing every task from scratch.
The current pool is organized into **operators**, **controllers**, and **controlled systems/control-system containers**.

Operators transform control data inside a workflow. Controllers map ``ControlError`` objects to ``ControlVariable`` objects.
Controlled-system wrappers connect BF-Systems to the control workflow, while ready-made control-system containers assemble common
closed-loop architectures.


**Learn more**

.. toctree::
   :maxdepth: 1
   :glob:

   pool_objects/*


**Cross reference**

- :ref:`BF-Control overview <target_bf_control>`
- :ref:`Control scenarios <target_bf_control_scenarios>`
- :ref:`API Reference BF-Control Pool Objects <target_pool_bf_control>`
