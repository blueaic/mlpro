.. _target_oa_cluster_analysis:

Online Cluster Analysis
=======================

Overview
--------

Online cluster analysis continuously maintains a structural description of a data stream while new observations arrive and old
observations may disappear from the active context. In its current development stage, MLPro-OA primarily provides the
**standardized framework and templates for implementing custom online cluster analyzers** rather than a broad collection of
ready-to-use clustering algorithms.

The current architecture separates the cluster-analysis contract, reusable cluster-management infrastructure, and integration
into an online-adaptive stream task. Three classes are central:

- ``ClusterActions`` defines the common public API through which cluster-based functionality can access a current cluster model.
- ``ClusterInfrastructure`` implements reusable, task-internal handling of clusters, properties, memberships, influences, and
  cluster lifecycle operations.
- ``ClusterAnalyzer`` combines that infrastructure with ``OAStreamTask`` and thereby turns a concrete clustering algorithm into
  an online-adaptive stream-processing task.

This separation is important for custom implementations. A component that only needs to consume cluster results can depend on
``ClusterActions`` instead of a particular analyzer implementation, while analyzer developers can reuse
``ClusterInfrastructure`` for the common mechanics of cluster handling and concentrate their own implementation on the actual
clustering algorithm.


ClusterActions: common cluster-analysis API
-------------------------------------------

``ClusterActions`` is the smallest common contract of the cluster-analysis stack. It exposes the current ``clusters`` collection
and standardizes queries that relate an ``Instance`` to that cluster model.

The two principal operations are:

- ``get_cluster_memberships()`` for relative membership values;
- ``get_cluster_influences()`` for relative influence values.

Both operations use the common ``ResultItem`` representation consisting of a cluster id, a result value, and the corresponding
cluster object. Result scopes allow callers either to inspect all applicable clusters or to request only the strongest result.

For integrations, this class is therefore the preferred API boundary whenever a consumer needs cluster information without
requiring the full adaptive task interface of ``ClusterAnalyzer``.


ClusterInfrastructure: reusable cluster handling
------------------------------------------------

``ClusterInfrastructure`` implements the common mechanics behind cluster-based tasks. It derives from ``ClusterActions`` and
provides the standardized internal machinery needed by cluster analyzers and potentially other cluster-oriented components.

Its responsibilities include:

- storage of the current clusters and generation of cluster ids;
- checking limits before new clusters are created;
- protected operations for adding and removing clusters;
- declaration and alignment of cluster properties through ``C_CLUSTER_PROPERTIES``;
- common computation of cluster memberships and influences;
- result scopes and optional influence thresholds;
- access to the configured cluster class.

The architectural intention is to keep these recurring concerns out of the concrete clustering algorithm. An implementation can
therefore focus on *when* and *how* its model changes, while ``ClusterInfrastructure`` standardizes *how clusters are represented,
managed, and queried* inside the task.


ClusterAnalyzer: adaptive stream-task integration
-------------------------------------------------

``ClusterAnalyzer`` combines ``OAStreamTask`` and ``ClusterInfrastructure``. It is the common adaptive template for online
clustering in an ``OAStreamWorkflow``.

A concrete analyzer supplies the algorithm-specific adaptation behavior for newly arriving and obsolete instances. The inherited
infrastructure provides the cluster model and cluster operations, while ``OAStreamTask`` contributes the common OA lifecycle,
execution model, adaptivity switch, workflow integration, and event-driven interaction with other stream tasks.

``ClusterAnalyzer`` additionally integrates cluster visualization and renormalization. If an upstream adaptive normalizer changes
its parameters, the maintained cluster model can be renormalized so that its geometric representation remains consistent with the
new coordinate system.

The resulting responsibility split can be summarized as::

    consumer / downstream component
                |
                v
         ClusterActions
        common query API
                ^
                |
    ClusterInfrastructure
    common cluster mechanics
                ^
                |
         ClusterAnalyzer
    OAStreamTask integration
                ^
                |
      concrete algorithm
    _adapt() / _adapt_reverse()

