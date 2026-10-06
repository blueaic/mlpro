## -------------------------------------------------------------------------------------------------
## -- Project : MLPro - The integrative middleware framework for standardized machine learning
## -- Package : mlpro.oa.streams.tasks.clusteranalyzers
## -- Module  : basics.py
## -------------------------------------------------------------------------------------------------
## -- History :
## -- yyyy-mm-dd  Ver.      Auth.    Description
## -- 2023-01-24  0.0.0     DA       Creation
## -- 2023-04-18  0.1.0     DA       First implementation of classes ClusterMembership, ClusterAnalyzer
## -- 2023-05-06  0.2.0     DA       New class ClusterCentroid
## -- 2023-05-14  0.3.0     DA       Class ClusterAnalyzer: simplification
## -- 2023-05-30  0.3.1     DA       Further comments, docstrings
## -- 2023-06-03  0.4.0     DA       Method ClusterAnalyzer.get_cluster_memberships():
## --                                - renaming
## --                                - new parameter p_scope
## --                                - refactoring
## --                                New Method ClusterAnalyzer.new_cluster_allowed()
## -- 2023-11-18  0.5.0     DA       Class ClusterCentroid: added plot functionality
## -- 2023-12-08  0.6.0     DA       Class ClusterAnalyzer: 
## --                                - changed internal cluster storage from list to dictionary
## --                                - added method _remove_cluster()
## -- 2023-12-10  0.6.1     DA       Bugfix in method ClusterAnalyzer.get_cluster_membership()
## -- 2023-12-20  0.7.0     DA       Renormalization
## -- 2024-02-23  0.8.0     DA       Class ClusterCentroid: implementation of methods _remove_plot*
## -- 2024-02-24  0.8.1     DA       Method ClusterAnalyzer._remove_cluster() explicitely removes
## --                                the plot of a cluster before removal of the cluster itself
## -- 2024-02-24  0.8.2     DA       Class ClusterCentroid: redefined method remove_plot()
## -- 2024-04-10  0.8.3     DA       Refactoring
## -- 2024-05-04  0.9.0     DA       Introduction of cluster properties
## -- 2024-05-27  1.0.0     DA       Initial design finished
## -- 2024-05-28  1.0.1     DA       Bugfix in ClusterAnalyzer.new_cluster_allowed()
## -- 2024-06-05  1.0.2     DA       Bugfix in ClusterAnalyzer.get_cluster_membership()
## -- 2024-06-06  1.1.0     DA       New method ClusterAnalyzer._get_next_cluster_id()
## -- 2024-06-08  1.2.0     DA       Refactoring class ClusterAnalyzer: 
## --                                - renamed attributes C_MS_SCOPE_* to C_RESULT_SCOPE_*
## --                                - new method _get_cluster_relations()
## --                                - new method get_cluster_influences()
## -- 2024-06-16  1.2.1     DA       Bugfix in ClusterAnalyzer.align_cluster_properties()
## -- 2024-08-20  1.3.0     DA       Raising of events Cluster.C_CLUSTER_ADDED, Cluster.C_CLUSTER_REMOVED
## -- 2024-08-21  1.3.1     DA       Resolved name collision of class mlpro.bf.events.Event
## -- 2025-04-13  1.4.0     DA       Refactoring of ClusterAnalyzer:
## --                                - provision of current clusters as public attribute clusters
## --                                - removed the get_clusters() method
## --                                - renamed the _get_next_cell_id() method to _get_next_cluster_id()
## -- 2025-04-24  1.5.0     DA       Added method _get_clusters() since needed for wrappers(!!)
## -- 2025-04-27  1.5.1     DA       Class ClusterAnalyzer: changed internal access to clusters to 
## --                                self.clusters 
## -- 2025-06-06  1.6.0     DA       Refactoring: p_inst -> p_instances
## -- 2025-08-20  1.7.0     DA       Method ClusterAnalyzer._get_cluster_relations: 
## --                                new parameter p_relative_values
## -- 2025-09-03  1.8.0     DA       Class ClusterAnalyzer: 
## --                                - Bugfix: added missing parameter p_thrs_cluster_influence
## --                                - Method _get_cluster_relations(): robustness for negative influences
## -- 2026-08-05  1.9.0     DA       New classes ClusterActions, ClusterInfrastructure
## -- 2026-10-06  2.0.0     DA       Refactoring and extension
## -------------------------------------------------------------------------------------------------

