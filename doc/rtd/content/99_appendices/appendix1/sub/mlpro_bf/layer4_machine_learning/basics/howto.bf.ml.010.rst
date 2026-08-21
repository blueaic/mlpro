.. _Howto BF ML 010:
Howto BF-ML-010: Hyperparameters
================================

This How-To focuses on the BF-ML hyperparameter abstractions. It demonstrates how hyperparameters are represented through
``HyperParam``, ``HyperParamSpace``, and ``HyperParamTuple`` and how individual values can be accessed and changed through the
common mathematical interface.

**Executable code**

.. literalinclude:: ../../../../../../../../../test/howtos/bf/ml/howto_bf_ml_010_hyperparameters.py
	:language: python


**Results**

.. code-block:: bash

    Variable with ID num_states = 100.00
    Variable with ID smoothing = 0.04
    Variable with ID lr_rate = 0.00
    Variable with ID buffer_size = 100000.00
    Variable with ID update_rate = 100.00
    Variable with ID sampling_size = 256.00

    A new value for variable ID ids_[0]
    Variable with ID ids_[0] = 50.00


**Cross Reference**

- :ref:`Adaptive models and hyperparameters <target_bf_ml_model>`
- :ref:`Training and hyperparameter tuning <target_bf_ml_train_and_tune>`
- :ref:`API Reference: Machine Learning <target_api_bf_ml>`
