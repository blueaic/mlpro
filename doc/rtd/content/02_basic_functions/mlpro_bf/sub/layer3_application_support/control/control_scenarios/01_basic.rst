.. _target_bf_control_scenario_basic:

Basic control system
--------------------

``BasicControlSystem`` is the compact container for a conventional single-loop control configuration. It combines one
``Controller`` with one controlled system and internally builds the required ``ControlWorkflow`` around them.

The workflow contains the standard feedback path: a ``Comparator`` computes the ``ControlError`` from setpoint and controlled
variable, the controller generates the ``ControlVariable``, and the ``ControlledSystem`` applies it to the wrapped BF-System and
returns the new ``ControlledVariable``.

A native :class:`mlpro.bf.systems.System` can be supplied directly; the control-system container wraps it automatically as a
``ControlledSystem`` task.

.. image::
    images/01_control_system.drawio.png
    :scale: 50%

The executable :ref:`Howto BF-CONTROL-001 <Howto BF CONTROL 001>` demonstrates the complete setup and execution of this basic
closed-loop architecture.


**Cross Reference**

- :ref:`Howto BF-CONTROL-001: Basic control system <Howto BF CONTROL 001>`
- :ref:`Control scenarios <target_bf_control_scenarios>`
- :ref:`BF-Control overview <target_bf_control>`
- :ref:`BF-Systems <target_bf_systems>`
