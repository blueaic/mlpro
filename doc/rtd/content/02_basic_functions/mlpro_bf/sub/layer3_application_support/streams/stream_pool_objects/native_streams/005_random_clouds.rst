.. _target_bf_streams_generators:

Random Cluster and Multi-Cluster Benchmark Streams
-------------------------------------------------

MLPro-BF provides a generator framework for producing synthetic data streams in a configurable, d-dimensional feature space.
The current implementation replaces the former random-cloud generators with a more structured generator architecture based on
``StreamGenerator`` and ``MultiStreamGenerator``.

The generic ``StreamGenerator`` template provides the common mechanics for generated streams, including reproducible random
number generation, configurable feature dimensions, optional rescaling of feature boundaries, optional outlier generation, and
regular MLPro stream/sampler integration. Concrete generators derive from this template and implement the actual data-generation
logic.

For cluster-shaped data, the active generator stack is located below
``mlpro.bf.streams.streams.generators.multiclusters`` and provides two central abstractions:

- ``StreamGenCluster`` generates a single cluster of random points. A cluster can remain static or change its center and radii
  over time. Multiple cluster states and transition steps describe this temporal behavior.
- ``MultiStreamGenCluster`` combines several cluster generators and therefore supports synthetic multi-cluster streams with
  independently configurable cluster behavior.

These generators have an explicit **benchmark character**. They make the underlying cluster structure controllable and repeatable,
so that clustering algorithms can be evaluated against known synthetic scenarios rather than opaque real-world data. Static
configurations are useful for checking basic cluster identification and memberships, while dynamic configurations can challenge
an analyzer with moving, growing, shrinking, appearing, or otherwise changing cluster structures.

This is particularly relevant for :ref:`Online Cluster Analysis <target_oa_cluster_analysis>` in MLPro-OA-Streams. The
multi-cluster streams provide standardized input scenarios for developing, debugging, demonstrating, and comparing custom
``ClusterAnalyzer`` implementations. Because MLPro-OA standardizes the analyzer API and cluster handling while leaving the actual
clustering algorithm open, reproducible BF-Streams benchmarks form a natural counterpart to that architecture.

The same benchmark streams can also support downstream experiments in cluster-based anomaly and drift detection as these areas
mature.

The former module ``mlpro.bf.streams.streams.clouds`` is deprecated and is no longer part of the active stream API. Existing
applications that still use the legacy cloud generators should migrate to the generator classes described above.


**Cross reference**

- :ref:`Online Cluster Analysis <target_oa_cluster_analysis>`
- :ref:`Howto BF-STREAMS-CLUSTER-001: One Static Random 2D Cluster <Howto BF STREAMS CLUSTER 001>`
- :ref:`Howto BF-STREAMS-CLUSTER-002 <Howto BF STREAMS CLUSTER 002>`
- :ref:`Howto BF-STREAMS-CLUSTER-003 <Howto BF STREAMS CLUSTER 003>`
- :ref:`Howto BF-STREAMS-CLUSTER-004 <Howto BF STREAMS CLUSTER 004>`
- :ref:`Howto BF-STREAMS-CLUSTER-005 <Howto BF STREAMS CLUSTER 005>`
- :ref:`Howto BF-STREAMS-CLUSTER-006: One Static Random 3D Cluster <Howto BF STREAMS CLUSTER 006>`
- :ref:`Howto BF-STREAMS-CLUSTER-007 <Howto BF STREAMS CLUSTER 007>`
- :ref:`Howto BF-STREAMS-CLUSTER-008 <Howto BF STREAMS CLUSTER 008>`
- :ref:`Howto BF-STREAMS-MULTICLUSTER-001: Two Static Fixed 2D Clusters <Howto BF STREAMS MULTICLUSTER 001>`
- :ref:`Howto BF-STREAMS-MULTICLUSTER-002 <Howto BF STREAMS MULTICLUSTER 002>`
- :ref:`Howto BF-STREAMS-MULTICLUSTER-003 <Howto BF STREAMS MULTICLUSTER 003>`
- :ref:`Howto BF-STREAMS-MULTICLUSTER-004 <Howto BF STREAMS MULTICLUSTER 004>`
- :ref:`Howto BF-STREAMS-MULTICLUSTER-006 <Howto BF STREAMS MULTICLUSTER 006>`
- :ref:`Howto BF-STREAMS-MULTICLUSTER-007 <Howto BF STREAMS MULTICLUSTER 007>`
- :ref:`Howto BF-STREAMS-MULTICLUSTER-008 <Howto BF STREAMS MULTICLUSTER 008>`
- :ref:`Howto BF-STREAMS-MULTICLUSTER-009 <Howto BF STREAMS MULTICLUSTER 009>`
- :ref:`Howto BF-STREAMS-MULTICLUSTER-010 <Howto BF STREAMS MULTICLUSTER 010>`
- :ref:`API reference: Streams <target_ap_bf_streams>`
