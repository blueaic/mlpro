.. _target_bf_mt:

Multitasking
============

In MLPro, **multithreading** and **multiprocessing** support asynchronous execution of
independent program parts. Multithreading runs work in threads within one process,
while multiprocessing uses separate processes and requires explicit interprocess
communication for shared state.

Both approaches can improve throughput, but their performance depends on the workload
and synchronization overhead. In conventional CPython builds, the Global Interpreter
Lock (GIL) limits simultaneous execution of Python bytecode by threads; native extensions
may release it. Free-threaded Python builds have different concurrency characteristics.
Multiprocessing can execute CPU-bound Python code across multiple cores, at the cost of
additional process and data-transfer overhead.

The details of the multitasking implemented in MLPro are explained in more detail below:

**Range**

In the context of multitasking, the range describes the degree of parallelism of a program function. There are three 
different degrees:

- Synchronous/serial
- Asynchronous/parallel using multithreading
- Asynchronous/parallel using multiprocessing


**Asynchronous execution of methods**

MLPro provides the property class **Async** for asynchronous execution of callables.
Its ``_start_async()`` method executes the target synchronously or starts a new thread
or process, depending on the configured maximum range and the optional per-call range.
``wait_async_tasks()`` joins the asynchronous operations registered on the current
``Async`` instance.

``Async`` derives from ``Range`` and does not inherit from ``Log``. Its constructor
accepts ``p_range_max``, the optional shared-object class ``p_class_shared``, and
additional keyword arguments for shared-object construction. An associated shared
object can be accessed using ``get_so()`` or assigned using ``assign_so()``.

Each asynchronous call creates a new thread or process; ``Async`` does not provide a
bounded worker pool. Its task list is not synchronized for concurrent starts and waits
on the same instance. In addition, exceptions raised by worker threads are not
forwarded by ``wait_async_tasks()``. Applications must account for these limitations
when orchestrating nested or concurrent work.

**Tasks and workflows**

A fundamental and consistently used concept in MLPro is that of tasks and workflows. A task is a class that can be 
executed in one of the three possible ranges mentioned above. Tasks can in turn be grouped into workflows. 
Any **directed graphs** of tasks can be set up and processed massively parallel via corresponding predecessor 
relationships. Successor tasks are informed about the termination of their predecessors via event technology. The 
**Task** and **Workflow** classes of the same name have once again been implemented as property classes. They are 
consistently reused in higher functions through inheritance. Some examples are :ref:`Stream Processing <target_bf_streams_processing>` 
and the :ref:`Adaptive Workflows <target_bf_ml_workflows>`.

``Task`` integrates ``EventManager`` and therefore accepts the optional parameter ``p_event_config``. This provides a common configuration channel for event-capable task subclasses. Such subclasses can query ``_get_event_mode()`` before constructing an event object and thereby suppress disabled events without unnecessary object creation. The built-in ``C_EVENT_FINISHED`` event continues to coordinate predecessor/successor execution in workflows.


**Gap under MacOS**

At the time of the creation of MLPro, a technical problem related to multiprocessing occurred on Apple computers 
under MacOS. This is documented at `Race condition when using multiprocessing BaseManager and Pool in Python3 <https://github.com/python/cpython/issues/88321>`_. It is recommended to 
check MLPro functionalities in multiprocessing mode on MacOS-based computers very carefully and, if in doubt, to use 
multithreading.


**Cross reference**

- :ref:`Howto BF-MT-001: Multitasking - Parallel algorithms <Howto BF MT 001>`
- :ref:`Howto BF-MT-002: Multitasking - Tasks and workflows <Howto BF MT 002>`
- :ref:`API Reference BF-MT - Multitasking <target_api_bf_mt>`


