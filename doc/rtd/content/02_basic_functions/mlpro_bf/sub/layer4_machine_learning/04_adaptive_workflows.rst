.. _target_bf_ml_workflows:

Adaptive Workflows
==================

Overview
--------

``AWorkflow`` combines the semantics of a :ref:`Model <target_bf_ml_model>` with those of a :ref:`Workflow <target_bf_mt>`.
It is therefore both an executable task graph and an adaptive ML object.

This is the key idea: several adaptive tasks can be grouped into a larger structure that again behaves like one adaptive model.
The composition does not introduce a second ML abstraction; it reuses the same model interface at a higher level.

.. image:: images/MLPro-BF-ML-Workflow.drawio.png
   :scale: 50%


Model composition and multitasking
----------------------------------

Because the contained objects are normal MLPro tasks, an adaptive workflow can use predecessor relations, shared data, threads,
processes, and the asynchronous execution ranges provided by :ref:`BF-MT <target_bf_mt>`. ML workloads can therefore be composed
and scheduled with the same runtime mechanisms as other MLPro workflows.

``AWorkflow`` additionally propagates model-level behavior across the task graph:

**Adaptivity**
    ``switch_adaptivity()`` is forwarded to adaptive tasks. This allows a complete model group to be switched between adaptive
    and non-adaptive operation through one interface.

**Random seeds**
    ``set_random_seed()`` is propagated to contained tasks that support the common model interface.

**Adaptation state**
    ``get_adapted()`` reports whether at least one contained adaptive task has adapted.

**Buffers**
    ``clear_buffer()`` clears the buffers of contained models where supported.

**Accuracy**
    ``get_accuracy()`` aggregates the accuracy values of adaptive tasks and returns their average. If no task exposes an accuracy
    value, the workflow returns ``1``.


Composite hyperparameters
-------------------------

When an adaptive task is added, ``AWorkflow`` can extend its own ``HyperParamSpace`` by the task's hyperparameter dimensions. A
``HyperParamDispatcher`` then provides a common tuple that forwards values to the original model-specific tuples.

This creates a particularly important interoperability point: a higher-level training or tuning mechanism can work with the
hyperparameters of a composite model through the same interface used for a single model.

In conceptual form::

    Model A ----\
                 \
    Model B ------> AWorkflow ----> one adaptive model interface
                 /
    Model C ----/

The workflow can thus serve both as an execution graph and as a macro-model composed from cooperating learners.


**Cross reference**

- :ref:`Adaptive models <target_bf_ml_model>`
- :ref:`Training and hyperparameter tuning <target_bf_ml_train_and_tune>`
- :ref:`BF-MT: Multitasking <target_bf_mt>`
- :ref:`API reference BF-ML <target_api_bf_ml>`
