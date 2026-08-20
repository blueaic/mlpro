.. _target_bf_streams_tasks_rearranger:

Rearranger
==========

A stream task often needs only part of the incoming data or needs the same dimensions in a different arrangement. The **Rearranger** transforms the feature and label spaces of incoming instances without introducing a source-specific processing step.

It can:

* select a subset of features or labels,
* change their order,
* move dimensions from feature data to label data,
* move dimensions from label data to feature data.

The mapping is described through ``p_features_new`` and ``p_labels_new``. Each entry specifies whether the source dimension comes from the feature space (``'F'``) or label space (``'L'``), followed by the Dimension objects that shall appear in the new space.

Conceptually:

``[F1, F2, F3] + [L1] -> Rearranger -> [F3, F1, L1] + [F2]``

The resulting feature and label spaces are prepared from the first incoming instance. Afterwards the task replaces the feature/label Elements of each processed Instance according to the configured mapping.

This makes Rearranger useful as a lightweight feature-selection and schema-transformation step before downstream algorithms. Because it remains a normal StreamTask, it can be inserted anywhere in a StreamWorkflow and combined with windows, derivation, online learning, or custom tasks.


**Cross Reference**
    + :ref:`Howto BF-STREAMS-121: Rearranger (2D) <Howto BF STREAMS 121>`
    + :ref:`Howto BF-STREAMS-122: Rearranger (3D) <Howto BF STREAMS 122>`
    + :ref:`Howto BF-STREAMS-123: Rearranger (nD) <Howto BF STREAMS 123>`
    + :ref:`API Reference: Streams <target_ap_bf_streams>`
