.. _target_oa_stream_statistics:

Online Statistics
=================

Overview
--------

Online statistics provide compact, continuously updated descriptions of the active stream context. In MLPro-OA they are
implemented as regular ``OAStreamTask`` objects so they can react to new and obsolete instances, participate in adaptive
workflows, and remain consistent when upstream normalization changes.


MovingAverage
-------------

The current native statistics task is ``MovingAverage``. It incrementally updates a moving average for incoming feature vectors
and can optionally remove the contribution of obsolete instances. This makes it particularly suitable behind a sliding window or
another processing stage that emits ``InstTypeDel`` entries.

For every processed batch, ``MovingAverage`` replaces the incoming instance set with a single new instance containing the
current average. The task therefore acts both as a statistic and as a stream transformation that can feed later workflow stages.

Key framework features include:

- incremental updates for new instances;
- optional reverse updates for obsolete instances;
- 2D, 3D, and nD visualization;
- a crosshair property for the current average in 2D/3D views;
- renormalization of the internally stored average after an upstream adaptive normalizer changes its parameters;
- optional renormalization of existing plot data.

A typical use is::

    Stream -> Window / BoundaryDetector -> Adaptive Normalizer -> MovingAverage -> Observer / later task

The observation howto demonstrates this pattern in an executable adaptive workflow.


**Cross reference**

- :ref:`Howto OA-OBS-001: Observing an adaptive stream workflow <Howto_OA_OBS_001>`
- :ref:`Howtos OA-Streams <target_appendix1_OA_streams>`
- :ref:`Adaptive Preprocessing <target_oa_stream_preprocessing>`
- :ref:`Observation and Helpers <target_oa_helpers>`
- :ref:`OA-Streams Overview <target_oa_stream_overview>`
- :ref:`API reference: MLPro-OA-Streams <target_api_oa_streams>`
