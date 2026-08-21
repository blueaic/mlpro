.. _target_bf_control:

Closed-loop control
===================

Overview
--------

MLPro-BF-Control provides a workflow-based model for closed-loop control. It builds on :ref:`BF-Streams <target_bf_streams>` for
instance flow, tasks, workflows, shared state, and scenarios, and on :ref:`BF-Systems <target_bf_systems>` for the controlled
plant.

The module covers the complete loop from setpoint to controlled variable. Its central objects are ``ControlData`` with the
specializations ``SetPoint``, ``ControlError``, ``ControlVariable``, and ``ControlledVariable``; ``ControlTask`` and ``Operator``
for processing; ``Controller`` and ``ControlledSystem`` for the active loop components; ``ControlWorkflow`` and ``ControlShared``
for orchestration, timing, and shared state; and ``ControlSystem`` and ``ControlPanel`` at scenario level.

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

All control signals are ``ControlData`` instances and therefore participate in the same ``InstDict``-based processing model as
BF-Streams. ``ControlWorkflow`` specializes ``StreamWorkflow`` and keeps the predecessor-based task graph, execution ranges, and
visualization model. ``ControlledSystem`` wraps a :class:`mlpro.bf.systems.System` and translates between control variables and
the System API's ``Action`` and ``State`` objects.

Control-specific shared state adds process timing, unique instance ids, latency coordination, and setpoint handling. The latency
of the controlled system therefore becomes part of the execution model rather than an external detail.


.. _target_bf_control_scenarios:
.. _target_bf_control_scenario_basic:
.. _target_bf_control_scenario_basic_int:
.. _target_bf_control_scenario_cascade:

Basic control scenarios
-----------------------

The fundamental control configurations are part of the BF-Control basics and are intentionally presented directly here rather
than hidden in a deeper documentation hierarchy.

**Basic control system**
    ``BasicControlSystem`` combines one controller with one controlled system. Internally, a ``Comparator`` creates the
    ``ControlError``, the controller computes the ``ControlVariable``, and the wrapped system returns the next
    ``ControlledVariable``.

    .. image::
        control/control_scenarios/images/01_control_system.drawio.png
        :width: 620 px

    See :ref:`Howto BF-CONTROL-001 <Howto BF CONTROL 001>` for an executable example.

**Basic control system with integrator**
    The same container can insert an ``Integrator`` after the controller. The operator accumulates successive control variables
    before they are handed to the controlled system.

    .. image::
        control/control_scenarios/images/02_control_system_with_integrator.drawio.png
        :width: 620 px

    See :ref:`Howto BF-CONTROL-002 <Howto BF CONTROL 002>`.

**Cascade control system**
    ``CascadeControlSystem`` builds nested ``ControlWorkflow`` objects. The output of an outer controller is converted into the
    setpoint of the next inner loop, while the inner controlled variable is converted back into the signal expected by the outer
    workflow. Shared timing information coordinates different latencies across the cascade.

    .. image::
        control/control_scenarios/images/03_cascade_control_system.drawio.png
        :width: 700 px

    See :ref:`Howto BF-CONTROL-003 <Howto BF CONTROL 003>`.


.. _target_bf_control_pool_objects:
.. _target_bf_control_pool_operators:
.. _target_bf_control_pool_controllers:
.. _target_bf_control_pool_systems:
.. _target_bf_control_pid:

Ready-to-use building blocks
----------------------------

BF-Control ships with a compact pool of reusable components that fit directly into the workflow model.

**Operators**
    ``Comparator`` computes ``SetPoint - ControlledVariable`` and replaces the incoming values by a ``ControlError``.
    ``Converter`` changes one ``ControlData`` type into another while preserving values and time stamp. ``Integrator`` buffers
    and cumulatively adds incoming ``ControlVariable`` values.

**Controllers**
    ``Controller`` is the template for mapping a ``ControlError`` to a ``ControlVariable``. ``PIDController`` provides a ready
    SISO PID implementation with proportional, integral, and derivative terms, timestamp-based integration/differentiation,
    optional anti-windup, and clipping to the output-space boundaries. The pool also contains the example ``Hunter`` controller.

**Controlled systems**
    ``ControlledSystem`` wraps any BF-System for use as a ``ControlTask``. Ready-to-use system models such as PT1 and PT2 from
    :ref:`BF-Systems <target_bf_systems>` can therefore be inserted directly into a control workflow.

**Control-system containers**
    ``BasicControlSystem`` and ``CascadeControlSystem`` assemble the recurring loop structures described above. Custom
    ``ControlSystem`` implementations can build arbitrary task graphs in ``_setup()`` when the supplied containers are not
    sufficient.


How-Tos and API
---------------

The BF-Control How-Tos cover the basic loop, the additional integrator, cascade control, and PID controllers with PT1/PT2 plants.
The API reference provides the detailed class and method documentation for custom implementations.

**Cross reference**

- :ref:`Howtos BF-Control <target_howto_bf_control>`
- :ref:`Howto BF-CONTROL-001: Basic control system <Howto BF CONTROL 001>`
- :ref:`Howto BF-CONTROL-002: Control system with integrator <Howto BF CONTROL 002>`
- :ref:`Howto BF-CONTROL-003: Cascade control system <Howto BF CONTROL 003>`
- :ref:`Howto BF-CONTROL-101: PID controller with PT1 system <Howto_BF_CONTROL_101>`
- :ref:`Howto BF-CONTROL-102: PID controller with PT2 system <Howto_BF_CONTROL_102>`
- :ref:`Howto BF-CONTROL-103: Cascaded PID controller <Howto_BF_CONTROL_103>`
- :ref:`BF-Systems <target_bf_systems>`
- :ref:`BF-Streams <target_bf_streams>`
- :ref:`API Reference BF-Control <target_api_bf_control>`
- :ref:`API Reference BF-Control Pool Objects <target_pool_bf_control>`
