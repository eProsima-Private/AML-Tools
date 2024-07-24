.. include:: /rst/exports/alias.include
.. include:: /rst/exports/roles.include

.. _tutorials_dashboard_fetch:

####################################
Fetch a model with the AML Dashboard
####################################

Background
==========

The :term:`AML` Dashboard is a web-based tool that allows users to interact with the |aml| framework.

This tutorial showcases the fetching process of an |aml| model using the *AML Dashboard*.

.. figure:: /rst/figures/tutorials/fetch_dashboard.png
    :align: center
    :width: 100%

Prerequisites
=============

Ensure you have installed the *AML Dashboard* using one of the following methods:

- :ref:`Linux Installation <amldashboard_linux>`
- :ref:`Docker Image Installation <amldashboard_docker>`

For more information, check the :ref:`AML Dashboard Usage <amldashboard_fetching>` section.

Running the demo
================

To run the necesaary components for fetching a model using the |aml| Dashboard, follow these steps:

Start the backend server
------------------------

1. Navigate to the ``backend`` directory.

.. code-block:: bash

   cd backend

2. Load the |amlip| environment.

.. code-block:: bash

   source /AML-IP/install/setup.bash

3. Start the server:

.. code-block:: bash

   python3 server.py

Start the Model Manager Sender Node
-----------------------------------

1. Load the |amlip| environment.

.. code-block:: bash

   source /AML-IP/install/setup.bash

2. Navigate to the ``backend`` directory.

.. code-block:: bash

   cd backend

3. Start the Model Manager Sender Node:

.. code-block:: bash

   python3 sender.py

To stop the Model Manager Sender Node, press ``Ctrl + C``.

Start the AML Dashboard
-----------------------

1. Navigate to the ``frontend/aml_dashboard`` directory.

.. code-block:: bash

   cd frontend/aml_dashboard

2. Start the |aml| Dashboard:

.. code-block:: bash

   npm run dev

3. Access the dashboard at `http://localhost:5173/ <http://localhost:5173/>`__.

Fetching the Model
==================

To fetch a model using the |aml| Dashboard, follow these steps:

1. Click on the ``Fetching`` tab.

2. Click on the ``Search for statistics`` button in the *AML Statistics Fetcher*.

3. Once the statistics are received, the status will appear as **Statistics received !** in the *AML Collaborative Learning Status*.

4. Click on the ``Request model`` button in the *AML Model Fetcher*.

5. Once the model is received, the status will change to **Model received !** in the *AML Collaborative Learning Status*.

.. note::

   Make sure that at least one **Model Manager Sender Node** is running to facilitate the model fetching process.

.. raw:: html

   <video width=100% height=auto autoplay loop controls muted>
        <source src="../_static/resources/tutorials/dashboard_fetch.mp4">
        Your browser does not support the video tag.
    </video>
    <br></br>
