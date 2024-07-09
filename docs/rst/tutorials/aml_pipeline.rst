.. include:: /rst/exports/roles.include

.. _tutorials_aml_pipeline:

AML Pipeline
############

You can request this Jupyter notebook and AML libraries in :ref:`Get access to AML Toolkit <get_access_toolkit>`.


Running a binary classifer with MNIST
*************************************

Load AML libraries
==================

Most functionality to work with AML can be found in two packages:
- ``aml_engine.amlSimpleLibrary`` contains functions and classes to create and manipulate AML models,
- ``aml_engine.amlAuxiliaryLibrary`` contains functions and classes specific for training.


.. code-block:: python

    from aml_engine import amlSimpleLibrary as sc
    from aml_engine import amlAuxiliaryLibrary as ql

Load MNIST dataset
==================

The original dataset files:

- ``t10k-images-idx3-ubyte``
- ``t10k-labels-idx1-ubyte``
- ``train-images-idx3-ubyte``
- ``train-labels-idx1-ubyte``

The dataset can be downloaded from:
http://yann.lecun.com/exdb/mnist/
and
https://huggingface.co/datasets/ylecun/mnist


.. code-block:: python

    from MNIST import mnistGenerator

The ``mnistGenerator`` searches and loads the datasets and provides functionality to load individual digits.

Embedding constants
===================

A simple embedding for black and white images:
- constants for each black pixel `B(i,j)` (height x width),
- constants for each white pixel `W(i,j)` (height x width),
- constants for each label (10 if using all digits).

For instance, with 2x2 images the embedding set would be
``[B(1,1), B(1,2), B(2,1), B(2,2), W(1,1), W(1,2), W(2,1), W(2,2), label(1), label(2), ...]``

### Embedding function

We can use the following function to embed MNIST images.

An image is defined by a set of constants, one per pixel. Each constant will describe that pixel as white or black.
For instance:
``[W(1,1), W(1,2), B(1,3), B(1,4), W(1,5), ... W(28,27), B(28,28)]``


.. code-block:: python

    def digitToConstants(d, size):
        ss = size * size
        printImage = False

        j = 0
        threshold = 256 / 10
        ret = [-1] * size * size
        for x in range(size):
            for y in range(size):
                if d[j] > threshold:
                    ret[j] = j
                else:
                    ret[j] = j + ss
                j += 1

        result = set(ret)
        return result

Functions to read examples and embed them as constants
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

These functions load images and embed them.

- ``mnistDigit`` produces embedded images from the target class, to create positive duples.
- ``mnistOtherDigit`` produces images from any class other than the target, to create negative duples.


.. code-block:: python

    def mnistDigit(targetDigit, size):
        d, label, i = MNIST_GENERATOR.getNextDigit(targetDigit, False)
        result = digitToConstants(d, size)
        return sc.amlset(result)


    def mnistOtherDigit(targetDigit, size):
        d, label, i = MNIST_GENERATOR.getNextDigit(targetDigit, True)
        result = digitToConstants(d, size)
        return sc.amlset(result)

Training
========

Training parameters
^^^^^^^^^^^^^^^^^^^


.. code-block:: python

    # Training iterations
    iterations = 1000 # Maximum number of mini-batch iterations

    # Problem parameters
    validation_size = 10000
    MNIST_GENERATOR = mnistGenerator(validation_size)
    gridSideLength = 28  # side of images in the MNIST dataset
    embedding_constants = {*range(0, 2 * gridSideLength * gridSideLength)}
    targetDigit = 0  # 0 ... 9

    balance = 9
    pBatchSize = 100
    nBatchSize = 100 * balance
    maxPTrainingExamples = 6000
    maxNTrainingExamples = 54000

Notice that we are picking one target digit.
The model will discriminate between that digit (positive class), and the rest.
It is also possible to slightly modify this script for the multiclass problem.

Model and batch trainer initialisation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Initialise the ``model`` object that contains:
- the ``atomization``, which is the model itself,
- the ``cmanager`` or constant manager, which contains information describing the constants (indices, names, etc).


.. code-block:: python

    model = sc.model()

Add to the constant manager in our model the embedding constants.

Notice that we also add a ``v`` constants.
In AML this name is generally used in binary classifiers to indicate the positive class.
If we had more classes we would simple add more labels (v1, v2, ..., or use any other naming convention).


.. code-block:: python

    for i in embedding_constants:
        c = model.cmanager.setNewConstantIndex()

    vIndex = model.cmanager.setNewConstantIndexWithName("v")
    vTerm = sc.amlset([vIndex])

