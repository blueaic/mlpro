.. _target_bf_control_pool_controllers:

Controllers
===========

``Controller`` is the BF-Control template for mapping a ``ControlError`` to a ``ControlVariable``. A custom controller implements
``_compute_output()`` and receives the current typed error object together with a newly created control-variable object that must
be filled with the resulting values.

Controllers participate directly in the control workflow as ``ControlTask`` objects. Their execution is coordinated with the
latency information held in ``ControlShared``; if the next controller update is not due yet, the most recent control variable can
be duplicated with a new id and timestamp instead of recomputing it.

``ControllerFct`` provides a specialization intended for controllers represented by mathematical ``Function`` objects.

The ready-to-use controller pool currently contains ``PIDController`` and the example ``Hunter`` controller.


**Learn more**

.. toctree::
   :maxdepth: 1
   :glob:

   controllers/*


**Cross Reference**

- :ref:`PID Controller <target_bf_control_pid>`
- :ref:`BF-Control overview <target_bf_control>`
- :ref:`Howto BF-CONTROL-101: PID Controller with PT1 system <Howto_BF_CONTROL_101>`
- :ref:`API Reference BF-Control Pool Objects <target_pool_bf_control>`
