.. _target_bf_math_statistics:

Statistics and Boundaries
=========================

Why standardized boundaries?
----------------------------

Many algorithms need to know the valid or currently observed range of each dimension. Normalizers need source ranges, search procedures operate inside regions, plots need limits, and adaptive components may update their range estimates while data changes.

If every component represents boundaries differently, even a simple question such as "what is the upper limit of dimension 2?" requires custom conversion logic.
MLPro-BF-MATH therefore provides a small standardized boundary interface in :mod:`mlpro.bf.math.statistics`.

The basic representation is deliberately simple:

``one dimension -> [lower, upper]``

and for multiple dimensions:

``[[lower_0, upper_0], [lower_1, upper_1], ...]``

Creating boundary arrays
------------------------

The type alias **Boundaries** represents a numpy array of floating-point boundary values.
The static helper ``BoundaryProvider.create_boundaries()`` creates the standard structure with one row per dimension and two columns for lower and upper values.
Initially, all entries are ``NaN`` so that unknown boundaries remain explicit.

.. code-block:: python

    from mlpro.bf.math.statistics import BoundaryProvider

    boundaries = BoundaryProvider.create_boundaries(p_num_dim=3)

    print(boundaries.shape) # (3, 2)
    print(boundaries)

A component that computes or stores boundaries can use this helper to create a representation that other MLPro components already understand.

Selecting lower and upper sides
-------------------------------

The enum **BoundarySide** avoids magic integer indices when client code needs only one side of the interval.
It defines the two values ``LOWER`` and ``UPPER``.

.. code-block:: python

    from mlpro.bf.math.statistics import BoundarySide

    lower_side = BoundarySide.LOWER
    upper_side = BoundarySide.UPPER

This small abstraction becomes useful in generic algorithms that work independently of the concrete object providing the boundaries.

BoundaryProvider
----------------

**BoundaryProvider** defines the common interface for objects that expose boundaries.
Concrete subclasses implement ``get_boundaries()`` and may allow the result to be reduced by dimension and/or boundary side.

Conceptually, the same method can answer four different questions:

* no selection: return all lower and upper boundaries,
* one dimension: return the lower and upper boundary of that dimension,
* one side: return all lower or all upper boundaries,
* dimension plus side: return one scalar boundary value.

A typical consumer can therefore depend on the interface rather than on the internal storage of the producing object.

.. code-block:: python

    from mlpro.bf.math.statistics import BoundarySide

    # provider is a concrete BoundaryProvider implementation
    all_boundaries = provider.get_boundaries()
    dim_0          = provider.get_boundaries(p_dim=0)
    all_upper      = provider.get_boundaries(p_side=BoundarySide.UPPER)
    upper_dim_0    = provider.get_boundaries(
        p_dim=0,
        p_side=BoundarySide.UPPER
    )

The optional ``p_copy`` parameter lets implementations distinguish between returning a reference to their internal array and returning an independent copy.

Where boundaries connect to the rest of BF-MATH
------------------------------------------------

Boundary handling is intentionally a small building block, but it connects naturally to several other concepts:

* :ref:`Normalization <target_bf_math_normalizer>` can derive scaling parameters from dimensional boundaries.
* :ref:`Geometry <target_bf_math_geo>` represents Hypercuboids through lower and upper limits per dimension.
* Dimensions in the mathematical base layer can carry their own configured boundaries.

The standardized statistics interface is useful when these sources need to be consumed generically without coupling an algorithm to a particular producer.


**Cross reference**
    + :ref:`API reference <target_ap_bf_math_stat>`
