.. _Howto BF SYSTEMS 010:

Howto BF-SYSTEMS-010: System, SAGateway, Actuator, Sensor
========================================================

This How-To demonstrates the real-system interface of BF-Systems. It implements a custom ``SAGateway`` with two sensors and two
actuators, maps them to a custom system's state and action dimensions, switches the system to real mode, and processes an action.

**Executable code**

.. literalinclude:: ../../../../../../../../../test/howtos/bf/systems/howto_bf_systems_010_systems_controllers_actuators_sensors.py
   :language: python


**What to observe**

The example shows the complete hardware abstraction path: sensor values are imported through the gateway into the system state,
while action values are mapped to actuators and exported through the same gateway. The custom gateway methods simulate the actual
device communication and can be replaced by a concrete hardware adapter.


**Cross Reference**

- :ref:`Hardware access <target_bf_systems_hardware>`
- :ref:`State-based systems <target_bf_systems>`
- :ref:`API Reference: Systems <target_ap_bf_systems>`
