.. _target_bf_mathematics:

Layer 2 - Mathematics
=====================

Mathematical Foundations
------------------------

Machine learning code quickly becomes difficult to combine if every component brings its own idea of dimensions, data spaces, elements, mappings, or scaling.
MLPro-BF-MATH provides a common mathematical vocabulary for these recurring concepts so that higher-level components can exchange and process data in a standardized way.

The central idea is simple:

``Dimension -> Set/Space -> Element -> Function -> Scaler``

**Dimensions, sets and elements.** A **Dimension** stores the structural information of one coordinate, including names, unit, base set, boundaries, description, symmetry, and additional user-defined parameters. Besides numeric base sets such as real, natural, and integer numbers, dimensions can also represent data objects such as images or point clouds.

A **Set** combines several dimensions into a multivariate structure. Sets can be extended, queried by dimension id or name, copied, appended, or spawned into subsets. An **Element** represents one concrete point or data item in such a set and stores one value for every related dimension.

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

**Metric and Euclidean spaces.** The class **MSpace** is the generic template for metric spaces and defines the common distance interface. **ESpace** implements the Euclidean metric directly.

.. code-block:: python

    p1 = Element(space)
    p1.set_values([0.0, 0.0])

    p2 = Element(space)
    p2.set_values([3.0, 4.0])

    print(space.distance(p1, p2))  # 5.0

**Functions and scaling.** The class **Function** standardizes mappings between mathematical representations. Implementations may map scalar values, lists, numpy arrays, and Element objects, may provide an inverse mapping, and can optionally restrict a mapping to one dimension. For Element-based mappings, output elements can be created automatically if an output set and output element class are configured.

The class **Scaler** extends Function with standardized parameter handling for scaling, unscaling, and rescaling data. It maintains previous and current parameter sets so that already scaled data can be transformed consistently after parameters change. This mechanism is the foundation for MLPro's normalizers and is particularly useful in online or adaptive scenarios.

Higher-Level Mathematical Components
------------------------------------

The foundations above are intentionally generic. On top of them, MLPro-BF-MATH provides dedicated components for **normalization**, **managed properties**, **geometry**, and **statistical boundary handling**. These components reuse the same data structures and mapping concepts rather than introducing separate representations of their own.

The following pages describe these higher-level components in detail:

.. toctree::
   :maxdepth: 1
   :glob:

   layer2_mathematics/*


**Cross reference**
    + :ref:`Howto BF-MATH-001: Dimensions, Spaces and Elements <Howto BF MATH 001>`
    + :ref:`API Reference <target_ap_bf_math>`
