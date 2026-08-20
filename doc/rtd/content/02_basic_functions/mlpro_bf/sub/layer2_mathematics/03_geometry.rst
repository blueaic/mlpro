.. _target_bf_math_geo:

Geometry
========

Why geometric properties?
-------------------------

Many MLPro applications need to describe more than abstract feature vectors. They work with positions, regions, centers, sizes, trajectories, or other geometric state that changes over time.

MLPro-BF-MATH models these concepts as managed properties. Geometric objects can therefore carry their current value together with optional derivatives, visualization state, and renormalization behavior. The geometry package builds directly on :ref:`Managed Properties <target_bf_math_properties>`.

The main relationships are:

``Point -> Crosshair``

and

``MultiProperty -> Hypercuboid -> center + size``

Geometric building blocks
-------------------------

**Point.** A **Point** represents coordinates in a hyper-space. Because Point inherits from Property, it can optionally derive velocity and acceleration automatically from time-stamped position updates.

.. code-block:: python

    from mlpro.bf.math.geometry import Point

    point = Point(
        p_name='position',
        p_derivative_order_max=1
    )

    point.set(p_value=[0.0, 0.0], p_tstamp=0)
    point.set(p_value=[2.0, 3.0], p_tstamp=1)

    print(point.value)          # [2. 3.]
    print(point.derivatives[1]) # velocity

This makes a Point more than a coordinate container. It can act as a compact state variable for moving objects or evolving geometric centers. Point supports 2D, 3D, and nD visualization; in 2D and 3D views, a first derivative can additionally be visualized as a velocity vector.

**Crosshair.** A **Crosshair** specializes Point by adding axis-aligned guide lines through the current position. It retains the same managed-property behavior, including optional velocity and acceleration, plotting, and renormalization.

.. code-block:: python

    from mlpro.bf.math.geometry import Crosshair

    cursor = Crosshair(
        p_name='cursor',
        p_derivative_order_max=1
    )

    cursor.set(p_value=[1.5, -0.5], p_tstamp=0)

Typical use cases include highlighting a current operating point, a selected sample, or a geometric reference position. Because Crosshair is a Point, client code can treat both classes through the same basic interface whenever only position and derivative information matter.

**Hypercuboid.** A **Hypercuboid** represents an axis-aligned region in an arbitrary number of dimensions. Its value is stored as one lower and one upper boundary for every dimension.

.. code-block:: python

    from mlpro.bf.math.geometry import Hypercuboid

    region = Hypercuboid(p_name='region')
    region.set([
        [0.0, 4.0],
        [1.0, 5.0]
    ])

    print(region.center_geo.value) # geometric center
    print(region.size_geo.value)   # geometric size

Hypercuboid is implemented as a MultiProperty. Whenever its boundaries change, the dependent properties ``center_geo`` and ``size_geo`` are updated automatically. This is a direct example of how the managed-property system keeps several geometric characteristics synchronized.

**Collision checks.** Hypercuboid also provides a collision test for axis-aligned regions. Two hypercuboids collide as long as their intervals overlap in every dimension.

.. code-block:: python

    region_a = Hypercuboid(p_name='a')
    region_a.set([[0.0, 2.0], [0.0, 2.0]])

    region_b = Hypercuboid(p_name='b')
    region_b.set([[1.0, 3.0], [1.0, 3.0]])

    print(region_a.check_collision(region_b)) # True

This makes Hypercuboid useful as a lightweight representation of bounding boxes, operating regions, search spaces, or occupancy regions.

**Renormalization and visualization.** Geometric objects often live in data spaces whose normalization changes over time. Point and Hypercuboid therefore support renormalization through MLPro normalizers so that their internally stored values can follow a changed coordinate system. The geometry classes also integrate with MLPro's plotting infrastructure for 2D, 3D, and nD views.


**Cross reference**
    + :ref:`Howto BF-MATH-031: Geometry - Point in 2D <Howto BF MATH 031>`
    + :ref:`Howto BF-MATH-032: Geometry - Point in 3D <Howto BF MATH 032>`
    + :ref:`Howto BF-MATH-033: Geometry - Hypercuboid in 2D <Howto BF MATH 033>`
    + :ref:`Howto BF-MATH-034: Geometry - Hypercuboid in 3D <Howto BF MATH 034>`
    + :ref:`Howto BF-MATH-035: Geometry - Crosshair in 1D <Howto BF MATH 035>`
    + :ref:`Howto BF-MATH-036: Geometry - Crosshair in 2D <Howto BF MATH 036>`
    + :ref:`Howto BF-MATH-037: Geometry - Crosshair in 3D <Howto BF MATH 037>`
    + :ref:`Managed Properties <target_bf_math_properties>`
    + :ref:`Normalization <target_bf_math_normalizer>`
    + :ref:`API reference <target_ap_bf_math_geo>`