"""
Ver. 2.0.0 (2026-10-06)

This module provides a template class for online cluster analysis.
"""


from typing import List, Tuple
from abc import ABC, abstractmethod

from mlpro.bf.various import *
from mlpro.bf.plot import *
from mlpro.bf.events import *
from mlpro.bf.math.properties import *
from mlpro.bf.streams import Instance, InstDict
from mlpro.bf.ml import EventModeML

from mlpro.oa.streams import OAStreamTask
from mlpro.bf.math.normalizers import Normalizer
from mlpro.oa.streams.tasks.clusteranalyzers.clusters import Cluster, ClusterId



# Export list for public API
__all__ = [ 'ResultItem',
            'ClusterActions',
            'EventConfigCA',
            'ClusterAnalyzer',
            'ClusterInfrastructure',
            'ClusterAnalyzerExt' ]



ResultItem = Tuple[ClusterId, float, object]



## -------------------------------------------------------------------------------------------------
## -------------------------------------------------------------------------------------------------
class ClusterActions (ABC): 
    """
    Abstract interface for cluster collections and cluster-relation queries.

    The class provides the common clusters container and defines the public interface for evaluating
    membership and influence of instances with respect to the currently managed clusters. It does
    not prescribe how clusters are created, updated, removed, or stored beyond the public cluster
    dictionary.
    """

    # Possible result scopes for methods get_cluster_memberships() and get_cluster_influences()
    C_RESULT_SCOPE_ALL : int        = 0
    C_RESULT_SCOPE_MAX : int        = 1

## -------------------------------------------------------------------------------------------------
    def __init__( self ):
        self.clusters = {}


## -------------------------------------------------------------------------------------------------
    @abstractmethod
    def get_cluster_memberships( self, 
                                 p_instance : Instance,
                                 p_scope : int = C_RESULT_SCOPE_MAX ) -> List[ResultItem]: 
        """
        Determines the relative memberships of an instance with respect to the managed clusters.

        The cluster-specific membership measure is provided by Cluster.get_membership() or an
        equivalent implementation of the cluster interface.

        Parameters
        ----------
        p_instance : Instance
            Instance to be evaluated.
        p_scope : int
            Scope of the result. Use C_RESULT_SCOPE_ALL for all clusters or C_RESULT_SCOPE_MAX for
            the cluster with the highest membership.

        Returns
        -------
        List[ResultItem]
            Membership results as tuples of cluster id, relative membership in [0,1], and the
            corresponding cluster object.
        """

        ...


## -------------------------------------------------------------------------------------------------
    @abstractmethod
    def get_cluster_influences( self, 
                                p_instance : Instance,
                                p_scope : int = C_RESULT_SCOPE_MAX ) -> List[ResultItem]: 
        """
        Determines the relative influences of the managed clusters on an instance.

        The cluster-specific influence measure is provided by Cluster.get_influence() or an
        equivalent implementation of the cluster interface.

        Parameters
        ----------
        p_instance : Instance
            Instance to be evaluated.
        p_scope : int
            Scope of the result. Use C_RESULT_SCOPE_ALL for all clusters or C_RESULT_SCOPE_MAX for
            the cluster with the highest influence.

        Returns
        -------
        List[ResultItem]
            Influence results as tuples of cluster id, relative influence in [0,1], and the
            corresponding cluster object.
        """

        ...





## -------------------------------------------------------------------------------------------------
## -------------------------------------------------------------------------------------------------
@dataclass
class EventConfigCA (EventConfig):
    """
    Event configuration for cluster analyzers.

    The configuration extends the generic event configuration by switches for changes of the cluster
    population. Both cluster-specific events are disabled by default and can be enabled independently
    from outside the analyzer.

    Attributes
    ----------
    CLUSTER_ADDED : EventModeML
        Event mode for notifications about newly added clusters.
    CLUSTER_REMOVED : EventModeML
        Event mode for notifications about removed clusters.
    """

    CLUSTER_ADDED   : EventModeML = EventModeML.OFF
    CLUSTER_REMOVED : EventModeML = EventModeML.OFF





