.. _target_bf_systems_03:

PT1 System
==========

Overview
--------

``PT1`` is the ready-to-use first-order demo system in the BF-Systems pool. It models a proportional first-order lag and is
particularly useful for control examples, controller tuning experiments, and tests that need a simple dynamic plant.

The continuous reference model is commonly written as

.. math::

   G(s) = \frac{K}{T s + 1}

with gain ``K`` and time constant ``T``. The MLPro implementation evaluates the dynamics numerically. For every control cycle it
splits the configured system latency into ``C_SAMPLE_FREQ`` internal steps and recursively updates the system output.

The state and action spaces are both one-dimensional Euclidean spaces. Their dimension is named from ``p_sys_num`` and uses the
configured output boundaries. The resulting state is clipped to these boundaries after every simulated reaction.


Configuration
-------------

The main constructor parameters are:

- ``p_K``: gain factor;
- ``p_T``: time constant;
- ``p_sys_num``: numeric identifier used for the state/action dimension name;
- ``p_y_start``: initial output value;
- ``p_boundaries``: lower and upper output limits;
- ``p_latency``: duration of one externally visible system cycle.

``reset()`` restores the configured start value and marks the resulting state as initial.

.. image::
    images/time_behavior_pt1_system.png
    :width: 750 px


Usage
-----

.. code-block:: python

    from datetime import timedelta
    from mlpro.bf.systems.pool import PT1

    system = PT1(
        p_K=1.0,
        p_T=2.0,
        p_sys_num=0,
        p_y_start=0.0,
        p_boundaries=[-250, 250],
        p_latency=timedelta(seconds=0.1),
    )

The model is used directly by the BF-Control PID How-Tos.


**Cross Reference**

- :ref:`State-based systems <target_bf_systems>`
- :ref:`Howto BF-CONTROL-101: PID Controller with PT1 system <Howto_BF_CONTROL_101>`
- :ref:`PID Controller <target_bf_control_pid>`
- :ref:`API Reference <target_api_bf_systems_pool_pt1_system>`
