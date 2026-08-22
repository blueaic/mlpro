.. _target_bf_streams_generators:

Random Cluster and Multi-Cluster Stream Generators
--------------------------------------------------

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

This architecture supports both compact static test streams and dynamic scenarios in which clusters move, change their size, or
are combined into more complex multi-cluster arrangements. It is intended as reusable infrastructure for testing stream
processing, visualization, clustering, change detection, and other data-driven algorithms.

The former module ``mlpro.bf.streams.streams.clouds`` is deprecated and is no longer part of the active stream API. Existing
applications that still use the legacy cloud generators should migrate to the generator classes described above.


**Cross reference**

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
