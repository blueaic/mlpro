.. _target_oa_anomaly_detection:

Anomaly Detection
=================

Overview
--------

Anomaly detection is a specialization of :ref:`Change Detection <target_oa_change_detection>`. It identifies unusual behavior
in an evolving stream and represents it as explicit ``Anomaly`` objects and events while reusing the common
``Change``/``ChangeDetector`` architecture.

In its current state, MLPro-OA mainly provides the **standardized anomaly model and detector templates**. ``AnomalyDetector``
derives from ``ChangeDetector`` and inherits bounded change buffering, event handling, optional visualization, delayed activation
through an instance threshold, and the common change lifecycle. The public ``anomalies`` collection is an alias of the underlying
change buffer.

Concrete anomaly-detection logic is generally supplied by specialized child classes or extensions. The framework standardizes
how detected anomalies are represented, buffered, visualized, and emitted rather than claiming to provide one universal anomaly
algorithm.


Anomaly objects
---------------

The OA anomaly model distinguishes different structural meanings instead of reducing every deviation to one generic flag.
Instance-oriented anomaly objects include:

- **Point anomalies** for individual unusual observations.
- **Group anomalies** for a sequence or collection whose combined behavior is unusual.
- **Contextual anomalies** for observations that are unusual only in a particular context.

Cluster-oriented anomaly objects describe changes in an adaptive cluster model. The framework model includes anomaly types for
new-cluster appearance, disappearance, enlargement, shrinkage, deformation, density changes, and point/group effects around
clusters.

All anomaly types share the ``Change`` event semantics, which means downstream handlers can react consistently to specialized
anomaly classes.


.. _target_oa_ibad:

Instance-based anomaly detection
--------------------------------

Instance-based detectors work directly on stream observations or model outputs associated with individual observations. The
common template is ``AnomalyDetectorIB``.

``AnomalyDetectorIBPG`` extends this concept with optional group-anomaly formation. Consecutive point anomalies can be combined
into a group anomaly, allowing a detector to represent a persistent unusual episode rather than emitting an unrelated sequence
of point events.

This layer is intentionally algorithm-neutral: concrete detectors decide *why* an instance is anomalous, while OA-Streams
standardizes *how* the anomaly is represented, buffered, visualized, and emitted.


.. _target_oa_cbad:

Cluster-based anomaly detection
-------------------------------

Cluster-based anomaly detection is part of the **cluster-based change-detection area that is currently under development**. It is
designed to operate on the structural model maintained by an online :ref:`Cluster Analyzer <target_oa_cluster_analysis>` and to
express anomalies derived from changes in cluster geometry, density, population, or existence.

The architectural foundations and corresponding anomaly objects/templates are already present, but this area should not yet be
regarded as mature ready-to-use functionality. A custom cluster algorithm can expose the standardized cluster model and
properties, while specialized detector implementations can build on the common change/anomaly semantics.

Conceptually::

    instances -> ClusterAnalyzer -> cluster state/properties -> cluster-based AnomalyDetector

The clustering algorithm and the anomaly semantics remain decoupled through the standardized interfaces.


Anomaly lifecycle and triage
----------------------------

Anomalies can be buffered automatically. ``AnomalyDetector`` also provides a triage hook that lets specialized detectors decide
whether an existing anomaly should remain in the active history or be discarded during cleanup.

Because anomaly objects inherit the status semantics of ``Change``, algorithms may represent both the beginning and the end of
an anomalous condition where appropriate. Event consumers can register for the corresponding on/off event ids.


Use in adaptive workflows
-------------------------

Anomaly detectors are ordinary OA stream tasks and can therefore be inserted into an ``OAStreamWorkflow``. A detector may
observe raw/preprocessed instances, follow an adaptive model, or, for cluster-based approaches, consume an online cluster model.
An emitted anomaly event can then trigger observation, logging, model adaptation, or application-specific action without
coupling that reaction to the detector itself.

The active OA-Streams howto tree currently contains no dedicated anomaly-detection script. This page therefore serves as the
functional entry point, while class and method details are available in the API reference.


**Cross reference**

- :ref:`Change Detection <target_oa_change_detection>`
- :ref:`Online Cluster Analysis <target_oa_cluster_analysis>`
- :ref:`Observation and Helpers <target_oa_helpers>`
- :ref:`API reference: MLPro-OA-Streams - Anomaly detection <target_api_oa_stream_tasks_ad>`
