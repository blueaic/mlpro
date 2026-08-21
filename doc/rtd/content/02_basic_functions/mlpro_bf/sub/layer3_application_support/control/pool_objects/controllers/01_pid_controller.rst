.. _target_bf_control_pid:

PID Controller
==============

Overview
--------

``PIDController`` is the ready-to-use SISO PID implementation in BF-Control. It derives from ``Controller`` and therefore consumes
a ``ControlError`` and produces a ``ControlVariable`` inside a ``ControlWorkflow``.

The implementation uses the parameterization ``Kp``, ``Tn`` and ``Tv``:

.. math::

   u(t) = K_p e(t) + \frac{K_p}{T_n} \int e(t)\,dt + K_p T_v \frac{de(t)}{dt}

``p_integral_off`` and ``p_derivitave_off`` can disable the integral and derivative terms independently. The spelling
``p_derivitave_off`` follows the current public constructor parameter. Optional anti-windup limits can constrain the accumulated
integral value before the controller output is calculated.

The implementation derives its time step from the timestamps of consecutive ``ControlError`` objects. The first evaluation has no
previous timestamp and therefore starts without a derivative increment or time-based integral increment. Finally, the resulting
control variable is clipped to the boundaries of the first dimension of the configured output space.


Using the controller
--------------------

A PID controller is configured with matching input and output spaces. In a typical BF-Control setup these correspond to the
controlled-system state and action spaces:

.. code-block:: python

    from mlpro.bf.control.controllers.pid_controller import PIDController

    controller = PIDController(
        p_input_space=system.get_state_space(),
        p_output_space=system.get_action_space(),
        p_Kp=1.5,
        p_Tn=1.4,
        p_Tv=0.0,
        p_integral_off=False,
        p_derivitave_off=True,
    )

The controller parameters can also be changed during runtime through ``set_parameter()``. ``get_parameter_values()`` returns the
current ``Kp``, ``Tn`` and ``Tv`` values as a NumPy array.


How-Tos
-------

The supplied examples use the PID controller with the ready-to-use BF-Systems models and in cascaded configurations:

- :ref:`BF-CONTROL-101: PID Controller with PT1 system <Howto_BF_CONTROL_101>`
- :ref:`BF-CONTROL-102: PID Controller with PT2 system <Howto_BF_CONTROL_102>`
- :ref:`BF-CONTROL-103: Cascaded PID control <Howto_BF_CONTROL_103>`


**Cross Reference**

- :ref:`Controllers <target_bf_control_pool_controllers>`
- :ref:`PT1 System <target_bf_systems_03>`
- :ref:`PT2 System <target_bf_systems_04>`
- :ref:`API Reference <target_api_bf_control_controllers_pid_controller>`
