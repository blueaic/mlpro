.. _target_bf_math_properties:

Managed Properties
==================

Why managed properties?
-----------------------

In dynamic applications, a value is often more than just its current number. It may have a history, a time stamp, derivatives, visualization state, or it may need to be renormalized when the surrounding data representation changes.

A plain Python attribute stores the current value only. MLPro's **Property** class turns such a value into a *managed state variable* that can carry this additional behavior in a standardized way.

For example, instead of handling position, previous position, time stamps, and velocity in separate attributes, one Property can manage these aspects together.

**Core concept.** A **Property** stores a value of almost any type. Depending on its configuration, it can additionally provide:

* ``value_prev`` - the previously stored value,
* ``tstamp`` - the time stamp of the latest update,
* ``derivatives`` - automatically calculated numerical derivatives up to a configurable order,
* plotting support,
* renormalization support.

Numeric scalar and vector values can be supplied together with time stamps. MLPro then updates the internal history and derives higher-order information automatically. A typical lifecycle therefore looks like this:

``new value -> update history -> update time stamp -> calculate derivatives -> update visualization``

A minimal example illustrates the idea:

.. code-block:: python

    from mlpro.bf.math.properties import Property

    position = Property(
        p_name='position',
        p_derivative_order_max=1,
        p_value_prev=True
    )

    position.set(p_value=0.0, p_tstamp=0)
    position.set(p_value=2.0, p_tstamp=1)
    position.set(p_value=5.0, p_tstamp=2)

    print(position.value)          # 5.0
    print(position.value_prev)     # 2.0
    print(position.derivatives[1]) # 3.0

Here, the first derivative represents the rate of change between the latest samples. Higher derivative orders can be enabled in the same way.

Managing several properties
---------------------------

The class **Properties** is intended as a parent class for objects that require several managed state variables. Properties can be defined statically through the class attribute ``C_PROPERTIES`` or added dynamically at runtime. Each property is exposed as an attribute of the owning object and can be queried, replaced, linked, plotted, or renormalized together with the surrounding property structure.

This makes Properties useful whenever an object consists of several related characteristics. A geometric object, for example, may expose a center, a size, or other quantities as individual managed properties while still presenting them through one common object.

**Reusable definitions.** A property definition is represented by a tuple containing the property name, maximum derivative order, a switch for storing the previous value, and the Property class to be instantiated. The type aliases ``PropertyDefinition`` and ``PropertyDefinitions`` provide a standardized format for such reusable configurations.

**Hierarchical properties.** The class **MultiProperty** extends the concept to properties that themselves contain further managed properties. This is useful for structured mathematical or geometric objects whose top-level characteristics are composed of several dependent sub-properties.

The property system is a foundation for several other MLPro-BF-MATH components, especially the geometry package. Classes such as **Point**, **Crosshair**, and **Hypercuboid** combine managed values, optional derivatives, visualization, and renormalization through this common abstraction.


**Cross reference**
    + :ref:`API Reference - Managed Properties <target_ap_bf_math_properties>`
