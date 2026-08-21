.. _target_oa_stream_preprocessing:

Adaptive Preprocessing
======================

Overview
--------

Adaptive preprocessing keeps transformations aligned with a data stream whose statistical range or distribution changes over
time. In MLPro-OA-Streams this is implemented with regular ``OAStreamTask`` objects, so preprocessing can participate in the
same workflow, event, visualization, and adaptation model as all later analysis stages.

The current native preprocessing stack contains two central building blocks: ``BoundaryDetector`` and online-adaptive
normalizers.


.. _target_oa_boundary_detector:

Boundary detection
------------------

``BoundaryDetector`` combines ``OAStreamTask`` with the mathematical ``BoundaryProvider`` abstraction. It observes the feature
space of incoming instances and maintains per-dimension boundaries.

Forward and reverse adaptation have distinct roles:

- New instances may **extend** an observed boundary.
- Obsolete instances may require a boundary to be **reduced** again.
- If reduction cannot be determined from local state alone, an external ``BoundaryProvider`` can be queried, for example a
  sliding window that still contains the active data.

The detector therefore fits naturally into workflows where the valid data range itself is dynamic. Boundary changes can trigger
adaptation of downstream tasks instead of being handled by application-specific glue code.


.. _target_oa_streams_normalization:

Online-adaptive normalization
-----------------------------

``OAStreamNormalizer`` is the common template that combines a mathematical ``Normalizer`` with ``OAStreamTask``. Native
implementations currently include:

.. _target_oa_norm_minmax:

**NormalizerMinMax**
    Adapts MinMax normalization parameters to changing input boundaries and transforms incoming feature values to configurable
    destination boundaries, by default ``[-1, 1]``.

.. _target_oa_norm_ztrans:

**NormalizerZTrans**
    Provides online-adaptive Z-transformation based on the evolving statistics of the stream.

The key architectural detail is not only that normalization parameters can change. A parameter change can invalidate already
normalized data stored in plots or downstream task buffers. OA-Streams addresses this with renormalization support and adaptation
events so dependent tasks can update their internal state consistently.

A typical chain is::

    raw stream
       |
       v
    BoundaryDetector
       |
       | boundary change
       v
    NormalizerMinMax / NormalizerZTrans
       |
       | normalized stream + adaptation event
       v
    adaptive and non-adaptive downstream tasks


Hybrid preprocessing workflows
------------------------------

OA preprocessing is deliberately interoperable with :ref:`BF-Streams <target_bf_streams>`. Deterministic tasks such as
``Rearranger``, ``Window``/``RingBuffer``, or ``Deriver`` can be combined with adaptive boundary detection and normalization in
one ``OAStreamWorkflow``. This makes it possible to adapt only those stages that actually need adaptation.

The How-To collection demonstrates both compact normalizer pipelines and larger hybrid workflows in 2D, 3D, and nD.


How-Tos
-------

- :ref:`OA-PP-001: Boundary detection and MinMax normalization in 2D <Howto_OA_PP_001>`
- :ref:`OA-PP-002: Boundary detection and MinMax normalization in 3D <Howto_OA_PP_002>`
- :ref:`OA-PP-003: Boundary detection and MinMax normalization in nD <Howto_OA_PP_003>`
- :ref:`OA-PP-006: Z-transformation in 2D <Howto_OA_PP_006>`
- :ref:`OA-PP-007: Z-transformation in 3D <Howto_OA_PP_007>`
- :ref:`OA-PP-008: Z-transformation in nD <Howto_OA_PP_008>`
- :ref:`OA-PP-101: Hybrid preprocessing in 2D <Howto_OA_PP_101>`
- :ref:`OA-PP-102: Hybrid preprocessing in 3D <Howto_OA_PP_102>`
- :ref:`OA-PP-103: Hybrid preprocessing in nD <Howto_OA_PP_103>`
- :ref:`OA-PP-104: Hybrid preprocessing in 2D, 3D and nD <Howto_OA_PP_104>`
- :ref:`OA-PP-121: Complex preprocessing with parallel tasks <Howto_OA_PP_121>`


**Cross reference**

- :ref:`OA-Streams Overview <target_oa_stream_overview>`
- :ref:`BF-Streams: Stream tasks and workflows <target_bf_streams>`
- :ref:`BF-Math: Mathematics and normalizers <target_bf_mathematics>`
- :ref:`OA-Streams How-Tos <target_appendix1_OA_streams>`
- :ref:`API reference: MLPro-OA-Streams <target_api_oa_streams>`
