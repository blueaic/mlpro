.. _target_bf_ml_systems:
.. _target_bf_ml_asystems:

Adaptive Systems
================

Overview
--------

BF-ML extends the generic :ref:`BF-Systems <target_bf_systems>` abstraction with adaptive models. The resulting classes provide
a common foundation for systems whose internal behavior is not completely fixed but can be learned or updated from data.

This is particularly relevant when a state-transition model, success criterion, or failure criterion is unknown, too complex for
an exact analytical description, or expected to change over time. Instead of introducing a separate interface for learned system
models, BF-ML combines the existing ``System`` and ``Model`` semantics.

The current source package ``mlpro.bf.ml.systems`` provides:

- ``AFctBase`` as the common wrapper for adaptive system functions;
- ``AFctSTrans`` for an adaptive state-transition function;
- ``AFctSuccess`` for an adaptive success-state assessment;
- ``AFctBroken`` for an adaptive broken-state assessment;
- ``ASystem`` as the adaptive counterpart of a state-based ``System``.


Adaptive system functions
-------------------------

``AFctBase`` is itself a ``Model`` and embeds a concrete adaptive function. It keeps references to the system's state and action
spaces and derives the input/output spaces required by the embedded learner.

The specialized classes connect this mechanism to the standard BF-System function types:

**AFctSTrans**
    Combines the current state and action into the input of the embedded adaptive function. The function output represents the
    predicted next ``State``. Adaptation can use observed triples ``(state, action, next state)``.

**AFctSuccess**
    Maps a system state to an adaptive estimate of whether it represents a success state.

**AFctBroken**
    Provides the corresponding adaptive abstraction for broken/failure-state assessment.

All wrappers forward common model capabilities such as adaptivity, random seeds, buffering, accuracy, visualization, and
hyperparameters to their embedded adaptive function. Higher ML domains can therefore exchange the concrete learning algorithm
without changing the surrounding system interface.


Adaptive state-based systems
----------------------------

``ASystem`` combines ``System`` and ``Model``. It can use normal or adaptive implementations of state-transition, success, and
broken-state functions while preserving the regular BF-System interface for states, actions, simulation/real operation, latency,
visualization, and hardware-related behavior.

Conceptually::

    State + Action
         |
         v
     AFctSTrans  ----> next State

     State ----> AFctSuccess ----> success assessment
     State ----> AFctBroken  ----> broken assessment

                 |
                 v
              ASystem

The adaptive functions participate in the model lifecycle of the system. ``ASystem.switch_adaptivity()`` propagates the global
adaptivity setting to the contained functions, while ``_adapt()`` can delegate incoming adaptation information to them.

This architecture provides a low-level foundation for learned simulations, adaptive process models, and data-driven digital-twin
components. The actual learning paradigm remains the responsibility of higher ML frameworks or the concrete adaptive-function
implementation.


**Cross reference**

- :ref:`Adaptive models <target_bf_ml_model>`
- :ref:`Adaptive functions <target_bf_ml_afct>`
- :ref:`BF-Systems: State-based systems <target_bf_systems>`
- :ref:`API reference BF-ML <target_api_bf_ml>`
