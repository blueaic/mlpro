.. _target_oa_helpers:

Observation and Helpers
=======================

Overview
--------

Adaptive stream processing is event-rich: models adapt, boundaries change, clusters appear or disappear, and detectors raise
change events. MLPro-OA provides helper classes that observe these events without becoming part of the processing logic itself.

The helpers build on the BF-Streams helper infrastructure and can therefore be attached to tasks for logging, statistics, and
visualization while keeping the actual workflow unchanged.


OAObserver
----------

``OAObserver`` observes ``OAStreamTask.C_EVENT_ADAPTED`` events of a selected adaptive task. It records adaptation statistics by
subtype and counts how many stream instances were involved in each adaptation.

The observer distinguishes the stream-specific adaptation types:

- forward adaptation,
- reverse adaptation,
- event-triggered adaptation,
- renormalization.

Individual subtypes can be filtered. In visualization mode the observer places adaptations on a time axis and can use a
logarithmic scale for the number of affected instances. This makes adaptation behavior visible without adding instrumentation to
the adaptive algorithm itself.


Change observers
----------------

The helper package also contains generic and cluster-oriented change observers. Their purpose is to consume ``Change`` events
raised by change detectors and present the detected transitions together with the processing context.

This separation follows an important OA design principle::

    processing task -> event -> observer / application handler

The task remains responsible for processing and detection; observation remains optional and replaceable.


Cluster-analysis observation
----------------------------

``CAObserver`` adds observation facilities for online cluster analysis. It can react to cluster-related events and visualize how
the cluster model evolves while the stream is processed. This is particularly useful when evaluating online clustering and
cluster-based anomaly/drift detection, where the structural model itself changes over time.


End-to-end observation
----------------------

The OA-Streams observation How-To demonstrates a workflow combining boundary detection, adaptive MinMax normalization, moving
average statistics, and an observer. It is a useful reference for understanding how adaptive processing and event observation
fit together in one executable scenario.

- :ref:`OA-OBS-001: Observing an adaptive stream workflow <Howto_OA_OBS_001>`


**Cross reference**

- :ref:`OA-Streams Overview <target_oa_stream_overview>`
- :ref:`Change Detection <target_oa_change_detection>`
- :ref:`Online Cluster Analysis <target_oa_cluster_analysis>`
- :ref:`OA-Streams How-Tos <target_appendix1_OA_streams>`
- :ref:`API reference: MLPro-OA-Streams <target_api_oa_streams>`
