.. _target_oa_stream_overview:

Overview
========

MLPro-OA-Streams extends the generic data-stream processing model of :ref:`MLPro-BF-Streams <target_bf_streams>` with the
paradigm-independent adaptation semantics of :ref:`MLPro-BF-ML <target_bf_ml>`. The result is a framework for building stream
processing pipelines whose tasks can continuously adapt while data is flowing through them.

In its current development stage, OA-Streams is primarily a **standardized template framework**. It already provides the common
runtime, adaptation lifecycle, data models, events, and integration patterns needed to implement interoperable online-adaptive
stream algorithms. Ready-to-use native algorithms are available only for selected tasks, while other areas deliberately expose
reusable templates for custom implementations.

.. image:: images/oa_streams_architecture.svg
   :width: 680 px
   :align: center
   :alt: Simplified architecture of MLPro-OA-Streams combining BF-Streams and BF-ML

At the object level this combination is explicit: ``OAStreamTask`` combines ``StreamTask`` and ``Model``;
``OAStreamWorkflow`` combines ``StreamWorkflow`` and ``AWorkflow``; and ``OAStreamScenario`` specializes the stream-scenario
model for adaptive workflows. This keeps OA processing interoperable with the execution, multitasking, visualization, event,
and persistence mechanisms already defined in the lower MLPro layers.

The core objects are:

.. _target_oa_stream_tasks:

**OAStreamTask**
    The elementary adaptive processing unit. It inherits the stream-processing behavior of ``StreamTask`` and the adaptation,
    event, buffering, visualization, and model semantics of ``Model``.

.. _target_oa_stream_workflows:

**OAStreamWorkflow**
    A processing graph for adaptive and non-adaptive stream tasks. Because it also inherits from ``AWorkflow``, the complete
    graph behaves as an adaptive model and can propagate adaptivity to its contained tasks.

**OAStreamScenario**
    The executable context that binds a stream and an ``OAStreamWorkflow``. It reuses the simulation/real-operation lifecycle of
    BF scenarios and assigns the active stream to the workflow's shared object.

**OAStreamShared**
    The shared-data object used by OA workflows. It extends ``StreamShared`` and therefore preserves the established instance
    exchange model of BF-Streams.

**OAStreamAdaptation / OAStreamAdaptationType**
    Stream-specific adaptation events. In addition to the generic BF-ML adaptation semantics they distinguish reverse and
    renormalization adaptations and carry the number of affected stream instances.

A stream is not only a sequence of new samples. In dynamic processing chains, instances can also become obsolete, preprocessing
parameters can change, and downstream models may keep internal state that depends on earlier transformations. OA-Streams makes
these situations explicit through a stream-specific adaptation lifecycle.

.. image:: images/oa_streams_adaptation_lifecycle.svg
   :width: 720 px
   :align: center
   :alt: Simplified lifecycle of forward, reverse, and renormalization adaptation in an OAStreamTask

``OAStreamTask`` supports forward adaptation on new stream instances, reverse adaptation on obsolete or removed instances,
pre- and post-adaptation hooks around the instance-wise adaptation loop, renormalization after changing normalization parameters,
and typed adaptation events through ``OAStreamAdaptation`` and ``OAStreamAdaptationType``.

This event-oriented interaction is particularly important in multi-stage pipelines. For example, an adaptive boundary detector
may change the observed data range, an adaptive normalizer can react to the new boundaries, and downstream tasks can then
renormalize buffered state. Adaptation therefore becomes a property of the complete processing chain rather than an isolated
method call inside one algorithm.

OA workflows are intentionally hybrid. A workflow may contain adaptive OA tasks and ordinary BF stream tasks side by side. This
is useful because not every processing step needs to learn. Rearranging dimensions, buffering a window, deriving features, or
other deterministic processing can remain in BF-Streams while only selected stages adapt online.

The active functional scope is summarized below.

.. image:: images/oa_streams_functional_landscape.svg
   :width: 760 px
   :align: center
   :alt: Simplified functional landscape of adaptive preprocessing, cluster analysis, change detection, and auxiliary functionality in OA-Streams

**Adaptive preprocessing**
    Boundary detection and online-adaptive MinMax/Z-transformation normalizers provide selected ready-to-use preprocessing
    functionality within the common OA task model.

**Online cluster analysis**
    ``ClusterAnalyzer`` standardizes the architecture for custom online clustering algorithms: cluster management, memberships
    and influences, creation/removal events, visualization, renormalization, and extensible cluster properties. The framework
    currently focuses on templates rather than a broad pool of ready-to-use cluster analyzers.

**Change detection**
    Change detection is the common framework-level domain for identifying relevant changes in an evolving stream. ``Change`` and
    ``ChangeDetector`` provide the shared event, status, buffering, and visualization semantics. **Anomaly detection** and
    **drift detection** are subordinate specialized domains built on top of this common foundation. The current focus is on
    templates and standardized detector semantics; cluster-based change detection is still under development.

**Auxiliary functionality**
    Supporting components complement the main processing areas without defining another primary domain. This currently includes
    **online statistics**, such as ``MovingAverage``, and **observation and helpers** for monitoring adaptation, clusters, and
    detected changes without becoming part of the processing logic itself.


**Cross reference**

- :ref:`Howtos OA-Streams <target_appendix1_OA_streams>`
- :ref:`Howto OA-PP-121: Complex preprocessing with parallel tasks <Howto_OA_PP_121>`
- :ref:`API reference: MLPro-OA-Streams <target_api_oa_streams>`
- :ref:`BF-Streams: Data stream processing <target_bf_streams>`
- :ref:`BF-ML: Adaptive models and workflows <target_bf_ml>`
