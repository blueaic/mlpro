.. _target_bf_systems_hardware:

Hardware access
===============

MLPro-BF-Systems uses the same ``System`` abstraction for simulated and real systems. In real operation, sensor values and
actuator commands are connected to the system through a **sensor/actuator gateway** (``SAGateway``).

.. image::
    images/hardware_access.drawio.png
    :width: 400 px

The hardware-facing objects are intentionally small and composable:

**Sensor**
    A ``Sensor`` is a specialization of :class:`Dimension`. It describes one observable quantity exposed by a gateway. Sensor
    dimensions can be mapped to dimensions of the system's state space.

**Actuator**
    An ``Actuator`` is likewise a specialization of :class:`Dimension`. It describes one externally writable quantity and can
    be mapped to a dimension of the system's action space.

**SAGateway**
    ``SAGateway`` is the communication boundary between MLPro and concrete hardware. A custom gateway implements
    ``_get_sensor_value()``, ``_set_actuator_value()``, and ``_reset()``. The base class manages registered sensors and actuators
    and raises ``COMM_ERROR`` events if reading, writing, or resetting fails.

A system can register one or more gateways and define mappings between state/action dimensions and sensor/actuator dimensions.
This keeps the system model independent from the communication technology used underneath: field bus, device API, network
service, laboratory hardware, or another adapter can all be hidden behind the same gateway interface.

A typical integration follows this flow::

    sensor -> SAGateway -> State -> System
    actuator <- SAGateway <- Action <- System

The executable :ref:`Howto BF-SYSTEMS-010 <Howto BF SYSTEMS 010>` demonstrates a custom two-sensor/two-actuator gateway,
registers it on a custom system, switches the system to real mode, and processes an action through the mapping.


**Cross reference**

- :ref:`State-based systems <target_bf_systems>`
- :ref:`Howto BF-SYSTEMS-010: System, SAGateway, Actuator, Sensor <Howto BF SYSTEMS 010>`
- :ref:`API reference BF-Systems <target_ap_bf_systems>`
