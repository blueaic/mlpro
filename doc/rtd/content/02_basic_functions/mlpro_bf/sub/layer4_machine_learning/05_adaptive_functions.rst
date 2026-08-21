.. _target_bf_ml_afct:

Adaptive Functions
==================

Overview
--------

``AdaptiveFunction`` combines two fundamental MLPro abstractions: the mathematical :ref:`Function <target_bf_mathematics>` and
the adaptive :ref:`Model <target_bf_ml_model>`.

A normal ``Function`` defines a mapping between an input and an output space. ``AdaptiveFunction`` keeps this mathematical
contract but adds the full model semantics: adaptation, hyperparameters, task execution, event handling, buffering, persistence,
visualization, and the other common BF-ML capabilities.

.. image:: images/MLPro-BF-ML-AFct.drawio.png
   :scale: 50%

The important point is that BF-ML still does **not** prescribe a learning paradigm. ``AdaptiveFunction`` standardizes what a
learnable mapping looks like in MLPro; higher frameworks define how that mapping is learned.


Architecture
------------

The abstraction can be read as::

    Function
       +
    Model
       |
       v
    AdaptiveFunction

The constructor receives the mathematical input and output spaces and the class of the output element. At the same time it
initializes the model-side capabilities including adaptivity, buffering, asynchronous execution range, shared objects,
visualization, logging, and model-specific hyperparameters.

This makes adaptive functions a natural bridge between :ref:`BF-Math <target_bf_mathematics>` and specialized ML domains. A
higher framework can provide a concrete learner while all code consuming the function continues to work with the familiar
``map()`` semantics.


Typical roles
-------------

Adaptive functions are useful wherever an unknown or changing mapping needs to be represented through learning. Within MLPro
this includes, for example, learned prediction functions and the adaptive sub-functions used by
:ref:`Adaptive Systems <target_bf_ml_asystems>`.

They also form a natural foundation for supervised-learning implementations, where observations of input/output pairs provide
the adaptation information but the resulting model remains a mathematical mapping.


**Cross reference**

- :ref:`Adaptive models <target_bf_ml_model>`
- :ref:`Adaptive systems <target_bf_ml_asystems>`
- :ref:`BF-Math: Mathematics <target_bf_mathematics>`
- :ref:`SL: Adaptive functions for supervised learning <target_bf_sl_afct>`
- :ref:`RL: Model-based agents <target_agents_MBRL>`
- :ref:`API reference BF-ML <target_api_bf_ml>`
