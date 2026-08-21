.. _target_oa_control_overview:

Overview
========

MLPro-OA-Control extends the closed-loop control abstractions of :ref:`MLPro-BF-Control <target_bf_control>` with the
paradigm-independent adaptation semantics of :ref:`MLPro-BF-ML <target_bf_ml>`. Its purpose is to support controllers that can
change their internal policy while the control loop is running.

Like MLPro-OA as a whole, OA-Control is still under active development and expansion. A substantial part of the architectural and
standardization work is already in place, but the set of ready-to-use adaptive control algorithms is still limited. The current
focus is therefore on reusable templates, integration mechanisms, and selected reference implementations.

.. image:: images/oa_control_architecture.svg
   :width: 700 px
   :align: center
   :alt: Simplified architecture of online-adaptive closed-loop control in MLPro-OA

The central design principle is separation of concerns: BF-Control defines the control-loop semantics, BF-ML defines generic
adaptation semantics, and OA-Control connects both without introducing a second control runtime.

The currently active scope consists of three main building blocks:

- ``OAController`` as the generic template for online-adaptive controllers;
- ``OAControllerRL`` as a wrapper that integrates compatible MLPro-RL policies into an adaptive control loop;
- ``RLPID`` as a native RL-based adaptive PID policy and one of the few ready-to-use algorithmic building blocks already
  available in OA-Control.

Several additional names are already reserved in ``mlpro.oa.control.basics`` for future online-adaptive multi-controllers,
controlled systems, panels, workflows, complete control systems, and control-specific training. These classes are currently
placeholders and are therefore not presented as active functionality.

OA-Control is designed as an extension layer rather than a replacement for BF-Control. A typical implementation starts with the
same controlled system, control panel, operators, and workflow concepts described in BF-Control and replaces only the controller
stage by an adaptive controller.

The resulting dependency chain is::

    BF-Control        -> control-loop semantics
    BF-ML             -> adaptation semantics
    MLPro-RL          -> optional learning algorithms
    ------------------------------------------------
    MLPro-OA-Control  -> online-adaptive controller integration

The detailed topics are documented separately under :ref:`Pool objects <target_oa_control_pool_objects>`.


**Cross reference**

- :ref:`Pool objects <target_oa_control_pool_objects>`
- :ref:`API reference: MLPro-OA-Control <target_api_oa_control>`
- :ref:`API reference: OA-Control controllers <target_api_oa_control_controllers>`
- :ref:`BF-Control: Closed-loop control <target_bf_control>`
- :ref:`BF-ML: Machine learning foundations <target_bf_ml>`
- `Paper "Online-adaptive PID control using Reinforcement Learning" (Conference paper) <https://doi.org/10.1109/CoDIT66093.2025.11321229>`_
- `Paper "Online-adaptive PID control using Reinforcement Learning" (GitHub repo) <https://github.com/fhswf/paper-da-ieee-codit-2025>`_
