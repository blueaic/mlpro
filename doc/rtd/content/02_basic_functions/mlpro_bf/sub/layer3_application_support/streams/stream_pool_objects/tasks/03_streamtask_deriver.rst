.. _target_bf_streams_tasks_deriver:

Deriver
=======

The **Deriver** extends incoming stream instances with a numerical derivative of one selected feature. Instead of replacing the original signal, it adds the derived value as an additional feature dimension so downstream tasks can use both the signal and its rate of change.

A first-order example is conceptually:

``[position] -> Deriver(order=1) -> [position, position OD-1]``

The task uses the instance time stamp as its time base when available. If a physical or pseudo-time index is supplied consistently by the Stream, the derivative therefore follows the actual spacing of the samples rather than assuming that every update is equally spaced.

The selected derivative order is configured with ``p_order_derivative``. Higher-order derivatives require the corresponding amount of history; initial derivative values are therefore initialized until enough samples have been observed.

.. code-block:: python

    from mlpro.bf.streams.tasks import Deriver

    task = Deriver(
        p_derived_feature=my_feature,
        p_order_derivative=1,
        p_name='Velocity'
    )

The feature space is prepared from the first incoming instance. Deriver copies the selected feature definition, appends a suffix identifying the derivative order, and extends each processed Instance with the calculated value.

A corresponding label can optionally be supplied through ``p_derived_label`` so that the label space is extended in the same processing step.

For several derivative orders, use separate Deriver tasks in the workflow. This keeps every transformation explicit and allows each order to be routed or visualized independently.


**Cross Reference**
    + :ref:`Howto BF-STREAMS-131: Deriver <Howto BF STREAMS 131>`
    + :ref:`API Reference: Streams <target_ap_bf_streams>`
