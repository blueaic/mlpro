.. _target_bf_streams_processing_01:

Data Stream Processing Architecture
===================================

Processing one stream instance at a time becomes much more useful when processing steps can be reused, combined, parallelized, and kept synchronized as data enters and leaves the active state. MLPro addresses this with three levels: **StreamTask**, **StreamWorkflow**, and **StreamScenario**.

``Stream -> StreamScenario -> StreamWorkflow -> StreamTask(s)``

Stream tasks and instance flow
------------------------------

A **StreamTask** is the basic DSP processing unit. It receives an ``InstDict`` whose entries combine an instance id, an instance type, and the corresponding Instance object:

``instance_id -> ('+' | '-', Instance)``

``'+'`` denotes ``InstTypeNew`` and marks an instance that has become available. ``'-'`` denotes ``InstTypeDel`` and marks an instance that has become obsolete.

This distinction is more than bookkeeping. Stateful tasks can remove exactly the same instance that a predecessor removed. A fixed-size window, for example, emits the oldest instance as deleted when a new one enters. Downstream statistics, plots, or online algorithms can then update their state consistently instead of accumulating data that is no longer active.

A custom task usually only needs to specialize ``_run()``:

.. code-block:: python

    from mlpro.bf.streams import InstDict, InstTypeNew, StreamTask

    class MyTask(StreamTask):

        def _run(self, p_instances: InstDict):
            for inst_id, (inst_type, instance) in p_instances.items():
                if inst_type == InstTypeNew:
                    values = instance.feature_values
                    # process or modify the instance here

``StreamTask.run()`` handles integration with the shared workflow state. If ``p_duplicate_data=True`` is configured, the incoming instances are copied before processing; otherwise a task works on the objects forwarded by its predecessors.

**Shared processing state.** After a task has run, its resulting instance dictionary is stored in the workflow's **StreamShared** object under the task id. A dependent task retrieves the instance sets of its predecessor tasks from this shared object. This gives every task a well-defined input while still allowing the workflow to coordinate parallel branches.

Stream workflows
----------------

A **StreamWorkflow** combines StreamTasks through predecessor relations. It is built on MLPro-BF-MT's Workflow abstraction, so the dependency graph also determines which branches may be processed independently.

For example:

``t1 -> t2a --+``

``  \-> t2b --+-> t3``

can be configured with task objects rather than by manually moving data between functions:

.. code-block:: python

    from mlpro.bf.streams import StreamWorkflow

    workflow = StreamWorkflow(p_name='DSP Workflow')

    workflow.add_task(p_task=t1)
    workflow.add_task(p_task=t2a, p_pred_tasks=[t1])
    workflow.add_task(p_task=t2b, p_pred_tasks=[t1])
    workflow.add_task(p_task=t3, p_pred_tasks=[t2a, t2b])

When an external instance dictionary starts a new workflow cycle, the workflow resets its shared instance state and executes the tasks according to these dependencies. Tasks therefore focus on their processing function while the workflow handles routing, synchronization, and shared results.

**Range of asynchronicity.** StreamTask and StreamWorkflow inherit MLPro's multitasking concepts. Their ``p_range_max`` setting controls the permitted execution range, from synchronous execution to thread- or process-based execution where supported. DSP pipelines can therefore retain the same logical task graph while adapting execution to the application environment.

Stream scenarios
----------------

A **StreamScenario** is the orchestration layer that combines one Stream and one StreamWorkflow. Custom scenarios implement ``_setup()`` and return both objects:

.. code-block:: python

    from mlpro.bf import Mode
    from mlpro.bf.streams import StreamScenario, StreamWorkflow
    from mlpro.bf.streams.streams import StreamProviderMLPro

    class MyScenario(StreamScenario):

        def _setup(self, p_mode, p_visualize, p_logging):
            provider = StreamProviderMLPro(p_logging=p_logging)
            stream = provider.get_stream_list()[0]

            workflow = StreamWorkflow(
                p_name='My Workflow',
                p_visualize=p_visualize,
                p_logging=p_logging
            )

            return stream, workflow

During execution the scenario repeatedly performs the same cycle:

``get next Instance -> mark as new -> run StreamWorkflow -> update visualization -> next cycle``

When the stream is exhausted, the scenario detects the end of data. This makes StreamScenario the natural place to assemble reproducible DSP applications while keeping Stream and StreamTask implementations reusable in other scenarios.

**Visualization and helpers.** StreamTask and StreamWorkflow provide default 2D, 3D, and nD visualization for numeric feature data. The current stream subsystem also provides **StreamHelper** and **StreamTaskHelper** as extension points for additional task-related visualization or event-driven helper functionality without putting that logic into the processing task itself.

The complete executable architecture example is available in :ref:`Howto BF-STREAMS-102 <Howto BF STREAMS 102>`.


**Cross Reference**
    + :ref:`Howto BF-STREAMS-102: Tasks, Workflows and Stream Scenarios <Howto BF STREAMS 102>`
    + :ref:`BF-MT - Multitasking <target_bf_mt>`
    + :ref:`API Reference: Streams <target_ap_bf_streams>`
