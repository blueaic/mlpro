.. _target_bf_ml_model:

Adaptive models
===============

Overview
--------

``Model`` is the central template for adaptive machine-learning objects in MLPro. It deliberately defines only properties that
are independent of a concrete learning paradigm. Supervised learners, policies, agents, players, adaptive functions, adaptive
systems, and other higher-level ML objects can therefore share the same fundamental behavior.

.. image:: images/MLPro-BF-ML-Model.drawio.png
   :scale: 50%

``Model`` derives from ``Task`` and ``ScientificObject`` and combines capabilities from several lower BF layers with ML-specific
functionality. The result is considerably more than a common ``fit()`` interface: it is a reusable runtime and adaptation model.


Core capabilities
-----------------

**Adaptation**
    ``adapt()`` is the common entry point for explicit adaptation. Concrete models implement ``_adapt()`` and return whether an
    actual adaptation took place. Adaptivity can be switched on or off at runtime.

**Event-driven adaptation**
    ``adapt_on_event()`` provides the complementary event-based path and delegates to ``_adapt_on_event()``. This makes it
    possible to connect adaptation directly to MLPro's event infrastructure.

**Adaptation events**
    Successful adaptations are represented by ``Adaptation`` events and announced through ``C_EVENT_ADAPTED``. ``AdaptationType``
    distinguishes regular forward adaptation from event-triggered adaptation. Other ML objects can register handlers and react
    to these events, enabling adaptation chains between cooperating models.

**Execution and multitasking**
    Because ``Model`` is a ``Task``, a model can execute synchronously or within MLPro's asynchronous task infrastructure. Range,
    autorun, shared-object, and visualization concepts therefore apply to ML models as they do to other BF tasks.

**Hyperparameters**
    BF-ML represents hyperparameters using the mathematical abstractions of BF-Math. ``HyperParam`` derives from ``Dimension``,
    ``HyperParamSpace`` from ``ESpace``, and ``HyperParamTuple`` from ``Element``. A model initializes its specific parameter
    space in ``_init_hyperparam()`` and exposes its current tuple through ``get_hyperparam()``.

    A change of a hyperparameter raises ``HyperParam.C_EVENT_VALUE_CHANGED``. The model tracks whether its internal algorithm is
    synchronized with the tuple and can apply changed values through ``_update_hyperparameters()`` before adaptation.

**Buffering**
    A model can optionally create an internal ``Buffer`` by setting ``p_buffer_size``. The common ``clear_buffer()`` interface
    lets higher-level frameworks reset buffered learning data without knowing the concrete model implementation.

**Objective and accuracy**
    ``add_objective()``/``_add_objective()`` and ``get_accuracy()``/``_get_accuracy()`` provide paradigm-independent hooks for
    objective information and a normalized accuracy measure. Higher ML domains specialize the actual semantics.

**Persistence, visualization, logging, and scientific reference**
    These capabilities are inherited from lower BF layers. This means concrete ML models automatically participate in MLPro's
    persistence, plotting, logging, and scientific-reference infrastructure instead of implementing parallel mechanisms.

**Reproducibility**
    ``set_random_seed()`` offers a common hook for resetting model-side random behavior and is propagated by higher-level
    composite objects such as scenarios and adaptive workflows.


Hyperparameter composition
--------------------------

``HyperParamDispatcher`` allows several hyperparameter tuples to be represented through one common tuple. It maps each dimension
back to the original tuple and forwards read/write access. This is particularly important for composite models and
:ref:`Adaptive Workflows <target_bf_ml_workflows>`, where the parameters of several adaptive tasks can be exposed as one tuning
interface.


How-Tos
-------

:ref:`Howto BF-ML-001 <Howto BF ML 001>` demonstrates a custom ``Model`` including explicit adaptation, event-based adaptation,
execution as a task, model-specific hyperparameters, scientific referencing, and visualization.

:ref:`Howto BF-ML-010 <Howto BF ML 010>` focuses on the hyperparameter abstractions and their use.


**Cross reference**

- :ref:`Howto BF-ML-001: Adaptive model <Howto BF ML 001>`
- :ref:`Howto BF-ML-010: Hyperparameters <Howto BF ML 010>`
- :ref:`Adaptive workflows <target_bf_ml_workflows>`
- :ref:`Adaptive functions <target_bf_ml_afct>`
- :ref:`Adaptive systems <target_bf_ml_asystems>`
- :ref:`BF-MT: Multitasking <target_bf_mt>`
- :ref:`BF-Events: Event handling <target_bf_event>`
- :ref:`BF-Math: Mathematics <target_bf_mathematics>`
- :ref:`API Reference BF-ML <target_api_bf_ml>`
