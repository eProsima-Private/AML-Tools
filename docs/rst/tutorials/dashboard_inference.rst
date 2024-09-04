.. include:: /rst/exports/alias.include
.. include:: /rst/exports/roles.include

.. _tutorials_dashboard_inference:

####################################
Make predictions with the AML Dashboard
####################################

Background
==========

The :term:`AML` Dashboard is a web-based tool that allows users to interact with the |aml| framework.

This tutorial showcases the process of making predictions based on an |aml| model using the *AML Dashboard*.

.. figure:: /rst/figures/tutorials/inference.png 
    :align: center
    :width: 100%

Prerequisites
=============

Ensure you have installed the *AML Dashboard* using one of the following methods:

- :ref:`Linux Installation <amldashboard_linux>`
- :ref:`Docker Image Installation <amldashboard_docker>`

For more information, check the :ref:`AML Dashboard Interfaces <amldashboard_interfaces_evaluation>` and :ref:`AML Dashboard Usage <amldashboard_usage_evaluation>` sections.

Running the demo
================

To run the necessary components for evaluating a model and making predictions using the |aml| Dashboard, follow these steps:

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

Start the Inference Node
------------------------

.. warning::

    Before starting the inference node, ensure that there is at least one model and traing set available in the download directory.

1. Load the |amlip| environment.

.. code-block:: bash

   source /AML-IP/install/setup.bash

2. Navigate to the ``backend`` directory.

.. code-block:: bash

   cd backend

3. Start one or more inference nodes:

.. code-block:: bash

   python3 inference.py

.. check if there can be more inference nodes run parallely. 
Each inference node will wait for job assignments and will collectively distribute the workload when multiple nodes are running. 

Start the AML Dashboard
-----------------------

1. Navigate to the ``frontend/aml_dashboard`` directory.

.. code-block:: bash

   cd frontend/aml_dashboard

2. Start the |aml| Dashboard:

.. code-block:: bash

   npm run dev

3. Access the dashboard at `http://localhost:5173/ <http://localhost:5173/>`__.

Evaluating the Model
====================

To evaluate a model using the |aml| Dashboard, follow these steps:

1. Navigate to the ``Batch Prediction`` tab on the |aml| Dashboard.

2. Click on the ``Update Predictions`` button in the *Algebraic Machine Learning* section to initiate the predictions.

5. The confusion matrix for the predictions made by the model will be displayed.

.. raw:: html

   <video id=myVideo width=100% height=auto autoplay loop controls muted>
      <source src="../../_static/resources/tutorials/dashboard-batch-prediction.mp4">
      Your browser does not support the video tag.
   </video>

   <script>
      // Set the speed of the video once the page is loaded
      window.onload = function() {
         document.getElementById('myVideo').playbackRate = 1.0; // Set speed to 1.0x
      };
   </script>

Real-Time Predictions
=====================

To make real-time predictions using the trained model with the |aml| Dashboard, follow these steps:

1. Navigate to the ``Real-time Prediction`` tab on the |aml| Dashboard.

2. Check on the ``toggle prediction`` button in the *Predict for AML* section to initiate the real-time prediction process.

5. The label for the predictions made by the model will be displayed.

.. raw:: html

   <video id=myVideo width=100% height=auto autoplay loop controls muted>
      <source src="../../_static/resources/tutorials/dashboard-real-time.mp4">
      Your browser does not support the video tag.
   </video>

   <script>
      // Set the speed of the video once the page is loaded
      window.onload = function() {
         document.getElementById('myVideo').playbackRate = 1.0; // Set speed to 1.0x
      };
   </script>