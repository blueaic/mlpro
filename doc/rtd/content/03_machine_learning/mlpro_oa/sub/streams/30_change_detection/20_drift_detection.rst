.. _target_oa_drift_detection:

Drift Detection
===============

Overview
--------

Drift detection addresses persistent changes of the underlying data-generating process. In MLPro-OA it shares the same generic
``Change``/``ChangeDetector`` architecture as anomaly detection, so drift events can be handled by the same event-oriented
workflow mechanisms while retaining drift-specific semantics.

``DriftDetector`` derives from ``ChangeDetector`` and exposes its buffered changes through the public ``drifts`` collection. It
provides dedicated methods for buffering, removing, and raising ``Drift`` objects and a drift-specific triage hook for cleanup.

A drift event can describe both the beginning and the end of a drift, which is useful for long-running streams where a changed
regime may persist over many instances.


Drift versus anomaly
--------------------

An anomaly usually describes an unusual observation, group, or structural event. Drift describes a change in the process itself.
The distinction is semantic rather than infrastructural: both are specialized ``Change`` objects and both are emitted by
specialized ``ChangeDetector`` tasks.

This shared model allows a workflow to treat anomaly and drift detection uniformly at the event level while using different
algorithms and reaction policies.


.. _target_oa_ibdd:

Instance-based drift detection
------------------------------

Instance-based drift detection derives evidence directly from the arriving observations or statistics calculated from them. The
source architecture provides a dedicated instance-based detector layer beneath the common ``DriftDetector`` template.

Typical implementations can compare recent observations or statistics with an earlier reference state and raise a drift when a
persistent distributional change is detected. OA-Streams supplies the event, buffering, timestamp, status, and lifecycle
semantics; the concrete statistical criterion remains algorithm-specific.


.. _target_oa_cbdd:

Cluster-based drift detection
-----------------------------

Cluster-based drift detection observes the evolving structural description produced by an online cluster analyzer. Changes in
cluster positions, geometry, density, membership, relations, appearance, or disappearance can provide evidence of a changing
data-generating process.

Because :ref:`Online Cluster Analysis <target_oa_cluster_analysis>` exposes clusters and their properties through standardized
objects, drift detection can be decoupled from a particular clustering algorithm. The source tree provides a dedicated
cluster-based drift-detector layer for this purpose.

A representative pipeline is::

    Stream -> adaptive preprocessing -> ClusterAnalyzer -> DriftDetector
                                      |                  |
                                      | cluster model    +-> Drift(ON/OFF) events
                                      v
                              cluster properties


Drift lifecycle
---------------

``DriftDetector`` reuses the bounded change history of ``ChangeDetector``. Newly raised drift objects receive ids and timestamps
through the common change-event mechanism and can optionally be buffered. The drift-specific triage hook can decide whether
older drift objects remain relevant during detector cleanup.

Downstream components do not need to poll the detector. They can register handlers for the corresponding drift event ids and
react when a drift begins or ends.


Use in OA workflows
-------------------

A drift detector can be connected to observation, model adaptation, or application-specific logic through events. This enables
architectures in which detection and reaction remain separate, for example a drift event that switches a model into a stronger
adaptation mode or triggers reinitialization of selected pipeline stages.

The active OA-Streams How-To tree currently contains no dedicated drift-detection script. Concrete APIs and available detector
classes are documented in the API reference.


**Cross reference**

- :ref:`Change Detection <target_oa_change_detection>`
- :ref:`Online Cluster Analysis <target_oa_cluster_analysis>`
- :ref:`Observation and Helpers <target_oa_helpers>`
- :ref:`API reference: MLPro-OA-Streams - Drift detection <target_api_oa_stream_tasks_dd>`
