.. _target_bf_systems_04:

PT2 System
==========

Overview
--------

``PT2`` is the ready-to-use second-order demo system in the BF-Systems pool. Compared with ``PT1``, it can represent damped or
oscillatory second-order behavior and is therefore useful for more demanding closed-loop control examples.

A common continuous reference form is

.. math::

   G(s) = \frac{K \omega_0^2}{s^2 + 2 D \omega_0 s + \omega_0^2}

where ``K`` is the gain, ``D`` the damping ratio, and ``omega_0`` the characteristic angular frequency. The MLPro implementation
simulates the corresponding dynamics numerically with ``C_SAMPLE_FREQ`` internal integration steps per system cycle.

The state and action spaces are one-dimensional Euclidean spaces. The generated system output is limited to the configured
boundaries. Internally, the implementation stores the output and its first derivative over the configured maximum number of
cycles.


Configuration
-------------

The main constructor parameters are:

- ``p_K``: gain factor;
- ``p_D``: damping ratio;
- ``p_omega_0``: characteristic angular frequency;
- ``p_sys_num``: numeric identifier used for the state/action dimension name;
- ``p_max_cycle``: number of control cycles for which the internal simulation buffers are allocated;
- ``p_y_start``: initial output value;
- ``p_boundaries``: lower and upper output limits;
- ``p_latency``: duration of one externally visible system cycle.

The damping ratio determines the familiar second-order regimes: values below one lead to underdamped behavior, one gives critical
damping, and values above one lead to overdamped behavior.

.. image::
    images/time_behavior_pt2_system.png
    :width: 750 px


Usage
-----

.. code-block:: python

    from datetime import timedelta
    from mlpro.bf.systems.pool import PT2

    system = PT2(
        p_K=1.0,
        p_D=0.7,
        p_omega_0=1.0,
        p_sys_num=0,
        p_max_cycle=1000,
        p_y_start=0.0,
        p_latency=timedelta(seconds=0.1),
    )


**Cross Reference**

- :ref:`State-based systems <target_bf_systems>`
- :ref:`Howto BF-CONTROL-102: PID Controller with PT2 system <Howto_BF_CONTROL_102>`
- :ref:`PID Controller <target_bf_control_pid>`
- :ref:`API Reference <target_api_bf_systems_pool_pt2_system>`
