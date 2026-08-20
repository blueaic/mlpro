.. _target_bf_mathematics:

Layer 2 - Mathematics
=====================

Mathematics is an integral part of many areas, particularly in the fields of data analysis, machine learning, and system simulation.
MLPro-BF-MATH provides a set of reusable mathematical abstractions and helper classes that serve as a foundation for many higher-level MLPro components.

The basic data model is built around the following classes:

   a) **Dimension**

      An object that specifies the properties of one dimension, including names, unit, base set, boundaries, description, symmetry, and further optional parameters.
      Besides numeric base sets such as real, natural, and integer numbers, dimensions can also represent data objects such as images or point clouds.

   b) **Set**

      A collection of dimensions representing a multivariate set in a mathematical sense.
      Sets can be extended by new dimensions, queried by dimension id or name, copied, appended, or spawned into subsets.

   c) **Element**

      An element of a multivariate set. Each component stores the value that belongs to one dimension of the related set.

   d) **ElementList**

      A lightweight container for multiple Element objects referenced by ids.

   e) **DataObject** and **Data**

      DataObject is a generic container for large or non-standard data objects with optional metadata.
      The type alias Data summarizes the common data representations used by mathematical mappings and scalers: scalar values, lists, numpy arrays, and Element objects.

.. image:: images/MLPro-BF-MATH_Basics.drawio.png
    :width: 800

For distance calculations MLPro provides **MSpace** and **ESpace**.
MSpace is the generic template for metric spaces, while ESpace implements the Euclidean distance.

The class **Function** provides a common interface for mathematical mappings. A function may map scalar values, lists, numpy arrays, and Element objects and may also provide an inverse mapping.
Mappings can optionally be restricted to a single dimension. For Element-based mappings, output elements can be created automatically when an output set and output element class are configured.

The class **Scaler** extends Function by a standardized parameter handling for scaling, unscaling, and rescaling data.
It is the common base for normalization algorithms and keeps previous and current parameter sets so that already scaled data can be transformed consistently after parameter updates.

Beyond these mathematical basics, MLPro-BF-MATH provides dedicated functionality for managed properties, normalization, geometry, and statistical boundary handling:

.. toctree::
   :maxdepth: 1
   :glob:

   layer2_mathematics/*


**Cross reference**
    + :ref:`Howto BF-MATH-001: Dimensions, Spaces and Elements <Howto BF MATH 001>`
    + :ref:`API Reference <target_ap_bf_math>`