## -------------------------------------------------------------------------------------------------
## -------------------------------------------------------------------------------------------------
class ClusterAnalyzer (OAStreamTask, ClusterActions):
    """
    Lightweight base class for online cluster analysis.

    ClusterAnalyzer combines the execution semantics of OAStreamTask with the abstract cluster
    interface defined by ClusterActions. It intentionally does not prescribe a concrete cluster
    implementation or cluster-management infrastructure. Specialized analyzers can therefore provide
    their own high-performance cluster representation and storage while reusing the standard OA
    stream-task, event, plotting, and adaptation mechanisms.

    Parameters
    ----------
    p_name : str
        Optional task name. Default is None.
    p_range_max
        Maximum range of asynchronicity. Default is OAStreamTask.C_RANGE_THREAD.
    p_ada : bool
        Enables or disables adaptivity. Default is True.
    p_duplicate_data : bool
        If True, incoming instances are duplicated before processing. Default is False.
    p_event_config : EventConfigCA
        Event configuration used by the analyzer. Default is EventConfigCA().
    p_visualize : bool
        Enables or disables visualization. Default is False.
    p_logging
        Log level according to class Log. Default is Log.C_LOG_ALL.
    **p_kwargs
        Further optional keyword arguments forwarded to the underlying OA stream task.
    """

    C_TYPE                          = 'Cluster Analyzer'

    C_EVENT_CLUSTER_ADDED           = 'CLUSTER_ADDED'
    C_EVENT_CLUSTER_REMOVED         = 'CLUSTER_REMOVED'

    C_PLOT_ACTIVE                   = True
    C_PLOT_STANDALONE               = False

## -------------------------------------------------------------------------------------------------
    def __init__( self, 
                  p_name: str = None, 
                  p_range_max = OAStreamTask.C_RANGE_THREAD, 
                  p_ada: bool = True, 
                  p_duplicate_data: bool = False, 
                  p_event_config : EventConfigCA = EventConfigCA(),
                  p_visualize: bool = False, 
                  p_logging = Log.C_LOG_ALL, 
                  **p_kwargs ):
        
        OAStreamTask.__init__( self,
                               p_name = p_name, 
                               p_range_max = p_range_max, 
                               p_ada = p_ada, 
                               p_duplicate_data = p_duplicate_data, 
                               p_event_config = p_event_config,
                               p_visualize = p_visualize, 
                               p_logging = p_logging, 
                               **p_kwargs )

        ClusterActions.__init__( self )


## -------------------------------------------------------------------------------------------------
    def _run(self, p_instances : InstDict):
        """
        Processes a batch of stream instances by forwarding it to the adaptive model.

        Parameters
        ----------
        p_instances : InstDict
            Dictionary of stream instances to be processed.
        """

        self.adapt( p_instances = p_instances )


## -------------------------------------------------------------------------------------------------
    def init_plot(self, p_figure: Figure = None, p_plot_settings: PlotSettings = None):
        """
        Initializes the analyzer plot and propagates plot initialization to all current clusters.

        Parameters
        ----------
        p_figure : Figure
            Optional matplotlib figure.
        p_plot_settings : PlotSettings
            Optional plot settings.
        """

        if not self.get_visualization(): return

        super().init_plot( p_figure=p_figure, p_plot_settings=p_plot_settings)

        for cluster in self.clusters.values():
            cluster.init_plot(p_figure=p_figure, p_plot_settings = p_plot_settings)


## -------------------------------------------------------------------------------------------------
    def update_plot( self, 
                     p_instances : InstDict = None, 
                     **p_kwargs ):
        """
        Updates the visualization of all current clusters.

        Parameters
        ----------
        p_instances : InstDict
            Optional stream instances related to the current update.
        **p_kwargs
            Further plot-specific keyword arguments forwarded to the clusters.
        """

        if not self.get_visualization(): return

        for cluster in self.clusters.values():
            cluster.update_plot( p_instances = p_instances, **p_kwargs)