``ClusterAnalyzer`` therefore does not solve the clustering problem by itself. It defines the standardized environment in which
application-specific or third-party online clustering algorithms can be implemented consistently.


Benchmarking with native BF-Streams
-----------------------------------

The native stream pool in MLPro-BF provides reproducible benchmark inputs for developing and evaluating online cluster analyzers.
Of particular importance are the :ref:`Random Cluster and Multi-Cluster Benchmark Streams <target_bf_streams_generators>`.
They can generate known static or dynamic cluster structures in configurable dimensionality and with reproducible random seeds.

This creates a useful separation between **benchmark definition** and **analyzer implementation**: BF-Streams defines controlled
input scenarios, while OA-Streams standardizes how an online cluster analyzer represents, updates, and exposes its cluster model.
A custom ``ClusterAnalyzer`` can therefore be tested repeatedly against the same benchmark stream and compared with alternative
implementations under equivalent conditions.

Single-cluster scenarios are useful for validating basic model behavior, membership semantics, and adaptation to movement or size
changes. Multi-cluster scenarios are especially relevant for evaluating separation, competing memberships and influences,
cluster limits, and the response of an analyzer to evolving cluster configurations.


Cluster model and properties
----------------------------

Clusters are first-class objects rather than anonymous labels. The cluster-analysis package defines a reusable cluster model with
``Cluster``, cluster identifiers, centroid- and body-oriented specializations, and extensible cluster properties.

Algorithms declare the properties they maintain through ``C_CLUSTER_PROPERTIES``. New clusters can receive those definitions,
and property settings can be aligned with external consumers. The native property pool includes reusable concepts around cluster
centroids and bodies as well as derived properties such as **density** and **deformation index**.

Because the property mechanism builds on the generic BF-Math property abstractions, cluster metadata can be extended without
changing the common ``ClusterActions`` API or the fundamental analyzer lifecycle.


Forward and reverse adaptation
------------------------------

For streaming use cases, clustering must handle both directions of change:

**Forward adaptation**
    A newly arriving instance can change memberships, move or reshape existing clusters, or cause a new cluster to appear.

**Reverse adaptation**
    An obsolete instance can require the cluster model to undo part of its previous influence. This is especially relevant when
    the active data context is bounded by a window.

Algorithms that support both directions can therefore represent the structure of the *currently relevant* stream context rather
than only accumulating history forever.


Interoperability
----------------

Custom cluster analyzers built on the MLPro-OA templates can be placed after adaptive preprocessing and before change detectors
in one ``OAStreamWorkflow``. Downstream functionality that only needs cluster memberships, influences, or direct access to the
current cluster model can program against ``ClusterActions`` instead of depending on a concrete analyzer class.

A typical architecture is::

    Stream -> adaptive preprocessing -> ClusterAnalyzer -> cluster-based consumer
                                      |                 |
                                      |                 +-> ClusterActions API
                                      +-> cluster model / properties

This makes clustering a reusable adaptive model inside a larger processing chain while keeping the actual clustering algorithm
replaceable. Cluster-based change detection is still under development and should therefore be regarded as an evolving
integration area rather than mature ready-to-use functionality.


**Cross reference**

- :ref:`BF-Streams: Native Benchmark Streams <target_bf_streams_native_streams_pool>`
- :ref:`BF-Streams: Random Cluster and Multi-Cluster Benchmark Streams <target_bf_streams_generators>`
- :ref:`OA-Streams Overview <target_oa_stream_overview>`
- :ref:`Change Detection <target_oa_change_detection>`
- :ref:`BF-Math: Mathematics and properties <target_bf_mathematics>`
- :ref:`API reference: MLPro-OA-Streams - Cluster analysis <target_api_oa_stream_tasks_clu>`
