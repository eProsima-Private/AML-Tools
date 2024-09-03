.. include:: /rst/exports/alias.include
.. include:: /rst/exports/roles.include

.. _amldashboard_usage:

#####
Usage
#####

Prerequisites
=============

Ensure you have installed the *AML Dashboard* using one of the following methods:

- :ref:`Linux Installation <amldashboard_linux>`
- :ref:`Docker Image Installation <amldashboard_docker>`

Execution
=========

To run the *AML Dashboard*, follow the steps below:

Backend Server
--------------

Run the following commands to start the backend server:

1. Navigate to the ``backend`` directory.

.. code-block:: bash

   cd backend

2. Start the server:

.. code-block:: bash

   python3 server.py

AML-IP Nodes
------------

Depending on your requirements, you can run different types of |amlip| nodes:

1. Load the |amlip| environment

.. code-block:: bash

   source /AML-IP/install/setup.bash

2. Navigate to the ``backend`` directory.

.. code-block:: bash

   cd backend

* **Computing Node**

To run a Computing Node, execute:

.. code-block:: bash

   python3 computing.py

You can run multiple computing nodes simultaneously.
Each computing node will continuously await job assignments.
When running multiple nodes, they will collectively distribute the workload, optimizing the time to find a solution.

To stop a computing node, simply run ``ctrl+C``.

* **Model Manager Sender Node**

To run a Model Manager Sender Node, execute:

.. code-block:: bash

   python3 sender.py

To stop a Model Manager Sender Node, simply run ``ctrl+C``.

* **Inference Node**

To run an Inference Node, execute:

.. code-block:: bash

   python3 inference.py

To stop an Inference Node, simply run ``ctrl+C``.

AML Dashboard
-------------

To run the dashboard, follow the steps below:

1. Navigate to the ``frontend/aml_dashboard`` directory.

.. code-block:: bash

   cd frontend/aml_dashboard

2. Start the dashboard:

.. code-block:: bash

   npm run dev

With the *AML Dashboard* up and running, you can access it at the following address:

.. code-block:: bash

   http://localhost:5173/

Data Management Tab
^^^^^^^^^^^^^^^^^^^

To create a dataset, simply follow these steps:

1. Activate the ``video`` switch in the webcam section to enable webcam capture.

2. Specify the label of the dataset in the *Instance label* section.

3. Click on the ``Hold to record instances`` button in the *Capture instances to the training set* to start recording instances.

4. Once recorded, the dataset will be promptly displayed in the *dataset browser* section for easy access and management.

.. note::

   In order to be able to train a model, you must have at least two classes in the dataset.

.. figure:: /rst/figures/amldashboard/data_management.png

Training Tab
^^^^^^^^^^^^

To train a model using |aml|, follow these steps:

.. note::
   Please ensure that at least one **Computing Node** is running to facilitate the training process.

1. Specify the number of parallel trainings (executions) you wish to run.

2. Define the number of iterations per execution.

3. Set the percentage of dataset to distribute in each execution.

4. Click on the ``Train`` button in the *AML Training Launcher* to initiate the training process.

5. Once the training is completed, the model status will appear as **Finished :)** in the *AML Status*.

6. If the training process fails, an error message will be displayed indicating the reason for the failure.

.. figure:: /rst/figures/amldashboard/training.png

Fetching Tab
^^^^^^^^^^^^

To fetch a model, follow these steps:

.. note::

   Make sure that at least one **Model Manager Sender Node** is running to facilitate the model fetching process.

1. Click on the ``Search for statistics`` button in the *AML Statistics Fetcher*.

2. Once the statistics are received, the status will appear as **Statistics received !** in the *AML Collaborative Learning Status*.

3. Click on the ``Request model`` button in the *AML Model Fetcher*.

4. Once the model is received, the status will change to **Model received !** in the *AML Collaborative Learning Status*.

5. If the fetching process fails, an error message will be displayed indicating an error.

.. figure:: /rst/figures/amldashboard/fetching.png

Batch Prediction Tab
^^^^^^^^^^^^^^^^^^^^

To predict the output of a dataset, follow these steps:

.. note::

   Ensure that you have access to at least one |aml| Model to facilitate the batch prediction process.

1. Click on the ``Update predictions`` button in the *Algebraic Machine Learning*.

2. The predictions will be displayed in the Results *Algebraic Machine Learning* plot.

.. figure:: /rst/figures/amldashboard/batch_prediction.png

Real-Time Prediction Tab
^^^^^^^^^^^^^^^^^^^^^^^^

To predict the output of webcam images in real^time using an |aml| Model, follow these steps:

.. note::

   Ensure that you have access to at least one |aml| Model to facilitate the real^time prediction process.

1. Toggle the ``prediction`` switch in the *Predict for AML* section and activate the ``video`` switch in the webcam section.

2. The predictions will be displayed in the *Results AML* plot.

.. figure:: /rst/figures/amldashboard/real_time_prediction.png

Context Broker Tab
^^^^^^^^^^^^^^^^^^

To create and update data to the Context Broker and get the solution (inference) from the |aml| Model, follow these steps:

.. note::

   Make sure that the Context Broker is running to ensure successful interaction and data exchange. The Context Broker can be installed and configured as per instructions provided `here <https://github.com/telefonicaid/fiware-orion/blob/master/docker/README.md#1-the-fastest-way>`__.

1. Specify the Fiware Node parameters and Context Broker entity ID and attributes.

2. Click on the ``Create`` button to create the node using the provided parameters.

3. The *Fiware Node Status* will update to indicate whether the node has been created successfully.

4. Drag and drop an image or upload a file in the designated area to upload data.

5. Click the ``Post Data`` button to send the data to the Context Broker.

6. The *Data Status* will update to indicate whether the data has been successfully posted.

7. Once the solution is received, it will be displayed in the *Context Broker Solution* section and the *Solution Status* will update to **Solution received !** to indicate successful retrieval.

8. If the solution retrieval process fails, an error message will be displayed indicating an error.

.. figure:: /rst/figures/amldashboard/context_broker.png

Status Tab
^^^^^^^^^^

The status tab automatically refreshes every second, ensuring you receive real-time updates and information about the network's status.

.. figure:: /rst/figures/amldashboard/status.png
