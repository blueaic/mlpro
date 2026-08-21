.. _target_oa_overview:

Overview
========

MLPro-OA extends the common foundations of MLPro with mechanisms for **online adaptivity**: models and processing pipelines can react to new information while they are operating instead of relying exclusively on an offline-trained, static configuration.

The sub-framework builds directly on the generic adaptation semantics introduced in :ref:`MLPro-BF-ML <target_bf_ml>` and combines them with domain-specific runtime models. This keeps online adaptation interoperable with MLPro's established concepts for events, multitasking, workflows, scenarios, visualization, persistence, and mathematical abstractions.

The currently documented scope of MLPro-OA comprises two major application areas:

**Online-adaptive data stream processing**
    :ref:`MLPro-OA-Streams <target_oa_streams>` combines BF-Streams with the adaptive-model semantics of BF-ML. It provides online-adaptive stream tasks and workflows, forward and reverse adaptation, adaptation events, renormalization cascades, adaptive preprocessing, online cluster analysis, change detection, online statistics, and observation.

**Online-adaptive closed-loop control**
    :ref:`MLPro-OA-Control <target_oa_control>` applies the same principle to closed-loop control and provides the foundation for controllers that can adapt their behavior during operation.

This separation is intentional: MLPro-OA does not define one universal online-learning algorithm. Instead, it provides common adaptation semantics and specialized sub-frameworks that embed those semantics into concrete application domains while remaining compatible with the lower MLPro layers.


**Cross reference**

- :ref:`MLPro-BF-ML: Machine learning foundations <target_bf_ml>`
- :ref:`MLPro-OA-Streams <target_oa_streams>`
- :ref:`MLPro-OA-Control <target_oa_control>`
