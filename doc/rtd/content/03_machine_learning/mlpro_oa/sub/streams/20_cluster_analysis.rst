.. _target_oa_cluster_analysis:

Online Cluster Analysis
=======================

Overview
--------

Online cluster analysis continuously maintains a structural description of a data stream while new observations arrive and old
observations may disappear from the active context. In its current development stage, MLPro-OA primarily provides the
**standardized framework and templates for implementing custom online cluster analyzers** rather than a broad collection of
ready-to-use clustering algorithms.

The cluster-analysis architecture is deliberately split into a lightweight core and optional standard MLPro infrastructure. This
allows high-performance implementations to reuse the common clustering contract without depending on MLPro's generic property
model.

Four classes are central:

- ``ClusterActions`` defines the common public API for access to a current cluster model.
- ``ClusterAnalyzer`` combines this contract with ``OAStreamTask`` and provides the lightweight online-adaptive task layer.
- ``ClusterInfrastructure`` provides reusable standard MLPro mechanics for cluster storage, ids, limits, properties, memberships,
  influences, and cluster lifecycle operations.
- ``ClusterAnalyzerExt`` combines ``ClusterAnalyzer`` and ``ClusterInfrastructure`` and therefore represents the convenient
  standard MLPro implementation.

This separation is intentional. Specialized analyzers may derive directly from ``ClusterAnalyzer`` and provide their own cluster
representation and management, while conventional MLPro implementations can use ``ClusterAnalyzerExt`` and the generic property
infrastructure.


ClusterActions: common cluster-analysis API
-------------------------------------------

``ClusterActions`` is the smallest common contract of the cluster-analysis stack. It exposes the current ``clusters`` collection
and standardizes queries that relate an ``Instance`` to that cluster model.

The two principal operations are:

- ``get_cluster_memberships()`` for relative membership values;
- ``get_cluster_influences()`` for relative influence values.

Both operations use the common ``ResultItem`` representation consisting of a cluster id, a result value, and the corresponding
cluster object. Result scopes allow callers either to inspect all applicable clusters or to request only the strongest result.

For integrations, this class is the preferred API boundary whenever a consumer needs cluster information without requiring the
full adaptive task interface.


ClusterAnalyzer: lightweight adaptive task layer
------------------------------------------------

``ClusterAnalyzer`` combines ``OAStreamTask`` and ``ClusterActions``. It deliberately does **not** prescribe how clusters are
implemented, stored, created, or removed.

A specialized analyzer can therefore reuse MLPro-OA's stream-task lifecycle, adaptivity, event handling, visualization hooks,
workflow integration, and forward/reverse adaptation while implementing its own cluster-management strategy. This is particularly
important for high-performance implementations where the generic MLPro property infrastructure would introduce unnecessary
runtime overhead.

``ClusterAnalyzer`` forwards incoming stream data to the adaptive model and integrates cluster visualization and renormalization
at task level. The concrete cluster implementation remains responsible for supporting the corresponding operations.


ClusterInfrastructure: reusable standard MLPro mechanics
--------------------------------------------------------

``ClusterInfrastructure`` is a task-independent mixin that implements the standard MLPro mechanics behind conventional cluster
analyzers. It derives from ``ClusterActions`` but does not itself introduce ``Task``, ``StreamTask``, or ``OAStreamTask`` semantics.

Its responsibilities include:

- storage of the current clusters and generation of cluster ids;
- checking limits before new clusters are created;
- protected operations for adding and removing clusters;
- declaration and alignment of cluster properties through ``C_CLUSTER_PROPERTIES``;
- common computation of cluster memberships and influences;
- result scopes and optional influence thresholds;
- access to the configured cluster class.

The infrastructure can therefore be combined with a compatible task layer where these generic mechanisms are desired, but it is
not mandatory for every cluster analyzer.


ClusterAnalyzerExt: standard MLPro combination
----------------------------------------------

``ClusterAnalyzerExt`` combines the lightweight ``ClusterAnalyzer`` with ``ClusterInfrastructure``. It is the convenient base
class for conventional MLPro cluster analyzers that use the standard cluster model and property infrastructure.

The responsibility split can be summarized as::

    consumer / downstream component
                |
                v
         ClusterActions
        common query API
           ^         ^
           |         |
           |   ClusterInfrastructure
           |   standard MLPro mechanics
           |         ^
           |         |
       ClusterAnalyzer
       OA task layer
           ^         ^
           |         |
 specialized      ClusterAnalyzerExt
 high-speed       standard MLPro stack
 analyzer

This structure keeps the core clustering contract reusable while preserving the richer MLPro implementation as an optional layer.


Event configuration
-------------------

Cluster analyzers use ``EventConfigCA`` as their specific event configuration. It extends the generic MLPro event configuration by
the two cluster-lifecycle events ``CLUSTER_ADDED`` and ``CLUSTER_REMOVED``. Both are disabled by default and can be enabled
individually by the embedding application.

