.. _target_bf_control:

Closed-loop control
===================

Overview
--------

MLPro-BF-Control provides a workflow-based model for closed-loop control. It builds on :ref:`BF-Streams <target_bf_streams>` for
instance flow, tasks, workflows, shared state, and scenarios, and on :ref:`BF-Systems <target_bf_systems>` for the controlled
plant.

The module covers the complete control loop from setpoint to controlled variable. Its central objects are:

- **ControlData** and its specializations ``SetPoint``, ``ControlError``, ``ControlVariable``, and ``ControlledVariable``.
- **ControlTask** as the common base for control-processing tasks.
- **Operator** for reusable transformations inside the control workflow.
- **Controller** for mapping a control error to a control variable.
- **ControlledSystem** for wrapping a BF-System as a task inside the control workflow.
- **ControlWorkflow** for composing controllers, operators, controlled systems, and nested sub-control loops.
- **ControlShared** for shared process state, timing, unique control-instance ids, latency handling, and setpoint management.
- **ControlSystem** as the scenario-level orchestrator of the control process.
- **ControlPanel** as an interface for external start/stop and setpoint changes.

A basic loop can be read as::

    SetPoint + ControlledVariable
              |
          Comparator
              |
         ControlError
              |
          Controller
              |
        ControlVariable
              |
       ControlledSystem
              |
     ControlledVariable


Control data and workflow architecture
--------------------------------------

All control signals are represented as ``ControlData`` instances and therefore participate in the same instance-processing model
as BF-Streams. ``SetPoint`` stores the desired value, ``ControlledVariable`` the measured system output, ``ControlError`` their
difference, and ``ControlVariable`` the controller output. Helper functions ``get_ctrl_data()`` and ``replace_ctrl_data()`` allow
tasks to locate and replace these typed objects in an ``InstDict``.

A ``ControlWorkflow`` is a specialized ``StreamWorkflow``. This means control applications can use the same predecessor-based task
graphs, asynchronous execution ranges, and visualization mechanisms as stream-processing applications. Control-specific shared
state adds process timing and latency coordination on top of that infrastructure.

``ControlledSystem`` wraps a :class:`mlpro.bf.systems.System` and translates between ``ControlVariable``/``ControlledVariable``
and the System API's ``Action``/``State`` objects. The latency of the wrapped system participates in the workflow's time
management and therefore determines when actions are updated and when system transitions are processed.


Control systems and cascades
----------------------------

``ControlSystem`` is the scenario-level template. A custom implementation creates its ``ControlWorkflow`` in ``_setup()``; every
scenario cycle then executes that workflow. The ready-to-use ``BasicControlSystem`` builds a synchronous loop from one controller
and one controlled system and can optionally insert an ``Integrator`` after the controller.

``CascadeControlSystem`` generalizes this model to nested control loops. It creates one ``ControlWorkflow`` per cascade level and
uses ``Converter`` tasks to pass a superior controller output as the setpoint of the next inner loop and to return the inner
controlled variable to the outer workflow. Shared timing information is propagated across the nested workflows so different
latencies can be coordinated consistently.


Ready-to-use building blocks
----------------------------

The current pool provides:

- operators ``Comparator``, ``Converter``, and ``Integrator``;
- ``PIDController`` and the example ``Hunter`` controller;
- ``BasicControlSystem`` and ``CascadeControlSystem`` containers;
- integration of arbitrary BF-System implementations through ``ControlledSystem``.

The supplied How-Tos cover a basic loop, a loop with an additional control-variable integrator, a cascade control system, and PID
controllers applied to PT1/PT2 systems.


**Learn more**

.. toctree::
   :maxdepth: 1
   :glob:

   control/*


**Cross reference**

- :ref:`Control scenarios <target_bf_control_scenarios>`
- :ref:`Ready-to-use control objects <target_bf_control_pool_objects>`
- :ref:`Howtos BF-Control <target_howto_bf_control>`
- :ref:`BF-Systems <target_bf_systems>`
- :ref:`BF-Streams <target_bf_streams>`
- :ref:`API Reference BF-Control <target_api_bf_control>`
- :ref:`API Reference BF-Control Pool Objects <target_pool_bf_control>`
