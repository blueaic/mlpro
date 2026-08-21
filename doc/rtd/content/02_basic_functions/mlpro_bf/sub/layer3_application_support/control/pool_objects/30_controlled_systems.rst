.. _target_bf_control_pool_systems:

Controlled systems
==================

``ControlledSystem`` is the adapter between BF-Control and :ref:`BF-Systems <target_bf_systems>`. It wraps a
``mlpro.bf.systems.System`` as a ``ControlTask`` so the plant can be placed directly inside a ``ControlWorkflow``.

For an incoming ``ControlVariable``, the wrapper creates a BF-Systems ``Action`` and processes it on the wrapped system. The
current system ``State`` is then translated back into a new ``ControlledVariable`` for the feedback path. The wrapper also
forwards reset and visualization calls to the underlying system.

Timing is coordinated through ``ControlShared``. The wrapped system's latency determines when a new action becomes active; the
smallest latency across a nested control configuration determines the basic timing increment for system processing.

Native ``System`` objects can also be passed directly to ``BasicControlSystem`` and ``CascadeControlSystem``. These containers
wrap them automatically as ``ControlledSystem`` tasks.


**Cross Reference**

- :ref:`BF-Control overview <target_bf_control>`
- :ref:`BF-Systems <target_bf_systems>`
- :ref:`Basic control system <target_bf_control_scenario_basic>`
- :ref:`Cascade control system <target_bf_control_scenario_cascade>`
- :ref:`API Reference BF-Control Pool Objects <target_pool_bf_control>`
