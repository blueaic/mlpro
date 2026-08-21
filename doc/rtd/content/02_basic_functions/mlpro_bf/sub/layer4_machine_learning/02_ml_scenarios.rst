.. _target_bf_ml_scenario:

Machine Learning Scenarios
==========================

Overview
--------

An adaptive model does not operate in isolation. It learns and acts in a concrete context: a dataset, a data stream, a simulated
system, a real process, or another application-specific environment. BF-ML standardizes this relationship through ``Scenario``.

A useful distinction is:

- **Model** = the adaptive object.
- **Scenario** = the executable context in which the model operates and learns.

The concrete semantics of that context are intentionally left to higher ML domains. BF-ML defines only the common lifecycle and
runtime contract.

.. image:: images/MLPro-BF-ML-Scenario.drawio.png
   :scale: 50%


Scenario lifecycle
------------------

``Scenario`` derives from :ref:`ScenarioBase <target_bf_ops>` and adds explicit ownership of a ``Model``. Its custom ``_setup()``
method creates and returns that model. The framework then manages the model as part of the scenario lifecycle.

The inherited scenario functionality provides operation mode, cycle management, timing, visualization, logging, and persistence.
BF-ML adds model-specific coordination on top:

**Adaptivity**
    ``p_ada`` determines whether the model created by the scenario is adaptive. Higher-level scenario implementations can expose
    this switch without changing the underlying model API.

**Logging and visualization**
    Logging changes and plot initialization/updates are propagated to the internal model.

**Reproducibility**
    Resetting the scenario also resets the model's random seed through the common ``set_random_seed()`` interface.

**Persistence**
    When a scenario is persisted, the model can be stored separately in a dedicated ``model`` subfolder. During loading, the
    scenario restores the model and reconnects it to the runtime state. This allows a trained model and its surrounding scenario
    context to remain one reproducible application unit.

The resulting abstraction is reused by higher ML frameworks, where the generic cycle receives domain-specific meaning such as a
training sample, a stream instance, a reinforcement-learning interaction, or another adaptive processing step.


**Cross reference**

- :ref:`Adaptive models <target_bf_ml_model>`
- :ref:`Training and hyperparameter tuning <target_bf_ml_train_and_tune>`
- :ref:`BF-OPS: ScenarioBase <target_bf_ops>`
- :ref:`API reference BF-ML <target_api_bf_ml>`
