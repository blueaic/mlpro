.. _Howto BF ML 001:
Howto BF-ML-001: Adaptive Model
===============================

This How-To demonstrates the central BF-ML ``Model`` abstraction. It shows how to implement a custom model, define its
hyperparameters, trigger explicit and event-based adaptation, execute it as an MLPro task, attach scientific-reference metadata,
and use the visualization hooks.

**Executable code**

.. literalinclude:: ../../../../../../../../../test/howtos/bf/ml/howto_bf_ml_001_adaptive_model.py
	:language: python


**Results**

The example logs the model lifecycle and opens the configured demo visualization when executed interactively.

.. image:: images/howto_bf_ml_001_results.png
    :scale: 75%


**Cross Reference**

- :ref:`Adaptive models <target_bf_ml_model>`
- :ref:`Machine Learning foundation <target_bf_ml>`
- :ref:`API Reference: Machine Learning <target_api_bf_ml>`