## -------------------------------------------------------------------------------------------------
    def remove_plot(self, p_refresh:bool = True):
        """
        Removes the plots of all current clusters.

        Parameters
        ----------
        p_refresh : bool
            If True, requests a display refresh after plot removal. Default is True.
        """

        if not self.get_visualization(): return

        for cluster in self.clusters.values():
            cluster.remove_plot( p_refresh = False)

        
## -------------------------------------------------------------------------------------------------
    def _renormalize(self, p_normalizer: Normalizer):
        """
        Renormalizes all current clusters with the supplied normalizer.

        This hook is used by the OA task's event-driven renormalization mechanism.

        Parameters
        ----------
        p_normalizer : Normalizer
            Normalizer to be applied to all clusters.
        """

        for cluster in self.clusters.values():
            cluster.renormalize( p_normalizer=p_normalizer )





## -------------------------------------------------------------------------------------------------
## -------------------------------------------------------------------------------------------------
class ClusterInfrastructure (ClusterActions):   
    """
    Reusable cluster-management infrastructure for cluster analyzers.

    This mixin implements cluster creation limits, cluster identifiers, cluster storage, and the
    evaluation of membership and influence relations. It contains no task or stream-task semantics
    of its own and is intended to be combined with ClusterAnalyzer or another compatible host class.

    Parameters
    ----------
    p_cls_cluster : type
        Cluster class used by the infrastructure. Default is Cluster.
    p_cluster_limit : int
        Maximum number of clusters. A value of 0 disables the limit. Default is 0.
    p_thrs_cluster_influence : float
        Optional lower threshold for cluster influence clipping. Default is None.

    Attributes
    ----------
    C_CLUSTER_PROPERTIES : PropertyDefinitions
        Property definitions maintained by the standard MLPro cluster infrastructure.
    C_EPSILON_CI : float
        Small offset used when shifting non-positive influence values.
    """

    # List of cluster properties supported/maintained by the algorithm
    C_CLUSTER_PROPERTIES : PropertyDefinitions = []

    # Small value for cluster influence computation (CI). See method _get_cluster_relations().
    C_EPSILON_CI                    = 1e-6  

## -------------------------------------------------------------------------------------------------
    def __init__( self, 
                  p_cls_cluster : type = Cluster,
                  p_cluster_limit : int = 0,
                  p_thrs_cluster_influence : float = None ):

        ClusterActions.__init__( self )

        self._next_cluster_id : ClusterId = -1

        self._cls_cluster                 = p_cls_cluster
        self._cluster_limit               = p_cluster_limit
        self._thrs_cluster_influence      = p_thrs_cluster_influence

        self._cluster_properties          = {}
        for prop in self.C_CLUSTER_PROPERTIES:
            self._cluster_properties[prop[0]] = prop


## -------------------------------------------------------------------------------------------------
    def align_cluster_properties( self, p_properties : PropertyDefinitions ) -> list:
        """
        Aligns list of cluster properties with the given list. In particular, the maximum derivative
        order of numeric properties is aligned. 

        Parameters
        ----------
        p_properties : PropertyDefinitions
            List of properties to be aligned with.

        Returns
        list
            List of unknown properties.
        """

        unknown_properties = []

        for p_ext in p_properties:
            try:
                p_int = self._cluster_properties[p_ext[0]]

                # If the property is basically provided it is aligned with external settings
                self._cluster_properties[p_ext[0]] = p_ext
            except:
                # Property not supported by cluster algorithm
                unknown_properties.append(p_ext[0])

        return unknown_properties


## -------------------------------------------------------------------------------------------------
    def new_cluster_allowed(self) -> bool:
        """
        Checks whether another cluster may be added.

        Returns
        -------
        bool
            True if the configured cluster limit has not been reached or no limit is active.
        """

        return ( self._cluster_limit == 0 ) or ( len(self.clusters.keys()) < self._cluster_limit )
    

## -------------------------------------------------------------------------------------------------
    def get_cluster_cls(self):
        """
        Returns the cluster class configured for this infrastructure.

        Returns
        -------
        type
            Configured cluster class.
        """

        return self._cls_cluster
    

