.. _target_bf_ml_train_and_tune:

Training and Hyperparameter Tuning
==================================

Overview
--------

BF-ML separates the definition of a model from the process used to train, evaluate, tune, and persist it. ``Training`` provides
the generic orchestration layer for this process and operates on a :ref:`Machine Learning Scenario <target_bf_ml_scenario>`.

This keeps the training lifecycle independent of the concrete learning paradigm. Higher ML frameworks specialize what happens in
a training cycle, how a score is determined, and when training is considered finished, while reusing the same execution,
result-management, and tuning interfaces.


Training lifecycle
------------------

A ``Training`` instance is configured with a scenario class and optional limits for training cycles and adaptations. Without
hyperparameter tuning, the training creates the scenario directly and executes custom training cycles until the configured
termination condition is reached.

``run_cycle()`` handles the common lifecycle around the custom ``_run_cycle()`` implementation. It manages run initialization,
training/evaluation counters, cycle limits, result handling, persistence, and completion logging. ``run()`` executes the complete
training and returns the resulting ``TrainingResults`` object.

The training distinguishes two generic modes:

- ``C_MODE_TRAIN`` for adaptation/training cycles.
- ``C_MODE_EVAL`` for evaluation cycles that do not count toward the training-cycle total.

The concrete interpretation of these modes is left to the specialized training implementation.


Training results and persistence
--------------------------------

``TrainingResults`` provides a common result container. It records, among other values:

- start and end timestamps and total duration;
- start/end cycle ids;
- numbers of training and evaluation cycles;
- number of adaptations;
- a generic ``highscore``;
- arbitrary custom results added by specialized training implementations.

If a training path is configured, the completed scenario is persisted below the training run. This preserves both the trained
model and its surrounding application context for later operational use. A tabular summary can additionally be written through
``TrainingResults.save()``.

The meaning of ``highscore`` is deliberately not defined at BF level. It is the common scalar optimization target used by higher
ML domains and their tuning implementations.


Hyperparameter tuning
---------------------

``HyperParamTuner`` defines the paradigm-independent tuning interface. Its public ``maximize()`` method receives the training
class, number of trials, root path, and training parameters and delegates the actual optimization strategy to ``_maximize()``.

This design allows third-party optimization technology to be connected without changing the BF-ML training contract. The tuner
varies the model's hyperparameters through the common BF-ML hyperparameter abstractions and returns the ``TrainingResults`` of the
best trial.

``HyperParamTuner.save()`` can persist the best parameter assignment and score. Concrete tuner wrappers can additionally provide
trial-level data storage.


**Cross reference**

- :ref:`Adaptive models and hyperparameters <target_bf_ml_model>`
- :ref:`Machine Learning Scenarios <target_bf_ml_scenario>`
- :ref:`Howto BF-ML-010: Hyperparameters <Howto BF ML 010>`
- :ref:`API reference BF-ML <target_api_bf_ml>`
