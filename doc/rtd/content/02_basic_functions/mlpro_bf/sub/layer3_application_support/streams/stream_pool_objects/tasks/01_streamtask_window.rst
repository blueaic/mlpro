.. _target_bf_streams_tasks_window:

Window and Ring Buffer
======================

A stream may be endless, but many processing algorithms only need a finite representation of the most recent data. MLPro separates the general **Window** abstraction from its concrete sliding-window implementation **RingBuffer**.

The RingBuffer keeps at most ``p_buffer_size`` active instances. As soon as the buffer is full and a new instance arrives, the oldest one is removed and forwarded as ``InstTypeDel`` while the new one is forwarded as ``InstTypeNew``:

``new sample -> buffer full? -> oldest '-' + newest '+'``

This is an important DSP pattern because downstream tasks receive both changes explicitly and can update their own state consistently.

.. image::
    images/window.png
    :width: 800 px

A typical task is configured like this:

.. code-block:: python

    from mlpro.bf.streams.tasks.windows import RingBuffer

    window = RingBuffer(
        p_buffer_size=50,
        p_delay=True,
        p_enable_statistics=True,
        p_name='Recent samples'
    )

**Delayed forwarding.** With ``p_delay=False`` new instances are forwarded immediately while the buffer is still filling. With ``p_delay=True`` no instances are forwarded until the first complete window is available; the initial buffer content is then emitted together.

**Statistics.** Window provides mean, variance, and standard deviation over buffered data. RingBuffer can additionally maintain numeric feature boundaries through the common ``BoundaryProvider`` interface from MLPro-BF-MATH. Statistics are enabled through ``p_enable_statistics`` and are also activated when visualization requires them.

**Visualization.** RingBuffer specializes the standard StreamTask plotting behavior and can visualize the active window in 2D, 3D, and nD views. This makes the same object useful as both processing state and an inspectable view of the currently active data.


**Cross Reference**
    + :ref:`Howto BF-STREAMS-111: Ring Buffer / Window (2D) <Howto BF STREAMS 111>`
    + :ref:`Howto BF-STREAMS-112: Ring Buffer / Window (3D) <Howto BF STREAMS 112>`
    + :ref:`Howto BF-STREAMS-113: Ring Buffer / Window (nD) <Howto BF STREAMS 113>`
    + :ref:`Statistics and Boundaries <target_bf_math_statistics>`
    + :ref:`API Reference: Streams <target_ap_bf_streams>`
