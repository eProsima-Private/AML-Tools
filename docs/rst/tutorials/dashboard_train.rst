.. include:: /rst/exports/alias.include
.. include:: /rst/exports/roles.include

.. _tutorials_dashboard_train:

####################################
Train a model with the AML Dashboard
####################################

Background
==========

The :term:`AML` Dashboard is a web-based tool that allows users to interact with the |aml| framework.

This tutorial showcases the training process of an |aml| model using the *AML Dashboard*.

.. figure:: /rst/figures/tutorials/train_dashboard.png
    :align: center
    :width: 100%

Prerequisites
=============

Ensure you have installed the *AML Dashboard* using one of the following methods:

- :ref:`Linux Installation <amldashboard_linux>`
- :ref:`Docker Image Installation <amldashboard_docker>`

For more information, check the :ref:`AML Dashboard Interfaces <amldashboard_interfaces_training>` and :ref:`AML Dashboard Usage <amldashboard_usage_training>` sections.

Running the demo
================

To run the necessary components for training a model using the |aml| Dashboard, follow these steps:

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

Start the Computing Node
------------------------

1. Load the |amlip| environment.

.. code-block:: bash

   source /AML-IP/install/setup.bash

2. Navigate to the ``backend`` directory.

.. code-block:: bash

   cd backend

3. Start one or more computing nodes:

.. code-block:: bash

   python3 computing.py

Each computing node will wait for job assignments and will collectively distribute the workload when multiple nodes are running.

Start the AML Dashboard
-----------------------

1. Navigate to the ``frontend/aml_dashboard`` directory.

.. code-block:: bash

   cd frontend/aml_dashboard

2. Start the |aml| Dashboard:

.. code-block:: bash

   npm run dev

3. Access the dashboard at `http://localhost:5173/ <http://localhost:5173/>`__.

Training the Model
==================

To train a model using the |aml| Dashboard, follow these steps:

1. Navigate to the ``Training`` tab on the |aml| Dashboard.

2. Specify the training parameters:

   - Number of parallel trainings (executions).
   - Number of iterations per execution.
   - Percentage of the dataset to distribute in each execution.
   - The target class when the classification is binary (this is the case when standard or custom datasets are used).

3. Configure the neural network parameters:

   - Number of layers.
   - Number of epochs.
   - Batch size.

   .. note:: 

      The target class previously set will also be used for the neural network training.

4. Optionally, upload an atomization file as a pre-trained model.

5. Click on the ``Train`` button in the *AML Training Launcher* to initiate the training process.

6. The training progress will be displayed, and the model status will update to **Finished :)** once the training is completed.

.. raw:: html

   <video id=myVideo width=100% height=auto autoplay loop controls muted>
      <source src="../../_static/resources/tutorials/dashboard_train.mp4">
      Your browser does not support the video tag.
   </video>

   <script>
      // Set the speed of the video once the page is loaded
      window.onload = function() {
         document.getElementById('myVideo').playbackRate = 1.0; // Set speed to 1.0x
      };
   </script>
