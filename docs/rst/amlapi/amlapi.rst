.. include:: /rst/exports/alias.include
.. include:: /rst/exports/roles.include

.. _aml_api:

#############################
Open AML Engine API Reference
#############################


==========
Core types
==========

Segments
########

``Segments`` represent sets of constants.

``Segments`` have the same interface as Python ``set()``

.. code-block:: python

    class UCSegment(amlset):
        """
        Representation of an upper constant segment:
        UCSegment < {c1, c2, ...}
        """


    class LCSegment(amlset):
        """
        Representation of a lower constant segment:
        {c1, c2, ...} < LCSegment
        """


    class CSegment(amlset):
        """
        Representation of a set of embedding constants
        """

Atom
####

The basic element in AML models.

.. code-block:: python

    class Atom:
        """
        Individual atom from an atomization model.

        Vars:
        ucs (UCSegment) : representation of the upper constant segment of the atom
        gen (int)       : iteration at which the atom was created
        G   (int)       : amount of crossings needed to produce the atom
        ID  (int)       : unique identifier
        """

        def __eq__(self, other)

        def __hash__(self)

        def copy(self)


Duple
#####

Representation of a positive or negative duple in an embedding.

.. code-block:: python

    class Duple:
        """
        It represents a logic sentence of the embedding: `Left < Right`.
        It takes two terms for the left and right side of the inclusion operator.

        Vars:
        L,R (LCSegment)   : left and right terms of the Duple
        positive (bool)   : True  for positive duples (inclusion)
                            false for negative duples (exclusion)
        generation (int)  : to store generation at which it was created
        region (int)      : can be used to group duples
        hypothesis (bool) : when True the Duple is only used during training
                            if it does not create an inconsistency
        """

        def copy(self)

ConstantManager
###############

Manages embedding constants, and their names and indices.

.. code-block:: python


    class ConstantManager:
        """
        Hold information about the model's constants.
        Establish mapping between indices and embedding constants

        Vars:
        definedWithName (Dict[str:int]) : map from names to internal indices
                                          used by the engine {name -> index}
        embeddingConstants (amlset)     : set with indices created/used
        """

        def __eq__(self, other)

        def copy(self)

        def setNewConstantIndex(self):
            """
            Create a new constant.
            Return the index of the new constant.
            """

        def setNewConstantIndexWithName(self, name):
            """
            Create a new constant and store its name in 'definedWithName".
            Return the index of the new constant.
            """

        def getReversedNameDictionary(self):
            """
            Return a map from constants' indices to constants' names.
            """

        def updateConstantsTo(self, atomization, unionModel, storedPositives):
            """
            Remove unused constants from the ConstantManager.
            Removes constants not present in 'atomization',
            'unionModel', or in 'storedPositives'.
            """



Model exploration and manipulation
##################################

Function to analyse and manipulate model atomizations and duples.

.. code-block:: python

    def atomizationCopy(atomSet):
        """Deep copy of an atomization"""

    def removeRepeatedAtoms(atomization):
        """
        Remove repeated atoms with the same upper constant segment.
        From a pair o repeated atoms, it preserves the one with the most recent generation.
        """

    def removeRedundantAtoms(atomization, constants, markAsChecked):
        """
        Return a new atomization containing the non redundant atoms in 'atomization'.
        An atom is redundant with respecto to an atomization if
        it can be formed as the union of other atoms in the atomization.

        Vars:
        atomization (List[Atom]) : atomization
        constants (CSegment) : embedding constants.
        markAsChecked (bool) : mark surviving atoms.
        """

    def lowerOrEqual(left, right, atomization):
        """
        Return True if the term 'left' is contained in the term 'right'.
        If the lower atomic segment of a term A is a subset
        of the lower atomic segment of another term B, then the term A
        is contained in B.
        If A has some atom that B lacks, then A is not contained in B.

        Vars:
        left,right (LCSegment)   : left and right terms of the Duple.
        atomization (List[Atom]) : atomization.
        """

    def atomsNotIn(atomization, term):
        """
        Return the atoms in 'atomization' that do not form part of
        the lower atomic segment of 'term'.
        """

    def atomsIn(atomization, term):
        """
        Return the atoms in 'atomization' that form part of
        the lower atomic segment of 'term'.
        """