## -------------------------------------------------------------------------------------------------
    def _get_next_cluster_id(self) -> ClusterId:
        """
        Generates the next cluster identifier.

        Returns
        -------
        ClusterId
            Next monotonically increasing cluster id.
        """

        self._next_cluster_id += 1
        return self._next_cluster_id
    

## -------------------------------------------------------------------------------------------------
    def _add_cluster(self, p_cluster:Cluster) -> bool:
        """
        Adds a cluster to the managed cluster collection.

        Algorithms should call new_cluster_allowed() before invoking this method.

        Parameters
        ----------
        p_cluster : Cluster
            Cluster object to be added.
        """

        self.clusters[p_cluster.id] = p_cluster

        if self.get_visualization(): 
            p_cluster.init_plot( p_figure=self._figure, p_plot_settings=self.get_plot_settings() )


## -------------------------------------------------------------------------------------------------
    def _remove_cluster(self, p_cluster:Cluster):
        """
        Removes a cluster from the managed cluster collection.

        Parameters
        ----------
        p_cluster : Cluster
            Cluster object to be removed.
        """

        p_cluster.remove_plot(p_refresh=True)
        del self.clusters[p_cluster.id]


## -------------------------------------------------------------------------------------------------
    def _get_cluster_relations( self, 
                                p_relation_type : int,
                                p_instance : Instance,
                                p_relative_values : bool ,
                                p_scope : int ) -> List[ResultItem]:
        """
        Evaluates one cluster relation for the given instance across the managed clusters.

        Relation type 0 evaluates membership, while type 1 evaluates influence. Influence values can
        optionally be clipped by p_thrs_cluster_influence. If relative values are requested, the
        absolute relation values are normalized over the selected result scope.

        Parameters
        ----------
        p_relation_type : int
            Relation type: 0 for membership or 1 for influence.
        p_instance : Instance
            Instance to be evaluated.
        p_relative_values : bool
            If True, normalizes the resulting relation values.
        p_scope : int
            Result scope, typically C_RESULT_SCOPE_ALL or C_RESULT_SCOPE_MAX.

        Returns
        -------
        List[ResultItem]
            Evaluated cluster relations for the requested scope.
        """

        # 1 Determination of membership values of the instance for all clusters
        min_abs             = None
        list_results_abs    = []
        list_results_rel    = []
        cluster_max_results = None

        for cluster in self.clusters.values():

            if p_relation_type == 0:
                result_abs  = cluster.get_membership( p_instance = p_instance )
            else:
                result_abs  = cluster.get_influence( p_instance = p_instance )
                if ( self._thrs_cluster_influence is not None ) and ( result_abs < self._thrs_cluster_influence ):
                    # Cluster influence clipping (CIC)
                    continue

            min_abs = result_abs if min_abs is None else min(min_abs, result_abs)

            if p_scope == self.C_RESULT_SCOPE_MAX:
                # Cluster with highest membership value is buffered
                if ( cluster_max_results is None ) or ( result_abs > cluster_max_results[1] ):
                    cluster_max_results = ( cluster, result_abs )
            else:
                list_results_abs.append( (cluster, result_abs) )


        # 2 Option: Maximum value only?
        if cluster_max_results is not None:
            if p_relative_values:
                return [ ( cluster_max_results[0].id, 1.0, cluster_max_results[0] ) ]
            else:
                return [ cluster_max_results ]


        # 3 Value shift on negative influence values
        if ( min_abs is not None ) and ( min_abs <= 0 ):
            min_abs -= self.C_EPSILON_CI
            for i in range(len(list_results_abs)):
                list_results_abs[i] = (list_results_abs[i][0], list_results_abs[i][1] - min_abs)


        # 4 Option: Absolute values only?
        if not p_relative_values:
            return list_results_abs


        # 5 Determination of relative result values according to the required scope
        for result_abs in list_results_abs:
            sum_results += result_abs[1]


        for result_abs in list_results_abs:
            try:
                result_rel = result_abs[1] / sum_results
            except ZeroDivisionError:
                result_rel = 0

            list_results_rel.append( ( result_abs[0].id, result_rel, result_abs[0] ) )

        return list_results_rel
        

