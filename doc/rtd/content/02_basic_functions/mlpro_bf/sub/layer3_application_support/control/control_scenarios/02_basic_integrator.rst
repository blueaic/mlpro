.. _target_bf_control_scenario_basic_int:

Basic control system with additional integrator
-----------------------------------------------

``BasicControlSystem`` can optionally insert an ``Integrator`` between the controller and the controlled system. This variant is
useful when the controller output represents an increment rather than an absolute control value.

The ``Integrator`` is a BF-Control ``Operator``. It consumes the current ``ControlVariable``, accumulates its values with the
previous result, and replaces the original instance by a new integrated ``ControlVariable`` with a fresh id and timestamp.

The resulting workflow is therefore::

    Comparator -> Controller -> Integrator -> ControlledSystem

.. image::
    images/02_control_system_with_integrator.drawio.png
    :scale: 50%

The executable :ref:`Howto BF-CONTROL-002 <Howto BF CONTROL 002>` shows how the integration stage is activated through
``p_ctrl_var_integration=True``.


**Cross Reference**

- :ref:`Howto BF-CONTROL-002: Control system with integrator <Howto BF CONTROL 002>`
- :ref:`Operators <target_bf_control_pool_operators>`
- :ref:`Basic control system <target_bf_control_scenario_basic>`
- :ref:`BF-Control overview <target_bf_control>`
