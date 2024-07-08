.. include:: /rst/exports/roles.include

.. _demos_debugger:

AML-DL Debugger
###############

Here we use the embedding described in :ref:`demos_queens_embedding` as an example.

We have also added the following duple to create an inconsistet embedding, and illustrate the debugging process.

.. code-block:: python

    theEmbedding.REGION = 14
    ADD(INC(F("Q", 4), F("E", 4)))

Basic use
*********

To execute the AML-DL Debugger:

.. code-block:: bash

    python amlDebugger.py queens_embedding.py parameters

We can use additional parameters to make our embedding more flexible.
Change the call to the `embedding` function adding the "boardDim" as a function parameter.

.. code-block:: python

    def embedding(boardDim):

In this examples, when not specified, we call the embedding with dimension 8, same as a conventional chessboard.

.. code-block:: bash

    python amlDebugger.py queens_embedding.py 8

The AML-DL Debugger should welcome you with the following menu screen.

.. image:: /rst/figures/demos/debugger_menu.png
   :width: 1002
   :alt: AML-DL Debugger main menu
   :align: center

Expected format
===============

The AML-DL Debugger expects a tuple with the names of the constants and the positive and negative duples.
The correct return can easily be achieved by ending your embedding function with the following lines:

.. code-block:: python

    constantNames = [el.key for el in F("constants pending transfer to algebra").r]
    p = F("inclusions").r
    n = F("exclusions").r

    return constantNames, p, n


Creating an embedding
*********************

The AML-DL Debugger can greatly help to build embeddings by displaying in a user-friendly manner the constants and duples resulting from AML-DL expressions.
This can be useful to detect errors early while creating embeddings.

The suggested workflow is to build the minimum scaffold for an embedding, load it into the AML-DL Debugger, and then simply refresh it using the reload key ``R`` to display the changes on the embedding.

This code snippets can be used as a template for your embedding.
The AML-DL Debugger can read it with no issue.

.. code-block:: python

    def embedding(boardDim):

        with Descriptor() as theEmbedding:

            # -- Define constants

            # -- Define duples

            constantNames = [el.key for el in F("constants pending transfer to algebra").r]
            p = F("inclusions").r
            n = F("exclusions").r

        return constantNames, p, n

Defining the embedding constants
================================

To build the embedding for the N-Queens completion problem, we start by defining the set of queens:

.. code-block:: python

    CV("Q", boardDim * boardDim)

After (R)eloading the embedding in the AML-DL Debugger, we can (I)nspect the embedding:

.. image:: /rst/figures/demos/debugger_consts_1.png
   :width: 1002
   :alt: AML-DL Debugger displaying some constants while building the N-Queens embedding
   :align: center

We find the :math:`N^2` Queens, and no other constants or duples.

After adding all constants and reloading the embedding we can see the following result:

.. image:: /rst/figures/demos/debugger_consts_2.png
   :width: 1002
   :alt: AML-DL Debugger displaying all constants for the N-Queens embedding
   :align: center

In this case, since the board dimension is a parameter, we can easily modify it and check how that affects at the resulting constants.

Defining the embedding duples
=============================

In a similar fashion we can start adding some duples:

.. code-block:: python

    theEmbedding.REGION = 1
    # {R(i), C(j)} < Q(i,j)
    for x in range(0, boardDim):
        for y in range(0, boardDim):
            ADD(INC(M(F("R", x), F("C", y)), F("Q", ix(x, y))))

    # R(i) !< {Qx!=i, E}
    ADD(EXC(T("R", _i), M(R("Q(x=, )", T("Q(x=, )", _i)), "E")))

    theEmbedding.REGION = 2
    # C(j) !< {Qy!=j, E}
    ADD(EXC(T("C", _i), M(R("Q( ,y=)", T("Q( ,y=)", _i)), "E")))

After reloading the embedding and using the inspector, we observe that :math:`N^2` positive duples have been created from the first AML-DL expression, and :math:`N` negative duples from each of the following two expressions.

.. image:: /rst/figures/demos/debugger_duples_1.png
   :width: 1247
   :alt: AML-DL Debugger displaying some duples while building the N-Queens embedding
   :align: center

When adding all positive and negative duples (notice that we have added an additional negative duple), the full embedding results in:

.. image:: /rst/figures/demos/debugger_duples_2.png
   :width: 1247
   :alt: AML-DL Debugger displaying all duples for the N-Queens embedding
   :align: center

Debugging an embedding
**********************

It is possible to run into an inconsistency while writing an embedding.
The consistency module can be run at any point during the creation of an embedding, and can help to detect contradictory sentences as soon as they are introduced.

When adding the following expression to the N-Queens embedding, it becomes inconsistent.

.. code-block:: python

    theEmbedding.REGION = 14
    ADD(INC(F("Q", 4), F("E", 4)))

The AML-DL Debugger shows the following output:

.. image:: /rst/figures/demos/debugger_inconsistent.png
   :width: 1080
   :alt: AML-DL Debugger displaying inconsistent duples in an embedding
   :align: center

As described in :ref:`demos_consistency_checker`, the issue is that the embedding imposes two contradictory conditions:
:math:`R[4] < E[4]` and :math:`R[4] \nless E[4]`.

By removing the expression in region 14 the embedding returns to be consistent and the consistency module displays a successful result.

.. image:: /rst/figures/demos/debugger_consistent.png
   :width: 372
   :alt: AML-DL Debugger displaying a succesful result for a consistent embedding
   :align: center