The event configuration belongs to the analyzer layer and can be extended by specialized implementations with additional
domain-specific events.


Cluster model
-------------

The cluster model follows the same lightweight-versus-rich separation.

``ClusterBase`` is the minimal abstract cluster representation. It provides cluster identity, optional plot support, and the two
generic relation operations ``get_membership()`` and ``get_influence()``. It is deliberately independent of MLPro's generic
``Properties`` model.

``Cluster`` extends ``ClusterBase`` with ``Properties`` and ``KWArgs`` and remains the standard MLPro cluster template. Further
specializations such as ``ClusterCentroid`` and ``ClusterBody`` build on this richer model.

This gives specialized high-performance analyzers a clean option to derive directly from ``ClusterBase`` while conventional MLPro
algorithms can continue to use the property-based ``Cluster`` hierarchy.

Benchmarking with native BF-Streams
-----------------------------------

The native stream pool in MLPro-BF provides reproducible benchmark inputs for developing and evaluating online cluster analyzers.
Of particular importance are the :ref:`Random Cluster and Multi-Cluster Benchmark Streams <target_bf_streams_generators>`.
They can generate known static or dynamic cluster structures in configurable dimensionality and with reproducible random seeds.

This creates a useful separation between **benchmark definition** and **analyzer implementation**: BF-Streams defines controlled
input scenarios, while OA-Streams standardizes how an online cluster analyzer represents, updates, and exposes its cluster model.
A custom cluster analyzer can therefore be tested repeatedly against the same benchmark stream and compared with alternative
implementations under equivalent conditions.

Single-cluster scenarios are useful for validating basic model behavior, membership semantics, and adaptation to movement or size
changes. Multi-cluster scenarios are especially relevant for evaluating separation, competing memberships and influences,
cluster limits, and the response of an analyzer to evolving cluster configurations.

A few representative benchmark scenarios are shown below. The complete visual benchmark gallery is available in
:ref:`BF-Streams <target_bf_streams_generators>`.

.. list-table::
   :widths: 25 25 25 25

   * - :ref:`Single / dynamic 2D <Howto BF STREAMS CLUSTER 003>`

       .. image:: ../../../../99_appendices/appendix1/sub/mlpro_bf/layer3_application_support/streams/images/howto_bf_streams_cluster_003.gif
          :width: 140 px
          :alt: Dynamic single-cluster 2D benchmark
     - :ref:`Multi / static 2D <Howto BF STREAMS MULTICLUSTER 002>`

       .. image:: ../../../../99_appendices/appendix1/sub/mlpro_bf/layer3_application_support/streams/images/howto_bf_streams_multicluster_002.gif
          :width: 140 px
          :alt: Static multi-cluster 2D benchmark
     - :ref:`Multi / crossing 2D <Howto BF STREAMS MULTICLUSTER 004>`

       .. image:: ../../../../99_appendices/appendix1/sub/mlpro_bf/layer3_application_support/streams/images/howto_bf_streams_multicluster_004.gif
          :width: 140 px
          :alt: Crossing multi-cluster 2D benchmark
     - :ref:`Multi / crossing 3D + outliers <Howto BF STREAMS MULTICLUSTER 010>`

       .. image:: ../../../../99_appendices/appendix1/sub/mlpro_bf/layer3_application_support/streams/images/howto_bf_streams_multicluster_010.gif
          :width: 140 px
          :alt: Crossing multi-cluster 3D benchmark with rescaled outliers


Cluster model and properties
----------------------------

The standard MLPro cluster hierarchy remains property-based. Algorithms using ``ClusterInfrastructure`` can declare the
properties they maintain through ``C_CLUSTER_PROPERTIES``. New clusters can receive those definitions, and property settings
can be aligned with external consumers. The native property pool includes reusable concepts around cluster centroids and bodies
as well as derived properties such as **density** and **deformation index**.

This property layer is optional: lightweight implementations can derive their cluster objects directly from ``ClusterBase``
without carrying the generic property machinery.

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

    Stream -> adaptive preprocessing -> ClusterAnalyzer-based task -> cluster-based consumer
                                      |                      |
                                      |                      +-> ClusterActions API
                                      +-> lightweight or standard cluster model

This makes clustering a reusable adaptive model inside a larger processing chain while keeping both the clustering algorithm and
its internal cluster representation replaceable. Cluster-based change detection is still under development and should therefore
be regarded as an evolving integration area rather than mature ready-to-use functionality.

**Cross reference**

- :ref:`BF-Streams: Native Benchmark Streams <target_bf_streams_native_streams_pool>`
- :ref:`BF-Streams: Random Cluster and Multi-Cluster Benchmark Streams <target_bf_streams_generators>`
- :ref:`OA-Streams Overview <target_oa_stream_overview>`
- :ref:`Change Detection <target_oa_change_detection>`
- :ref:`BF-Math: Mathematics and properties <target_bf_mathematics>`
- :ref:`API reference: MLPro-OA-Streams - Cluster analysis <target_api_oa_stream_tasks_clu>`
