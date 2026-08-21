.. _target_bf_systems:

State-based systems
===================

Overview
--------

MLPro-BF-Systems provides a common model for state-based systems in simulation and real operation. A system is described by a
**state space**, an **action space**, its current :class:`State`, and a transition from the current state to the next state after an
:class:`Action` has been applied.

The central objects are:

- **State**: the current condition of a system. Besides its values and timestamp, a state can be marked as initial, terminal,
  successful, broken, or timed out.
- **Action / ActionElement**: the input applied to a system. An action can contain several action elements, for example for
  multi-agent or multi-source setups.
- **System**: the common execution model for simulated and real systems. It combines state transitions, terminal-state
  assessment, timing, persistence, visualization, task execution, and real/simulated operation modes.
- **FctSTrans, FctSuccess, FctBroken**: interchangeable function templates for state transition, success assessment, and
  broken-state assessment. The same behavior can alternatively be implemented directly in a custom System subclass.
- **Sensor, Actuator, SAGateway**: the hardware-facing abstraction for reading state-related values from sensors and writing
  action-related values to actuators.
- **MultiSystem / SystemShared**: infrastructure for composing several systems and exchanging mapped state/action values between
  them.
- **DemoScenario**: a lightweight scenario for exercising and validating a system with generated or predefined actions.

A compact mental model is therefore::

    Action -> System -> State
                |        |
                |        +-> success / broken / terminal
                +-> simulated transition or real hardware access


System execution model
----------------------

A custom system normally starts by defining its state and action spaces in ``setup_spaces()``. During operation,
``process_action()`` applies an action and updates the current state. In simulated mode this is based on the state-transition
logic of the system or an externally supplied ``FctSTrans`` object. In real mode, MLPro can obtain state values from sensors and
forward action values to actuators through one or more ``SAGateway`` objects.

The execution cycle also evaluates the resulting state for success and breakdown. These checks can be implemented directly in
the system through ``_compute_success()`` and ``_compute_broken()`` or delegated to ``FctSuccess`` and ``FctBroken`` objects.
This separates the physical or logical system dynamics from application-specific terminal-state criteria when desired.

``System`` also participates in MLPro's task architecture and supports latency/timestep handling, reset, persistence, and
visualization. This makes the same system implementation reusable from standalone demonstrations, control applications, and
higher-level ML scenarios.


Simulation, hardware, and composed systems
------------------------------------------

**Simulation.** Native Python implementations can provide ``_simulate_reaction()`` directly. MLPro also supports optional
MuJoCo-backed systems through the separate MLPro-Int-MuJoCo integration. See :ref:`MuJoCo integration <target_bf_systems_mujoco>`.

**Real systems.** ``Sensor`` and ``Actuator`` objects are dimensions exposed by an ``SAGateway``. A system maps state dimensions
to sensors and action dimensions to actuators and can then use the same System API in real mode. See
:ref:`Hardware access <target_bf_systems_hardware>` and :ref:`Howto BF-SYSTEMS-010 <Howto BF SYSTEMS 010>`.

**Composed systems.** ``MultiSystem`` and ``SystemShared`` provide the basis for connecting several systems and mapping values
between their state and action dimensions. They build on MLPro's task/workflow infrastructure so that coupled systems can also
participate in asynchronous execution.


Ready-to-use systems
--------------------

The systems pool contains reusable examples and benchmark components, including first- and second-order systems (``PT1`` and
``PT2``), double-pendulum systems, and the Fox system. PT1 and PT2 are especially useful together with BF-Control for building
and testing closed-loop control configurations.

.. image::
    images/Systems.drawio.png
    :width: 550 px


**Learn more**

.. toctree::
   :maxdepth: 1
   :glob:

   systems/*


**Cross reference**

- :ref:`Howto BF-SYSTEMS-001: Demonstrating native systems <Howto BF SYSTEMS 001>`
- :ref:`Howto BF-SYSTEMS-010: System, SAGateway, Actuator, Sensor <Howto BF SYSTEMS 010>`
- :ref:`BF-Control <target_bf_control>`
- `MLPro-Int-MuJoCo <https://mlpro-int-mujoco.readthedocs.io>`_
- :ref:`API reference BF-Systems <target_ap_bf_systems>`
- :ref:`API reference BF-Systems sample pool <target_pool_bf_systems>`
