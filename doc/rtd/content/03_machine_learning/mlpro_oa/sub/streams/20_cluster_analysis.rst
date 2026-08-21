.. _target_oa_cluster_analysis:

Online Cluster Analysis
=======================

Overview
--------

Online cluster analysis continuously maintains a structural description of a data stream while new observations arrive and old
observations may disappear from the active context. In its current development stage, MLPro-OA primarily provides the
**standardized framework and templates for implementing custom online cluster analyzers** rather than a broad collection of
ready-to-use clustering algorithms.

``ClusterAnalyzer`` is the common adaptive template for this task. It is an ``OAStreamTask`` and therefore participates in the
same forward/reverse adaptation lifecycle as other OA processing tasks. A concrete clustering algorithm implements how new and
obsolete instances change the current cluster model, while the framework standardizes cluster management, events, results,
properties, visualization, and renormalization.

In other words, ``ClusterAnalyzer`` does not solve the clustering problem by itself. It defines the interoperable framework in
which application-specific or third-party online clustering algorithms can be implemented consistently.


Cluster model
-------------

Clusters are first-class objects rather than anonymous labels. The cluster-analysis package defines a reusable cluster model with
``Cluster``, cluster identifiers, centroid- and body-oriented specializations, and extensible cluster properties.

The analyzer standardizes common operations such as:

- creation and removal of clusters, including ``CLUSTER_ADDED`` and ``CLUSTER_REMOVED`` events;
- limits on the number of clusters;
- cluster memberships and cluster influences for incoming data;
- selection of all relevant results or the strongest result through result scopes;
- relations between clusters;
- synchronization of property definitions across cooperating algorithms;
- visualization and renormalization after changes in upstream preprocessing.

This separates the generic semantics of an online cluster model from the concrete clustering algorithm.


Cluster properties
------------------

A particularly important part of the design is the property system. Algorithms declare the properties they maintain through
``C_CLUSTER_PROPERTIES``. New clusters receive those definitions automatically, and property settings can be aligned with
external consumers.

The native property pool includes reusable concepts around cluster centroids and bodies as well as derived properties such as
**density** and **deformation index**. Because the property mechanism builds on the generic BF-Math property abstractions, cluster
metadata can be extended without changing the core analyzer contract.


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
in one ``OAStreamWorkflow``. Cluster creation/removal events and evolving cluster properties can also be observed by helper
classes or consumed by cluster-based anomaly and drift detectors.

A typical architecture is::

    Stream -> adaptive preprocessing -> ClusterAnalyzer -> cluster-based change detection
                                      |                 |
                                      +-> properties    +-> change events

The standardized interfaces make clustering a reusable adaptive model inside a larger event-driven processing chain, even when
the actual clustering algorithm is supplied by the application developer or a third-party extension.

Cluster-based change detection is currently under development and should therefore be regarded as an evolving integration area
rather than mature ready-to-use functionality.


**Cross reference**

- :ref:`OA-Streams Overview <target_oa_stream_overview>`
- :ref:`Change Detection <target_oa_change_detection>`
- :ref:`BF-Math: Mathematics and properties <target_bf_mathematics>`
- :ref:`API reference: MLPro-OA-Streams - Cluster analysis <target_api_oa_stream_tasks_clu>`
