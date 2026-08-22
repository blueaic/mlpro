.. _target_bf_streams_native_streams_pool:

Native Benchmark Streams
========================

Along with third-party stream support, MLPro provides a pool of native stream objects that can be used directly in applications and experiments. A central purpose of this pool is to provide **reproducible benchmark streams** for validating stream-processing and machine-learning functionality under controlled conditions.

The native streams cover several characteristic data situations, including file-based input, high-dimensional random data, structured geometric patterns, injected point outliers, and synthetic cluster structures. Depending on the stream, parameters such as dimensionality, random seed, number of instances, boundaries, outlier rate, cluster geometry, and temporal cluster behavior can be controlled explicitly.

This makes the pool useful not only for demonstrations but also for repeatable comparisons between algorithms and processing pipelines. In particular, the cluster and multi-cluster generators are designed to support benchmark scenarios for :ref:`Online Cluster Analysis <target_oa_cluster_analysis>` in MLPro-OA-Streams.

.. toctree::
   :maxdepth: 2
   :glob:

   native_streams/*


**Cross Reference**
   - :ref:`Howto BF-STREAMS-001: Accessing Native Data From MLPro <Howto_BF_STREAMS_001>`
   - :ref:`Online Cluster Analysis <target_oa_cluster_analysis>`
   - :ref:`API Reference: Streams <target_ap_bf_streams>`