When training, we also need to instantiate a ``batchLearner`` object that will take charge of all the details of training for one iteration (pinning terms, traces, dual model, etc).
Check the Algebraic Machine Learning paper for a detailed explanation (https://arxiv.org/abs/1803.05252).


.. code-block:: python

    # Initialize batch training
    batchLearner = ql.batchLearner(model)
    batchLearner.params.useReduceIndicators = True
    batchLearner.params.byQuotient = False
    batchLearner.params.staticConstants = True

Training loop
^^^^^^^^^^^^^

.. code-block:: python

    cOrange = "\u001b[33m"
    cGreen = "\u001b[36m"
    cReset = "\u001b[0m"

    # Start training
    for i in range(iterations):
        # Here we can add heuristics for the minibatch size

        # Generate and embed examples
        print("<Generating training set", end="", flush=True)
        nbatch = []
        for e in range(int(nBatchSize)):
            counterExampleTerm = mnistOtherDigit(targetDigit, gridSideLength)

            is_positive_duple = False
            generation = model.generation
            region = 1

            nRel = sc.duple(vTerm, counterExampleTerm, is_positive_duple, generation, region)  # fmt:skip
            nbatch.append(nRel)

        pbatch = []
        for e in range(int(pBatchSize)):
            exampleTerm = mnistDigit(targetDigit, gridSideLength)

            is_positive_duple = True
            generation = model.generation
            region = 1

            pRel = sc.duple(vTerm, exampleTerm, is_positive_duple, generation, region)
            pbatch.append(pRel)
        print(">")

        # Training function.
        # It is somewhat parallel to one backpropagation step, but instead of modifying weight
        #   it
        batchLearner.enforce(pbatch, nbatch)

        print(
            f"{cOrange}BATCH#:{cReset}",
            f"{cOrange}{i}{cReset}",
            "batchSize(",
            int(pBatchSize),
            ",",
            int(nBatchSize),
            "             ------------- master: ",
            "model size",
            len(batchLearner.unionModel),
        )

    if False:
        ql.saveAtomizationOnFile(
            batchLearner.lastUnionModel,
            model.cmanager,
            f"RESULTS/MNIST_{targetDigit}_{i}",
        )


Being the engine still in development, the output is quite verbose.
Below you can see the output of iteration 948.

::

    ... previous iterations ...

    <Generating training set>
    updating unionModel... 9976
    final unionModel size: 9884
     + region  1 > 100
     - region  1 > 900
    Number of indicators 2930
    Number of unique indicators 2930
    Number of indicators 2930
    Number of unique indicators 2930
    <Preparing space class...>
    <Calculating free traces...> (0.077s : c 0.075s - py 0.002s)
    Number of indicators after selecting useful 1316
    negative duple indicators 8
    Final number of indicators: 56
    <Calculating traces...> (0.049s : c 0.045s - py 0.004s)
    - 1  <>--
    + 2  + 4  + 1  + 1  + 2  + 1  + 1  + 2  + 3  + 1  + 2  + 1  + 1  + 1  + 2  --
    --
    --
    From 26 to 26 (repetition)
    Traces enforced with 26 atoms
    From 1002 to 1002 (repetition)
    <Traces of constants>
    CrossAll time: 0.074s
    From 10831 to 9977 (repetition)
    G spectrum:
      G 0 atoms 452
      G 1 atoms 8
      G 2 atoms 14
      G 3 atoms 38
      G 4 atoms 70
      G 5 atoms 80
      G 6 atoms 104
      G 7 atoms 94
      G 8 atoms 54
      G 9 atoms 22
      G 10 atoms 7
      G 11 atoms 2
      G 12 atoms 2
    L spectrum:
      L 1 atoms 452
      L 2 atoms 8
      L 3 atoms 14
      L 4 atoms 28
      L 5 atoms 46
      L 6 atoms 38
      L 7 atoms 22
      L 8 atoms 25
      L 9 atoms 18
      L 10 atoms 20
      L 11 atoms 17
      L 12 atoms 19
      L 13 atoms 20
      L 14 atoms 19
      L 15 atoms 7
      L 16 atoms 17
      L 17 atoms 17
      L 18 atoms 21
      L 19 atoms 18
      L 20 atoms 15
      L 21 atoms 19
      L 22 atoms 8
      L 23 atoms 11
      L 24 atoms 9
      L 25 atoms 8
      L 26 atoms 9
      L 27 atoms 5
      L 28 atoms 6
      L 29 atoms 4
      L 30 atoms 3
      L 31 atoms 3
      L 32 atoms 3
      L 33 atoms 2
      L 34 atoms 3
      L 35 atoms 1
      L 36 atoms 2
      L 37 atoms 3
      L 39 atoms 1
      L 40 atoms 1
      L 41 atoms 2
      L 42 atoms 1
      L 44 atoms 2
    fraction of negative indicators:  0.14285714285714285 , union model fraction:  15
    BATCH: 948 batchSize( 100 , 900              ------------- master:  model size 9977

    ... following iterations ...


Postprocessing
==============

Here you can explore the atomization in the last model: `model.atomization`

But also the cumulative model that has been built combining the atomizations across the whole training process: `batchLearner.unionModel`


.. code-block:: python

    print(f"{cGreen}Union model size:{cReset} {len(batchLearner.unionModel)}")
    print(f"{cGreen}Size spectrum:{cReset}")
    sc.printLSpectrum(batchLearner.unionModel)

    print(f"{cGreen}Some random atoms:{cReset}")
    import random
    for at in random.choices(model.atomization, k=10):
        print(at.ucs)

    batchLearner.unionModel.sort(reverse=True,key=lambda at: len(at.ucs))
    print(f"{cGreen}Largest atom{cReset}")
    print(batchLearner.unionModel[0].ucs)


This displays the following information::

    Union model size: 10409
    Size spectrum:
    L spectrum:
      L 1 atoms 1496
      L 2 atoms 27
      L 3 atoms 193
      L 4 atoms 286
      L 5 atoms 509
      L 6 atoms 637
      L 7 atoms 755
      L 8 atoms 959
      L 9 atoms 992
      L 10 atoms 938
      L 11 atoms 852
      L 12 atoms 713
      L 13 atoms 572
      L 14 atoms 362
      L 15 atoms 254
      L 16 atoms 194
      L 17 atoms 167
      L 18 atoms 110
      L 19 atoms 75
      L 20 atoms 50
      L 21 atoms 54
      L 22 atoms 29
      L 23 atoms 33
      L 24 atoms 24
      L 25 atoms 18
      L 26 atoms 23
      L 27 atoms 13
      L 28 atoms 13
      L 29 atoms 7
      L 30 atoms 7
      L 31 atoms 6
      L 32 atoms 6
      L 33 atoms 8
      L 34 atoms 6
      L 35 atoms 1
      L 36 atoms 4
      L 37 atoms 5
      L 38 atoms 1
      L 39 atoms 2
      L 40 atoms 3
      L 41 atoms 2
      L 42 atoms 1
      L 44 atoms 2
    Some random atoms:
    bitarray({264})
    bitarray({1184, 1568, 1351, 1512, 329, 303, 1136, 595, 596, 215, 125, 574})
    bitarray({222})
    bitarray({320, 1217, 1568, 357, 1134, 496, 1425, 1330, 244, 1268, 1052})
    bitarray({1568, 129, 1220, 1535, 1165, 1293, 271, 592, 597, 1304, 217, 1437, 351})
    bitarray({992, 513, 1568, 1029, 1194, 491, 939, 397, 653, 655, 1100, 690, 243, 1235, 1364, 1078, 539, 157})
    bitarray({582})
    bitarray({164})
    bitarray({1568, 1134, 1044, 398})
    bitarray({746})
    Largest atom
    bitarray({1280, 1408, 1160, 1162, 651, 1168, 657, 659, 1050, 1568, 289, 162, 425, 554, 1193, 1323, 302, 1198, 321, 970, 1357, 206, 1102, 208, 593, 1107, 1108, 215, 1113, 218, 348, 483, 996, 1251, 359, 1386, 620, 1132, 1133, 1136, 1137, 1267, 244, 509})


Plotting results
^^^^^^^^^^^^^^^^

For classification problems with square images the viewer module provides some functions to plot atoms.
It simply maps back constant indices to their position and color on an image.
It then uses ``matplotlib`` to output the results.


.. code-block:: python

    import viewer as av

    theViewer = av.atomViewer_bw_sq_image(
        cmanager=model.cmanager,
        min_size=2,
        scale=10,
        atoms_per_board=[10, 10],
    )
    theViewer.save(f"RESULTS/MNIST_IMG_{targetDigit}_{i}", batchLearner.unionModel)
    theViewer.save(f"RESULTS/MNIST_IMG_model_{targetDigit}_{i}", model.atomization)

As an example, below we show 100 atoms in ``model.atomization``.
Black and white pixels indicate that the constant is present in the atom; red, that both constants are present; and gray, that none is present.

.. image:: /rst/figures/tutorials/example_atoms_mnist.png
   :width: 400
   :alt: A hundred atoms from the atomization of MNIST.
   :align: center

