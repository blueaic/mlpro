.. _target_bf_control_scenario_cascade:

Cascade control system
----------------------

``CascadeControlSystem`` composes several nested control loops. Controllers and controlled systems are supplied in matching
lists, ordered from the outer to the inner loop. For every pair, MLPro creates a dedicated ``ControlWorkflow``.

The outer controller output is converted from ``ControlVariable`` to ``SetPoint`` and handed to the next inner workflow. After the
inner loop has executed, its ``ControlledVariable`` is converted back into a ``ControlVariable`` for the surrounding workflow.
This explicit conversion keeps the semantics of each control-data type clear across cascade boundaries.

The cascade shares timing information across all nested workflows. In particular, the shortest participating latency is
propagated through ``ControlShared`` so that differently paced controlled systems can be coordinated within one control scenario.

.. image::
    images/03_cascade_control_system.drawio.png
    :scale: 50%

The executable :ref:`Howto BF-CONTROL-003 <Howto BF CONTROL 003>` demonstrates how controllers and controlled systems are combined
into a cascaded configuration.


**Cross Reference**

- :ref:`Howto BF-CONTROL-003: Cascade control system <Howto BF CONTROL 003>`
- :ref:`Control scenarios <target_bf_control_scenarios>`
- :ref:`Operators <target_bf_control_pool_operators>`
- :ref:`BF-Control overview <target_bf_control>`
