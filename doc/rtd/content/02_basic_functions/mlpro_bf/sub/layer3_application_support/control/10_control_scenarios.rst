.. _target_bf_control_scenarios:

Control scenarios
=================

Overview
--------

MLPro-BF-Control provides ready-to-use control-system containers that assemble the underlying control tasks into executable
closed-loop scenarios. They are useful both as production building blocks and as reference implementations for custom
``ControlSystem`` subclasses.

``BasicControlSystem`` represents the standard single-loop case with one controller and one controlled system. The same container
can optionally insert an ``Integrator`` between controller and plant. ``CascadeControlSystem`` extends the architecture to
multiple nested loops, where the output of an outer controller becomes the setpoint of the next inner loop.

All of these scenarios use ``ControlWorkflow`` internally and therefore inherit the task graph, shared-state, timing, and
visualization concepts of BF-Control and BF-Streams.


**Learn more**

.. toctree::
   :maxdepth: 1
   :glob:

   control_scenarios/*


**Cross reference**

- :ref:`BF-Control overview <target_bf_control>`
- :ref:`Howto BF-CONTROL-001: Basic control system <Howto BF CONTROL 001>`
- :ref:`Howto BF-CONTROL-002: Control system with integrator <Howto BF CONTROL 002>`
- :ref:`Howto BF-CONTROL-003: Cascade control system <Howto BF CONTROL 003>`
- :ref:`API Reference BF-Control <target_api_bf_control>`
