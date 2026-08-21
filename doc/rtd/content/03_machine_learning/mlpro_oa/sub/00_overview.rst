.. _target_oa_overview:

Overview
========

MLPro-OA is the youngest sub-framework of MLPro. It extends the common foundations of MLPro with mechanisms for **online
adaptivity**: models and processing pipelines can react to new information while they are operating instead of relying
exclusively on an offline-trained, static configuration.

The sub-framework opens up two powerful application domains:

**Online-adaptive data stream processing**
    :ref:`MLPro-OA-Streams <target_oa_streams>` combines BF-Streams with the adaptive-model semantics of BF-ML. It standardizes
    online-adaptive stream tasks and workflows, forward and reverse adaptation, adaptation events, renormalization, adaptive
    preprocessing, online cluster analysis, change detection, online statistics, and observation.

**Online-adaptive closed-loop control**
    :ref:`MLPro-OA-Control <target_oa_control>` combines BF-Control with the adaptive-model semantics of BF-ML and provides the
    foundation for controllers that can adapt their behavior during operation.

A substantial part of the architectural and standardization work has already been completed. MLPro-OA builds directly on the
generic adaptation semantics introduced in :ref:`MLPro-BF-ML <target_bf_ml>` and integrates them with domain-specific runtime
models. This keeps online adaptation interoperable with MLPro's established concepts for events, multitasking, workflows,
scenarios, visualization, persistence, and mathematical abstractions.

At the same time, MLPro-OA is still under active development and expansion. In its current stage it is primarily a **template
framework for implementing interoperable online-adaptive algorithms**. Ready-to-use native algorithms are available only for
selected use cases, while several functional areas currently focus on reusable abstractions, standardized templates, data
models, lifecycle semantics, and integration mechanisms for custom implementations.

This is particularly visible in online cluster analysis and change detection, where the framework foundations are already in
place but the set of ready-to-use algorithms is still growing. Cluster-based change detection is currently under development.

MLPro-OA therefore does not define one universal online-learning algorithm. Its main role is to provide common adaptation
semantics and specialized sub-frameworks that embed those semantics into concrete application domains while remaining compatible
with the lower MLPro layers.


**Cross reference**

- :ref:`MLPro-BF-ML: Machine learning foundations <target_bf_ml>`
- :ref:`MLPro-OA-Streams <target_oa_streams>`
- :ref:`MLPro-OA-Control <target_oa_control>`
