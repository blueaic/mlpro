.. _target_bf_math_normalizer:

Normalization
=============

Why normalization?
------------------

Many algorithms become easier to combine and numerically more stable when their input features live on comparable scales. A temperature in degrees, a position in meters, and a probability may all describe the same sample, but their numerical ranges can differ by orders of magnitude.

MLPro treats normalization as a reversible mapping rather than as a one-way preprocessing step. The abstract **NormalizerAPI** defines the common interface for normalization, denormalization, and renormalization. The base class **Normalizer** implements this interface and extends :class:`Scaler` with a consistent linear parameter model.

**NormalizerAPI** declares three abstract operations:

* ``normalize(p_data, p_dim=None, p_param=None)`` maps data into normalized coordinates,
* ``denormalize(p_data, p_dim=None, p_param=None)`` maps normalized data back to their original coordinates,
* ``renormalize(p_data, p_dim=None, p_param_old=None, p_param_new=None)`` transforms normalized data from one parameter set to another.

The interface is independent of the normalization strategy. Concrete implementations provide the normalization behavior and parameter management. The optional ``p_dim`` argument selects a single dimension; parameter arguments allow explicit parameter sets where supported.

The basic lifecycle is:

``raw data -> determine parameters -> normalize -> parameters change -> renormalize``

The supplied MLPro normalizers use linear parameters per dimension. Internally, each dimension has a scale factor and an offset. This common representation enables the same operations for different normalization strategies:

* ``normalize()`` maps original data into normalized coordinates,
* ``denormalize()`` reconstructs data in the original coordinates,
* ``renormalize()`` converts already normalized data from an old parameter set to a new one,
* ``update_parameters()`` adapts the normalizer to new boundaries or statistics.

The operations work with MLPro data representations such as Elements and numpy arrays and can also be applied dimension-wise.

Normalization strategies
------------------------

**MinMax normalization.** **NormalizerMinMax** maps known source boundaries to configurable destination boundaries. The default destination interval is ``[-1, 1]``.

.. code-block:: python

    import numpy as np
    from mlpro.bf.math.normalizers import NormalizerMinMax

    normalizer = NormalizerMinMax(p_dst_boundaries=[-1, 1])
    normalizer.update_parameters(
        p_boundaries=np.array([
            [0.0, 100.0],
            [-50.0, 50.0]
        ])
    )

    data = np.array([[25.0, 0.0]])
    normalizer.normalize(data)

The boundaries may also be obtained directly from an MLPro Set. If source boundaries change, a new parameter set is computed while the former one is retained for later renormalization.

**Z transformation.** **NormalizerZTrans** standardizes data using mean and standard deviation. Parameters can be initialized from a complete dataset or maintained incrementally when samples are added or removed.

.. code-block:: python

    import numpy as np
    from mlpro.bf.math.normalizers import NormalizerZTrans

    dataset = np.array([
        [1.0, 10.0],
        [2.0, 20.0],
        [3.0, 30.0]
    ])

    normalizer = NormalizerZTrans()
    normalizer.update_parameters(p_dataset=dataset)

    sample = np.array([[2.0, 20.0]])
    normalizer.normalize(sample)

The incremental parameter update is especially useful for online scenarios where the statistical description of the data changes over time.

**Why renormalization matters.** In adaptive or online applications, normalization parameters may change after data has already been normalized. Simply applying the new parameters to old normalized values would move them into the wrong coordinate system.

MLPro therefore stores previous and current parameter sets. ``renormalize()`` first reconstructs the original value with the old parameters and then applies the new parameters:

``normalized(old) -> denormalize(old) -> normalize(new) -> normalized(new)``

This allows stored states, geometric properties, or other normalized data structures to remain consistent while the normalization model evolves.


**Cross reference**
    + :ref:`Howto BF-MATH-011: Normalizers <Howto BF MATH 011>`
    + :ref:`API reference <target_ap_bf_math_norm>`
