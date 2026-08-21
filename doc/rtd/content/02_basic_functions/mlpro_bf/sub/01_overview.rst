Overview
========

MLPro-BF is the common foundation stack of the MLPro ecosystem. It standardizes the infrastructure, execution models,
mathematical abstractions, application interfaces, and machine-learning semantics that are reused throughout MLPro.
Higher sub-frameworks can therefore concentrate on their domain-specific functionality instead of reimplementing the same
fundamental mechanisms again and again.

MLPro-BF is organized in five layers that deliberately build on one another:

.. image:: images/MLPro-BF_Overview.drawio.png
    :scale: 50%


The five-layer architecture
---------------------------

**Layer 0 - Elementary functions**
    :ref:`Layer 0 <target_bf_elementary>` provides the elementary technical infrastructure used throughout MLPro. It covers
    logging, time handling, persistence, data management, plotting and visualization support, scientific referencing, and
    further reusable base services and objects.

**Layer 1 - Computation**
    :ref:`Layer 1 <target_bf_computation>` standardizes execution and orchestration. Its central concepts include events,
    multitasking and asynchronous execution, tasks, workflows, shared objects, and generic operational scenarios with simulation
    and real-operation modes. These runtime abstractions are reused by many higher MLPro components.

**Layer 2 - Mathematics**
    :ref:`Layer 2 <target_bf_mathematics>` provides the common mathematical object model. It introduces dimensions, sets and
    spaces, elements, functions, normalizers, properties, geometric objects, and statistical utilities. These abstractions form
    a shared mathematical language for application and ML layers above.

**Layer 3 - Application support**
    :ref:`Layer 3 <target_bf_application_support>` connects the generic foundation to concrete applications. It provides
    standardized support for data stream processing, physics-related functionality, state-based systems including real hardware
    access, and closed-loop control. This layer is where reusable runtime and mathematical concepts become application-facing
    building blocks.

**Layer 4 - Machine learning**
    :ref:`Layer 4 <target_bf_ml>` anchors the paradigm-independent semantics of machine learning at BF level. It standardizes
    adaptive models, ML scenarios, training and hyperparameter tuning, adaptation events, adaptive workflows, adaptive functions,
    and adaptive systems. Higher MLPro domains can therefore build on the same definition of what an adaptive model is and remain
    interoperable across learning paradigms.


How the layers work together
----------------------------

The architecture can be read as a progression of abstraction levels::

    Infrastructure -> Execution -> Mathematics -> Applications -> Machine Learning

Each layer reuses the capabilities below it and adds a new level of semantics. A machine-learning model can therefore inherit
persistence and logging from the elementary layer, multitasking and event handling from the computation layer, mathematical
spaces and functions from the mathematics layer, and application abstractions such as streams or systems where needed.

The same principle continues above MLPro-BF: specialized MLPro sub-frameworks reuse and refine these common foundations rather
than defining isolated implementations of recurring concepts. This layered design is what enables consistent behavior,
reusability, and interoperability across the MLPro ecosystem.
