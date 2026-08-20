.. _target_bf_streams_3rd_party_support:

Third-Party Stream Integration
==============================

MLPro's DSP architecture is intentionally independent of the original data source. Once an external source is exposed as an MLPro **Stream**, downstream StreamTasks and StreamWorkflows can process it without source-specific logic.

There are two common integration patterns:

* implement a **Stream** when one concrete sequential source shall be consumed directly,
* implement a **StreamProvider** when an integration shall discover and expose several related streams through a common lookup interface.

The important boundary is the Instance object. An integration converts source-specific records into MLPro Instances with feature data, optional label data, ids/time stamps, and metadata. The feature and label spaces use the normal MLPro mathematical Dimension/Space abstractions. Everything behind that boundary may remain specific to the external library, protocol, file format, or live system.

Conceptually:

``external source -> Stream / StreamProvider -> Instance -> StreamWorkflow``

This adapter pattern is used by approved MLPro integration projects, for example:

* `MLPro-Int-OpenML - Integration of OpenML into MLPro <https://mlpro-int-openml.readthedocs.io>`_
* `MLPro-Int-scikit-learn - Integration of scikit-learn into MLPro <https://mlpro-int-scikit-learn.readthedocs.io>`_
* `MLPro-Int-River - Integration of River into MLPro <https://mlpro-int-river.readthedocs.io>`_

The same pattern can be applied to industrial live sources. A custom Stream can translate incoming sensor or message data into Instances while the surrounding DSP workflow remains unchanged. If the external system exposes multiple signals, machines, topics, or datasets, a StreamProvider can add discovery and selection on top.

A complete list of approved MLPro extensions can be found in the :ref:`MLPro Extension Hub <target_extension_hub>`.


**Cross reference**
    + :ref:`Stream Handling <target_bf_streams_handling>`
    + :ref:`Stream Processing <target_bf_streams_processing>`
    + :ref:`API Reference: Streams <target_ap_bf_streams>`
