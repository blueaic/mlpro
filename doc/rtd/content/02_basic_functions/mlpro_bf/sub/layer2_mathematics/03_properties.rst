.. _target_bf_math_properties:

Managed Properties
==================

MLPro provides an extended property system for classes that need to manage values together with additional information and behavior.
The module :mod:`mlpro.bf.math.properties` builds on Python attributes but adds functionality that is frequently required by dynamic and adaptive systems.

The basic class **Property** stores a value and can optionally provide:

* the previous value,
* a time stamp of the latest update,
* automatic numerical derivatives up to a configurable order,
* plotting support,
* renormalization support.

Values are accessed like managed attributes. Numeric scalar and vector values can be supplied with time stamps so that derivatives are updated automatically whenever a new value is assigned.
This makes Property suitable, for example, for quantities such as positions, velocities, accelerations, sizes, or other time-dependent characteristics.

The class **Properties** is intended as a parent class for objects that require several managed properties.
Properties can be defined statically through the class attribute ``C_PROPERTIES`` or added dynamically at runtime.
Each property is exposed as an attribute of the owning object and can be queried, replaced, linked, plotted, or renormalized together with the surrounding property structure.

A property definition is represented by a tuple containing the property name, maximum derivative order, a switch for storing the previous value, and the property class to be instantiated.
The related type aliases ``PropertyDefinition`` and ``PropertyDefinitions`` provide a standardized way to define reusable property configurations.

The class **MultiProperty** extends the concept to hierarchical properties that themselves contain further managed properties.
This is useful for structured mathematical or geometric objects whose top-level characteristics are composed of several dependent sub-properties.

The property system is used by several other MLPro-BF-MATH components, especially the geometry package.
Classes such as Point, Crosshair, and Hypercuboid combine managed values, optional derivatives, visualization, and renormalization through this common foundation.


**Cross reference**
    + :ref:`API Reference - Managed Properties <target_ap_bf_math_properties>`
