## -------------------------------------------------------------------------------------------------
## -- Project : MLPro - The integrative middleware framework for standardized machine learning
## -- Module  : howto_bf_streams_multiclusters_012_2_clusters_static_fix_par_2d.py
## -------------------------------------------------------------------------------------------------
## -- History :
## -- yyyy-mm-dd  Ver.      Auth.    Description
## -- 2025-09-19  1.0.0     DA       Creation/First implementation
## -- 2026-08-22  1.0.1     DA       Extended module documentation
## -------------------------------------------------------------------------------------------------

"""
Ver. 1.0.1 (2026-08-22)

This module demonstrates a two-dimensional benchmark stream with two compact clusters following
controlled trajectories that cross in the center of the feature space. The crossing creates an
ambiguous structural situation and is therefore a useful benchmark for evaluating cluster identity,
separation, and tracking behavior of online cluster analyzers.

You will learn:

1) How to define deterministic trajectories for two dynamic ``StreamGenCluster`` objects.

2) How to synchronize their state transitions so that the clusters cross each other.

3) How to combine both generators in a ``MultiStreamGenCluster`` benchmark stream.

4) How to run and visualize the crossing-cluster scenario in 2D.

"""

from mlpro.bf.ops import Mode
from mlpro.bf.plot import PlotSettings
from mlpro.bf.streams import *
from mlpro.bf.streams.streams.generators.multiclusters import *
from mlpro.bf.various import Log



## -------------------------------------------------------------------------------------------------
## -------------------------------------------------------------------------------------------------
class MyScenario (StreamScenario):
    """
    Example of a custom stream scenario including a stream and a stream workflow. See class 
    mlpro.bf.streams.models.StreamScenario for further details and explanations.
    """

    C_NAME      = '2 Clusters rnd, static'

## -------------------------------------------------------------------------------------------------
    def _setup(self, p_mode, p_visualize:bool, p_logging):

        # 1 Set up MLPro's cluster generator
        stream1 = StreamGenCluster( p_num_dim = 2, 
                                    p_seed = 1,
                                    p_states = [ ClusterState( p_center = [500, 400], p_radii = [50, 50] ) ,
                                                 ClusterState( p_center = [0, 0], p_radii = [50, 50] ),
                                                 ClusterState( p_center = [-800, -500], p_radii = [50, 50] ) ],
                                    p_transition_steps = [self._cycle_limit/4]*2,
                                    p_logging = p_logging )

        stream2 = StreamGenCluster( p_num_dim = 2, 
                                    p_seed = 2,
                                    p_states = [ ClusterState( p_center = [-500, 500], p_radii = [50, 50] ) ,
                                                 ClusterState( p_center = [0, 0], p_radii = [50, 50] ),
                                                 ClusterState( p_center = [100, -500], p_radii = [50, 50] ) ],
                                    p_transition_steps = [self._cycle_limit/4]*2,
                                    p_logging = p_logging )

        mstream = MultiStreamGenCluster( p_num_dim = 2, p_num_instances = self._cycle_limit )
        mstream.add_stream( p_stream = stream1 )
        mstream.add_stream( p_stream = stream2 )


        # 2 Set up a stream workflow
        workflow = StreamWorkflow( p_name = 'wf1', 
                                   p_range_max = StreamWorkflow.C_RANGE_NONE, 
                                   p_visualize = p_visualize,
                                   p_logging = logging )


        # 3 Return stream and workflow
        return mstream, workflow





# 1 Preparation of demo/unit test mode
if __name__ == "__main__":
    # 1.1 Parameters for demo mode
    cycle_limit = 1000
    logging     = Log.C_LOG_WE
    visualize   = True
    step_rate   = 2
  
else:
    # 1.2 Parameters for internal unit test
    cycle_limit = 2
    logging     = Log.C_LOG_NOTHING
    visualize   = False
    step_rate   = 1


# 2 Instantiate the stream scenario
myscenario = MyScenario( p_mode=Mode.C_MODE_SIM,
                         p_cycle_limit=cycle_limit,
                         p_visualize=visualize,
                         p_logging=logging )


# 3 Reset and run own stream scenario
myscenario.reset()

if __name__ == '__main__':
    myscenario.init_plot( p_plot_settings=PlotSettings( p_view = PlotSettings.C_VIEW_2D,
                                                        p_view_autoselect = False,
                                                        p_step_rate = step_rate ) )
    input('Press ENTER to start stream processing...')

myscenario.run()

if __name__ == '__main__':
    input('Press ENTER to exit...')

    