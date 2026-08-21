.. _target_bf_control_pool_operators:

Operators
=========

BF-Control operators are reusable ``ControlTask`` implementations that transform typed control data inside a workflow.

The current pool provides:

- ``Comparator``: consumes ``SetPoint`` and ``ControlledVariable`` and creates a ``ControlError`` as their difference.
- ``Converter``: changes the semantic control-data type while preserving value space, values, and timestamp. It is used heavily
  when connecting nested cascade workflows.
- ``Integrator``: accumulates incoming ``ControlVariable`` values and emits a new integrated ``ControlVariable``.

Because ``Operator`` derives from ``ControlTask`` and therefore ``StreamTask``, these components can be inserted into normal
predecessor-based BF-Control workflows and participate in the same shared-data and execution model.


**Cross Reference**

- :ref:`BF-Control overview <target_bf_control>`
- :ref:`Control scenarios <target_bf_control_scenarios>`
- :ref:`Basic control system with additional integrator <target_bf_control_scenario_basic_int>`
- :ref:`Cascade control system <target_bf_control_scenario_cascade>`
- :ref:`API Reference BF-Control Pool Objects <target_pool_bf_control>`
