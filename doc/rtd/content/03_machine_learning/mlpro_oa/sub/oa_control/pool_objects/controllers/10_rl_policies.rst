.. _target_oa_control_pool_controllers_rl_policies:

RL policies
===========

``OAControllerRL`` integrates a regular MLPro-RL ``Policy`` and reward function into an ``OAController``. It is an
algorithm-neutral bridge between MLPro-RL and the OA-Control runtime rather than a learning algorithm of its own.

The wrapper converts the current ``ControlError`` into an RL ``State`` and lets the wrapped policy compute an ``Action``. That
action is converted back into a ``ControlVariable`` for the control workflow. From the second cycle onward, the wrapper builds a
SARS transition from the previous state and action, the current state, and the reward computed by the supplied reward function.
The resulting transition is then used to adapt the wrapped policy online.

Conceptually::

    ControlError
        |
        v
    RL State ---> RL Policy ---> RL Action ---> ControlVariable
        ^              |
        |              | adapt from SARS
        +---- Reward <-+

Any compatible MLPro-RL policy can supply the actual learning algorithm. OA-Control standardizes how that policy participates in
the closed-loop control process.

The current native RL-based policy for adaptive PID control is documented below.

.. toctree::
   :maxdepth: 1

   rl_policies/01_RLPID


**Cross reference**

- :ref:`Online-adaptive controllers <target_oa_control_pool_controllers>`
- :ref:`OA-Control Overview <target_oa_control_overview>`
- :ref:`API reference: OA-Control controllers <target_api_oa_control_controllers>`
