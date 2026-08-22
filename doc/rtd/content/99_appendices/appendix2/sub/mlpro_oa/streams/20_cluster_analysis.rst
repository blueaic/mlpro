.. _target_api_oa_stream_tasks_clu:
Cluster analysis
================

The cluster-analysis API is organized in three layers: ``ClusterActions`` defines the common consumer-facing cluster API,
``ClusterInfrastructure`` provides reusable internal cluster-management functionality, and ``ClusterAnalyzer`` combines this
infrastructure with ``OAStreamTask`` for online-adaptive stream processing.

.. image:: 20_cluster_analysis/images/MLPro-OA-Cluster_Analyzers_class_diagram.drawio.png
   :scale: 50%
   
   
.. automodule:: mlpro.oa.streams.tasks.clusteranalyzers.basics
   :members:
   :undoc-members:
   :private-members:
   :show-inheritance:


.. automodule:: mlpro.oa.streams.tasks.clusteranalyzers.clusters.basics
   :members:
   :undoc-members:
   :private-members:
   :show-inheritance:


.. automodule:: mlpro.oa.streams.tasks.clusteranalyzers.clusters.centroid
   :members:
   :undoc-members:
   :private-members:
   :show-inheritance:


.. automodule:: mlpro.oa.streams.tasks.clusteranalyzers.clusters.body
   :members:
   :undoc-members:
   :private-members:
   :show-inheritance: