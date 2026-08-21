.. _target_oa_anomaly_detection:

Anomaly Detection
=================

Overview
--------

Anomaly detection identifies unusual behavior in an evolving stream and represents it as explicit ``Anomaly`` objects and
events. In MLPro-OA, anomaly detection is a specialization of the generic :ref:`Change Detection <target_oa_change_detection>`
architecture rather than a separate runtime subsystem.

``AnomalyDetector`` derives from ``ChangeDetector``. It therefore inherits bounded change buffering, event handling, optional
visualization, delayed activation through an instance threshold, and the common change lifecycle. The public ``anomalies``
collection is an alias of the underlying change buffer.

Concrete algorithms should raise anomalies through the framework's anomaly-event methods so ids, timestamps, buffering, and
registered handlers remain consistent.

.. image:: ../../../../../99_appendices/appendix2/sub/mlpro_oa/streams/30_change_detection/10_anomaly_detection/images/MLPro-OA-Anomaly-Detectors_class_diagram.drawio.png
   :width: 90%
   :alt: Class architecture of anomaly detection in MLPro-OA


Anomaly objects
---------------

The OA anomaly model distinguishes different structural meanings instead of reducing every deviation to one generic flag.
Instance-oriented anomaly objects include:

- **Point anomalies** for individual unusual observations.
- **Group anomalies** for a sequence or collection whose combined behavior is unusual.
- **Contextual anomalies** for observations that are unusual only in a particular context.

Cluster-oriented anomaly objects describe changes in an adaptive cluster model. The current source tree contains anomaly types
for new-cluster appearance, disappearance, enlargement, shrinkage, deformation, density changes, and point/group effects around
clusters.

All anomaly types still share the ``Change`` event semantics, which means downstream handlers can react consistently to
specialized anomaly classes.


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

Cluster-based detection operates on the structural model maintained by an online
:ref:`Cluster Analyzer <target_oa_cluster_analysis>`. This enables anomalies that are not evident from a single sample alone to
be detected from changes in cluster geometry, density, population, or existence.

OA-Streams provides a cluster-based anomaly-detector foundation plus generic implementations and a point/group anomaly detector.
The detector can consume cluster information and raise specialized cluster anomaly objects when the cluster model changes.

This separation is important in adaptive pipelines::

    instances -> ClusterAnalyzer -> cluster state/properties -> cluster-based AnomalyDetector
                    |                                      |
                    +---------- adaptation events ---------+

The clustering algorithm and the anomaly semantics remain replaceable. A custom cluster algorithm can expose the standardized
cluster model and properties, while a detector can focus on the structural conditions it considers anomalous.


Anomaly lifecycle and triage
----------------------------

Anomalies can be buffered automatically. ``AnomalyDetector`` also provides a triage hook that lets specialized detectors decide
whether an existing anomaly should remain in the active history or be discarded during cleanup.

Because anomaly objects inherit the status semantics of ``Change``, algorithms may represent both the beginning and the end of
an anomalous condition where appropriate. Event consumers can register for the corresponding on/off event ids.


Use in adaptive workflows
-------------------------

Anomaly detectors are ordinary OA stream tasks and can therefore be inserted anywhere in an ``OAStreamWorkflow``. A detector may
observe raw/preprocessed instances, follow an adaptive model, or consume the output of online cluster analysis. An emitted anomaly
event can then trigger observation, logging, model adaptation, or application-specific action without coupling that reaction to
the detector itself.

The active OA-Streams How-To tree currently contains no dedicated anomaly-detection script. This page therefore serves as the
functional entry point, while concrete class and method details are available in the API reference.


**Cross reference**

- :ref:`Change Detection <target_oa_change_detection>`
- :ref:`Online Cluster Analysis <target_oa_cluster_analysis>`
- :ref:`Observation and Helpers <target_oa_helpers>`
- :ref:`API reference: MLPro-OA-Streams - Anomaly detection <target_api_oa_stream_tasks_ad>`
