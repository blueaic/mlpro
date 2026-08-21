.. _target_bf_ml:

Layer 4 - Machine Learning
==========================

Why a machine-learning foundation already at BF level?
------------------------------------------------------

Machine learning in MLPro is not introduced first at the level of supervised learning, reinforcement learning, game theory,
or another concrete learning paradigm. Its fundamental semantics are anchored one layer deeper, in the Basic Functions.

There are two reasons for this architectural decision:

1. **To define the fundamental nature of machine learning independently of any specific learning paradigm and anchor it
   unambiguously at a deep level of MLPro.**
2. **To provide a common foundation on which specialized, interoperable ML sub-frameworks can be built.**

This common foundation gives all higher ML domains the same basic language for adaptation, hyperparameters, execution,
events, workflows, scenarios, training, persistence, and model composition. Concrete learning paradigms can therefore focus on
their domain-specific semantics without redefining what an adaptive model is.


Overview
--------

The central abstraction of BF-ML is :ref:`Model <target_bf_ml_model>`. It combines adaptivity with capabilities inherited from
lower BF layers, including task execution, multitasking, event handling, persistence, buffering, visualization, logging, and
scientific referencing. BF-ML adds a paradigm-independent hyperparameter model and a common adaptation-event semantics on top.

.. image:: layer4_machine_learning/images/MLPro-BF-ML_Overview.drawio.png
    :scale: 45 %

Around ``Model``, BF-ML defines the generic building blocks from which higher ML frameworks are composed. The three core topics
form the common ML foundation used by all higher learning domains:

**Adaptive Models**
    The common template for adaptive ML objects. A model can be adapted explicitly or in reaction to events, can expose
    hyperparameters, execute as a task, buffer data, report accuracy, raise adaptation events, and participate in MLPro's
    multitasking infrastructure.

**Machine Learning Scenarios**
    The operational context in which a model acts and learns. A scenario combines an adaptive model with cycle management,
    operation mode, visualization, persistence, and the runtime semantics inherited from ``ScenarioBase``.

**Training and Hyperparameter Tuning**
    Generic training orchestration, result handling, persistence, limits, scoring hooks, and optional hyperparameter tuning are
    standardized independently of the concrete learning paradigm.

A useful mental model for this core is::

    Model -> Scenario -> Training

The adaptive model defines the learner, the scenario defines its operational context, and training standardizes how the model is
adapted and evaluated inside that context.


**Core topics**

.. toctree::
   :maxdepth: 1

   layer4_machine_learning/01_model
   layer4_machine_learning/02_ml_scenarios
   layer4_machine_learning/03_training_and_tuning


Advanced Topics
---------------

On top of this common core, BF-ML provides further paradigm-independent abstractions for composing adaptive models, turning
mathematical functions into learnable functions, and embedding learning capabilities into state-based systems.

**Adaptive Workflows**
    ``AWorkflow`` is both a workflow and a model. It allows several adaptive tasks to form a higher-level adaptive model while
    propagating adaptivity and combining their hyperparameters and runtime capabilities.

**Adaptive Functions**
    ``AdaptiveFunction`` combines the mathematical abstraction ``Function`` with ``Model``. It standardizes learnable mappings
    without prescribing how they are learned.

**Adaptive Systems**
    BF-ML combines the semantics of :ref:`BF-Systems <target_bf_systems>` with adaptive models. This provides generic building
    blocks for learned state-transition, success, and broken-state functions and for adaptive system models.

These extensions preserve the same underlying semantics::

    Model + Workflow -> Adaptive Workflow
    Model + Function -> Adaptive Function
    Model + System   -> Adaptive System

.. toctree::
   :maxdepth: 1

   layer4_machine_learning/04_adaptive_workflows
   layer4_machine_learning/05_adaptive_functions
   layer4_machine_learning/06_adaptive_systems

In this way BF-ML acts as the common ML foundation of MLPro. Supervised Learning, Reinforcement Learning, Game Theory, Online
Adaptive Processing, and other higher domains can reuse the same semantics instead of creating isolated model abstractions.


**Cross reference**

- :ref:`Howto BF-ML-001: Adaptive model <Howto BF ML 001>`
- :ref:`Howto BF-ML-010: Hyperparameters <Howto BF ML 010>`
- :ref:`BF-MT: Multitasking <target_bf_mt>`
- :ref:`BF-Events: Event handling <target_bf_event>`
- :ref:`BF-Math: Mathematics <target_bf_mathematics>`
- :ref:`BF-Systems: State-based systems <target_bf_systems>`
- :ref:`API reference BF-ML - Machine learning <target_api_bf_ml>`
