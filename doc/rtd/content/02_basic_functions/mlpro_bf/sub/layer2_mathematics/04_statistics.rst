.. _target_bf_math_statistics:

Statistics and Boundaries
=========================

Why standardized boundaries?
----------------------------

Many algorithms need to know the valid or currently observed range of each dimension. Normalizers need source ranges, search procedures operate inside regions, plots need limits, and adaptive components may update their range estimates while data changes.

If every component represents boundaries differently, even a simple question such as "what is the upper limit of dimension 2?" requires custom conversion logic. MLPro-BF-MATH therefore provides a small standardized boundary interface in :mod:`mlpro.bf.math.statistics`.

The basic representation is deliberately simple:

``one dimension -> [lower, upper]``

and for multiple dimensions:

``[[lower_0, upper_0], [lower_1, upper_1], ...]``

Boundary handling
-----------------

**Creating boundary arrays.** The type alias **Boundaries** represents a numpy array of floating-point boundary values. The static helper ``BoundaryProvider.create_boundaries()`` creates the standard structure with one row per dimension and two columns for lower and upper values. Initially, all entries are ``NaN`` so that unknown boundaries remain explicit.

.. code-block:: python

    from mlpro.bf.math.statistics import BoundaryProvider

    boundaries = BoundaryProvider.create_boundaries(p_num_dim=3)

    print(boundaries.shape) # (3, 2)
    print(boundaries)

A component that computes or stores boundaries can use this helper to create a representation that other MLPro components already understand.

**Selecting lower and upper sides.** The enum **BoundarySide** avoids magic integer indices when client code needs only one side of the interval. It defines the two values ``LOWER`` and ``UPPER``.

.. code-block:: python

    from mlpro.bf.math.statistics import BoundarySide

    lower_side = BoundarySide.LOWER
    upper_side = BoundarySide.UPPER

**Providing boundaries through a common interface.** **BoundaryProvider** defines the contract for objects that expose boundaries. Concrete subclasses implement ``get_boundaries()`` and may reduce the result by dimension and/or boundary side.

The same method can therefore answer four common questions:

* return all lower and upper boundaries,
* return both boundaries of one dimension,
* return all lower or all upper boundaries,
* return one scalar boundary value for a selected dimension and side.

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

Boundary handling is intentionally a small building block, but it connects naturally to the rest of BF-MATH: normalizers can derive scaling parameters from dimensional boundaries, Hypercuboids use lower and upper limits per dimension, and Dimensions can carry configured boundaries of their own. The common interface allows algorithms to consume these ranges without being coupled to a particular producer.


**Cross reference**
    + :ref:`API reference <target_ap_bf_math_stat>`