## -------------------------------------------------------------------------------------------------
    def get_cluster_memberships( self, 
                                 p_instance : Instance,
                                 p_scope : int = ClusterActions.C_RESULT_SCOPE_MAX ) -> List[ResultItem]:
        """
        Determines relative cluster memberships for the given instance.

        Parameters
        ----------
        p_instance : Instance
            Instance to be evaluated.
        p_scope : int
            Result scope. Default is C_RESULT_SCOPE_MAX.

        Returns
        -------
        List[ResultItem]
            Membership results as tuples of cluster id, relative membership, and cluster object.
        """

        return self._get_cluster_relations( p_relation_type = 0,
                                            p_instance = p_instance,
                                            p_relative_values = True,
                                            p_scope = p_scope )
    

## -------------------------------------------------------------------------------------------------
    def get_cluster_influences( self, 
                                p_instance : Instance,
                                p_scope : int = ClusterActions.C_RESULT_SCOPE_MAX ) -> List[ResultItem]:
        """
        Determines relative cluster influences for the given instance.

        Parameters
        ----------
        p_instance : Instance
            Instance to be evaluated.
        p_scope : int
            Result scope. Default is C_RESULT_SCOPE_MAX.

        Returns
        -------
        List[ResultItem]
            Influence results as tuples of cluster id, relative influence, and cluster object.
        """

        return self._get_cluster_relations( p_relation_type = 1,
                                            p_instance = p_instance,
                                            p_relative_values = True,
                                            p_scope = p_scope )

        



## -------------------------------------------------------------------------------------------------
## -------------------------------------------------------------------------------------------------
class ClusterAnalyzerExt (ClusterAnalyzer, ClusterInfrastructure):
    """
    Extended MLPro cluster analyzer with the standard cluster infrastructure.

    This convenience class combines the lightweight ClusterAnalyzer task layer with
    ClusterInfrastructure. It represents the standard MLPro implementation for analyzers that use
    MLPro cluster objects and the generic cluster-property infrastructure.

    Parameters
    ----------
    p_name : str
        Optional task name. Default is None.
    p_range_max
        Maximum range of asynchronicity. Default is OAStreamTask.C_RANGE_PROCESS.
    p_ada : bool
        Enables or disables adaptivity. Default is True.
    p_duplicate_data : bool
        If True, incoming instances are duplicated before processing. Default is False.
    p_cls_cluster : type
        Cluster class used by the infrastructure. Default is Cluster.
    p_cluster_limit : int
        Maximum number of clusters. A value of 0 disables the limit. Default is 0.
    p_thrs_cluster_influence : float
        Optional threshold for cluster influence clipping. Default is None.
    p_visualize : bool
        Enables or disables visualization. Default is False.
    p_logging
        Log level according to class Log. Default is Log.C_LOG_ALL.
    **p_kwargs
        Further optional keyword arguments forwarded to ClusterAnalyzer.
    """

    C_TYPE  = 'Cluster Analyzer (Ext)'

## -------------------------------------------------------------------------------------------------
    def __init__( self, 
                  p_name: str = None, 
                  p_range_max = OAStreamTask.C_RANGE_PROCESS, 
                  p_ada: bool = True, 
                  p_duplicate_data: bool = False, 
                  p_cls_cluster : type = Cluster,
                  p_cluster_limit : int = 0,
                  p_thrs_cluster_influence : float = None,
                  p_visualize: bool = False, 
                  p_logging = Log.C_LOG_ALL, 
                  **p_kwargs ):
        
        ClusterAnalyzer.__init__( self,
                                  p_name = p_name, 
                                  p_range_max = p_range_max, 
                                  p_ada = p_ada, 
                                  p_duplicate_data = p_duplicate_data, 
                                  p_visualize = p_visualize, 
                                  p_logging = p_logging, 
                                  **p_kwargs )

        ClusterInfrastructure.__init__( self, 
                                        p_cls_cluster = p_cls_cluster,
                                        p_cluster_limit = p_cluster_limit,
                                        p_thrs_cluster_influence = p_thrs_cluster_influence )