============
Embedders
============

Define how the training is performed.

Full Crossing Embedder
######################

.. code-block:: python

    class full_crossing_embedder:
        """
        Performs sparse crossing

        Vars:
        model (List[Atoms])      : The algebraic model.
        params (params_full)   : Holds params to modify the embedder's behaviour
        """

        def sortDuplesBySolvability(self, atomization, duples):
            """
            Sort list of duples to improve efficiency in the full crossing

            It is used in enforce if params.sortDuples is set to True

            Vars:
            atomization (List[Atoms]) : The algebraic model.
            duples (List[Duples])  : list of positive duples to be sorted.

            Return:
            List[Duples] : the set of duples sorted by solvability.
            """

        def enforce(self, duples):
            """
            Perform the training stage.

            Given a batch of positive duples, it performs the full crossing of
            every duple over the model.

            Vars:
            pDuples (List[Duples])  : list of positive duples
            """

Full Crossing Embedder Parameters
#################################

.. code-block:: python

    class params_full:
        """
        Holds params to modify the embedder's behaviour

        Vars:
        calculateRedundancy (bool) : Remove redundant atoms afeter every crossing.
        removeRepetitions (bool) : Remove repeated atoms after every crossing.
        sortDuples (bool) : Sort duples by solvability to reduce crossing time.
        binary (bool) : Sets on optimizations for binary problems.
        """

Sparse Crossing Embedder
######################

.. code-block:: python


    class sparse_crossing_embedder:
        """
        Performs sparse crossing
        It contains an algebraic model that can be trained, and heavily changes
          between iterations so it satisfies the last batch of duples.
        It also contains a union model that accumulates the atoms from models
          at every iteration. This model is much larger than the model used during
          a single step. This model represents the actual knowledge adquired over
          multiple iterations and it is generally the one used as a result of
          the training process.

        Vars:
        model (List[Atoms])      : The current algebraic model. It is used as inital
                                   conditions for the following iteration, and
                                   it is modified to adjust exactly to the current
                                   training batches.
        unionModel (List[Atoms]) : Set of atoms gathered from every iteration.
        params (params_sparse)   : Holds params to modify the embedder's behaviour
        """

        def enforce(self, pDuples, nDuples):
            """
            Perform the training stage.

            Given two batches of positive and negative duples, it trains the current
            model.

            pDuples (List[Duples])  : list of positive duples
            nDuples (List[Duples])  : list of negative duples
            """

        def testAccuracy(self, duples):
            """
            Compute FPR and FNR.

            All terms need to have their lower atomic segment calculated by
            termSpace.calculateLowerAtomicSegments()

            Vars:
            duples (List[Duples])  : list of positive and negative duples
            """

        def test(self, duples, region=-1):
            """
            Report FPR and FNR as a string

            Vars:
            duples (List[Duples])  : list of positive and negative duples
            region (int, optional) : if defined only duples in that region
                                     are considered
            """

        def setAtomization(self, atomization):
            """
            Updates the model's atomization

            Vars:
            atomization (List[Atoms]) : New atomization
            """

Sparse Crossing Embedder Parameters
###################################

.. code-block:: python

    class params_sparse:
        """
        removeRepetitions (bool) : Remove repeated atoms after every crossing.
        reductionByTraces (bool) :
        enforceTraceConstraints (bool) : True:  Enforce trace constrains using atomization.
                                         False: Introduce a fresh atom under every constant
                                                needed to close the traces.
        byQuotient (bool) : Set optimizations only for binary classification.
        storePositives (bool) : If a positive duple produced new atoms during crossing,
                                  the duple is stored and reused in the following batch.
        useReduceIndicators (bool) : The amount of atoms in the dual is reduced
                                       while keeping trace invariance
        negativeIndicatorThreshold (int) : Fraction of the union model used.
        staticConstants (bool) : Set to True to avoid removing embedding constants
                                   in problems where the embedding does not change
                                   during training.
                                 Set to False when new constants are added and removed
                                   during training.
        simplify_threshold (int) : Growing factor between crossings that
                                     would trigger a simplify action.
        ignore_single_const_ucs (bool) : When computing the growth of an atomization,
                                           only account for atoms with more than one
                                           atom in their ucs.
        """
