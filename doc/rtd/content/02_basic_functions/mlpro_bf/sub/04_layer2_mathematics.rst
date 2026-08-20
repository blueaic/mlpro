.. _target_bf_mathematics:

Layer 2 - Mathematics
=====================

Why a mathematical base layer?
------------------------------

Machine learning code quickly becomes difficult to combine if every component brings its own idea of dimensions, data spaces, elements, mappings, scaling, or geometric state.
MLPro-BF-MATH provides a common mathematical vocabulary for these recurring concepts so that higher-level components can exchange and process data in a standardized way.

The central idea is simple:

``Dimension -> Set/Space -> Element -> Function -> Scaler``

A **Dimension** describes one coordinate or feature. Several dimensions form a **Set** or mathematical space. An **Element** carries concrete values in such a set. A **Function** maps data from one representation to another, while **Scaler** specializes this concept for reversible scaling and rescaling.

Dimensions, sets and elements
-----------------------------

A **Dimension** stores the structural information of one coordinate, including names, unit, base set, boundaries, description, symmetry, and additional user-defined parameters.
Besides numeric base sets such as real, natural, and integer numbers, dimensions can also represent data objects such as images or point clouds.

A **Set** combines several dimensions into a multivariate structure. Sets can be extended, queried by dimension id or name, copied, appended, or spawned into subsets.

An **Element** represents one concrete point or data item in such a set. Each component stores the value that belongs to one related dimension.

.. code-block:: python

    from mlpro.bf.math import Dimension, ESpace, Element

    space = ESpace()
    space.add_dim(Dimension('x'))
    space.add_dim(Dimension('y'))

    point = Element(space)
    point.set_values([2.0, 3.0])

    print(point.get_values())

For groups of elements, **ElementList** provides a lightweight id-based container. **DataObject** can wrap large or non-standard data objects together with optional metadata, while the type alias **Data** summarizes the common representations handled by mathematical mappings: scalar values, lists, numpy arrays, and Element objects.

.. image:: images/MLPro-BF-MATH_Basics.drawio.png
    :width: 800

Metric and Euclidean spaces
---------------------------

The class **MSpace** is the generic template for metric spaces and defines the common distance interface. **ESpace** implements the Euclidean metric directly.

.. code-block:: python

    p1 = Element(space)
    p1.set_values([0.0, 0.0])

    p2 = Element(space)
    p2.set_values([3.0, 4.0])

    print(space.distance(p1, p2))  # 5.0

Functions and mappings
----------------------

The class **Function** standardizes mappings between mathematical representations. Implementations may map scalar values, lists, numpy arrays, and Element objects and can optionally provide an inverse mapping.
Mappings may also be restricted to a single dimension.

For Element-based mappings, output elements can be created automatically if an output set and output element class are configured. This makes Function a reusable integration point for transformations that need to work consistently across several data representations.

Scaling as a reusable mapping pattern
-------------------------------------

The class **Scaler** extends Function with standardized parameter handling for scaling, unscaling, and rescaling data.
It maintains previous and current parameter sets so that already scaled data can be transformed consistently after parameters change.

This mechanism is the common foundation for MLPro's normalizers and is particularly useful in online or adaptive scenarios where the underlying data range or statistics evolve over time.

Further mathematical functionality
----------------------------------

MLPro-BF-MATH builds several higher-level concepts on top of these basics:

* :ref:`Normalization <target_bf_math_normalizer>` for reversible MinMax and Z-transform scaling,
* :ref:`Managed Properties <target_bf_math_properties>` for time-aware, derivative-aware state variables,
* :ref:`Geometry <target_bf_math_geo>` for reusable geometric managed properties,
* :ref:`Statistics <target_bf_math_statistics>` for standardized handling of value boundaries.

.. toctree::
   :maxdepth: 1
   :glob:

   layer2_mathematics/*


**Cross reference**
    + :ref:`Howto BF-MATH-001: Dimensions, Spaces and Elements <Howto BF MATH 001>`
    + :ref:`API Reference <target_ap_bf_math>`
