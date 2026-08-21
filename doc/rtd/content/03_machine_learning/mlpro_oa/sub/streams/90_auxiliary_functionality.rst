.. _target_oa_auxiliary_functionality:

Auxiliary Functionality
=======================

MLPro-OA-Streams includes supporting functionality that complements the main processing areas without defining a separate
primary processing domain. These components help to summarize, inspect, and observe adaptive stream-processing workflows.

The current auxiliary functionality comprises:

**Online statistics**
    Incremental statistical tasks such as ``MovingAverage`` summarize the active stream context and can participate in the same
    forward/reverse adaptation and renormalization mechanisms as other OA stream tasks.

**Observation and helpers**
    Observer and helper classes make adaptation, cluster evolution, and detected changes visible without becoming part of the
    processing logic itself.


.. toctree::
   :maxdepth: 1

   40_statistics
   99_helpers


**Cross reference**

- :ref:`OA-Streams Overview <target_oa_stream_overview>`
- :ref:`Howtos OA-Streams <target_appendix1_OA_streams>`
- :ref:`API reference: MLPro-OA-Streams <target_api_oa_streams>`
