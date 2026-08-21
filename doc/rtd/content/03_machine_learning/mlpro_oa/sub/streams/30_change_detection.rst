.. _target_oa_change_detection:

Change Detection
================

Overview
--------

**Change detection is the common framework-level domain for detecting relevant changes in an evolving stream.** MLPro-OA
standardizes this through ``Change`` and ``ChangeDetector``. **Anomaly detection** and **drift detection** are specialized forms
of change detection and reuse the same lifecycle, buffering, visualization, and event semantics.

In the current development stage, this area is primarily a **template and standardization framework**. MLPro-OA defines how
changes and detectors are represented and integrated, but it does not yet provide a broad collection of ready-to-use change
detection algorithms. Concrete detection logic is generally implemented in specialized child classes or extensions.

A detected change is not represented only by a Boolean flag. ``Change`` combines identity, timestamp, status, event behavior,
visualization, and renormalization. This gives downstream components enough context to react to the beginning and end of a
change and allows detectors to participate directly in MLPro's event system.

The conceptual hierarchy is::

    Change Detection
        |
        +-- Anomaly Detection
        |      +-- instance-based
        |      +-- cluster-based
        |
        +-- Drift Detection
               +-- instance-based
               +-- cluster-based

Cluster-based change detection is currently under development. The corresponding data models, abstractions, and integration
paths are being established, but this part should not yet be understood as mature ready-to-use functionality.


The Change object
-----------------

A ``Change`` has a unique id and a public ``status``. A status of ``True`` marks the beginning of a change; ``False`` marks its
end. Event ids are derived from the concrete change type and its status, for example as ``<ChangeType>(ON)`` and
``<ChangeType>(OFF)``. Consumers can therefore register handlers for the exact change transitions they are interested in.

``ChangeDetector`` provides the common detector lifecycle, buffers recent change objects, assigns ids, controls execution after
a configurable number of instances, and integrates visualization and event raising.

This common contract lets different custom detection algorithms be exchanged while observers and downstream handlers continue
to work with the same event semantics.


Anomaly detection
-----------------

Anomaly detection specializes change detection for unusual observations, groups, contexts, or structural effects. MLPro-OA
provides the corresponding anomaly objects and detector templates for both **instance-based** and **cluster-based** approaches.

Instance-based anomalies describe deviations associated with individual observations or groups of observations. The framework
model includes point, group, and contextual variants.

Cluster-based anomalies describe changes in the evolving cluster structure, for example appearance, disappearance, enlargement,
shrinkage, deformation, density changes, and point/group effects around clusters. This cluster-based branch is still under
development.

See :ref:`Anomaly Detection <target_oa_anomaly_detection>` for the specialized framework objects and detector templates.


Drift detection
---------------

Drift detection specializes change detection for persistent changes of the underlying data-generating process. MLPro-OA defines
common drift abstractions and separate template layers for instance-based and cluster-based approaches.

The important framework-level distinction is that anomaly and drift detectors share the same ``Change``/``ChangeDetector``
contract. Their results can therefore be observed and processed uniformly even though their concrete algorithms and temporal
semantics are different. Cluster-based drift detection is part of the same ongoing development area as cluster-based change
detection in general.

See :ref:`Drift Detection <target_oa_drift_detection>` for the specialized drift lifecycle and detector templates.


.. toctree::
   :maxdepth: 1

   30_change_detection/10_anomaly_detection
   30_change_detection/20_drift_detection


Event-driven processing
-----------------------

Change detection becomes especially powerful as part of an ``OAStreamWorkflow``::

    Stream -> preprocessing -> adaptive model / cluster analysis -> ChangeDetector
                                                            |
                                                            v
                                                     Change event
                                                            |
                                +---------------------------+------------------+
                                |                           |                  |
                             observer                  model adaptation    application logic

This keeps detection separate from reaction. A detector identifies and describes a change; registered handlers decide whether
to visualize it, adapt another model, raise an alarm, or trigger application-specific behavior.


Observation and history
-----------------------

Detectors can keep a bounded history in ``changes``. OA helper classes complement this by observing emitted change events and
presenting them together with the processing workflow. See :ref:`Observation and Helpers <target_oa_helpers>`.


**Cross reference**

- :ref:`Anomaly Detection <target_oa_anomaly_detection>`
- :ref:`Drift Detection <target_oa_drift_detection>`
- :ref:`Online Cluster Analysis <target_oa_cluster_analysis>`
- :ref:`Observation and Helpers <target_oa_helpers>`
- :ref:`OA-Streams Overview <target_oa_stream_overview>`
- :ref:`API reference: MLPro-OA-Streams <target_api_oa_streams>`
