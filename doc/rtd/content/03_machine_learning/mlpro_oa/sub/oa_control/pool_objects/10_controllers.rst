.. _target_oa_control_pool_controllers:

Online-adaptive controllers
===========================

``OAController`` is the central framework template for online-adaptive closed-loop controllers. It combines the classical
``Controller`` contract of BF-Control with the adaptive ``Model`` contract of BF-ML. A controller therefore remains a regular
MLPro control task while gaining an online-adaptation lifecycle.

During each processing cycle an ``OAController`` receives the current ``ControlError``, computes the next ``ControlVariable``,
publishes it back into the control workflow, and invokes its adaptive part with the current error and generated control variable.
A custom controller implements the regular control computation together with ``_adapt()``.

This keeps the learning mechanism local to the controller while the surrounding controlled system, operators, control panel, and
workflow continue to use the standardized BF-Control semantics. ``OAController`` also defines a setpoint-change handler hook so
concrete implementations can decide how adaptation should react when the operating target changes.

The active pool additionally provides RL-based controller integration.

.. toctree::
   :maxdepth: 2

   controllers/10_rl_policies


**Cross reference**

- :ref:`OA-Control Overview <target_oa_control_overview>`
- :ref:`API reference: OA-Control controllers <target_api_oa_control_controllers>`
- :ref:`BF-Control: Closed-loop control <target_bf_control>`
- :ref:`BF-ML: Machine learning foundations <target_bf_ml>`
