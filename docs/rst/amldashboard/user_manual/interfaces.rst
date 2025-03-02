.. include:: /rst/exports/alias.include
.. include:: /rst/exports/roles.include

.. _amldashboard_interfaces:

##########
Interfaces
##########

The *AML Dashboard* integrates six main interfaces:

.. _amldashboard_interfaces_data_collection:

Data Collection
===============

The first tab comprises five distinct areas that enable users to swiftly create their own data sets for training an |aml| model.

1. **Exploring Data Input**: The *AML Dashboard* collection interface is designed to help non-computer scientists easily create and understand data collection.
   It features the following components:

   - **A Drop-down Menu**: Allows users to select the dataset they want to collect.
     The available options are: *Sensors* (for gesture data), *MNIST* (for handwritten digits), *KMnist* (for handwritten Japanese characters),
     *FashionMnist* (for clothing items), *MedMnist* (for medical images), *Cifar10* (for objects) and *Custom* (for user-defined data).

   - **Ground Truth Video Stream**: Shows the actual video feed.

   - **Overlaid Skeleton Video**: Displays the skeleton recognized by the hand recognition algorithm.

   These visual aids allow users to test and explore the aspects captured by the model.

2. **Collecting Data**: Users can create their own data sets to train an |aml| model.
   A drop-down menu allows the selection of one out of four musical instruments for demonstration purposes.

3. **Data Set Browser**: Each collected image is displayed in a data set browser, where users can explore, move, or delete images in the training stack, as well as managing labels of the different classes.
   This feature is crucial for iterative training, enabling users to remove or add new labeled data to improve the |aml| algorithm as needed.

.. _amldashboard_interfaces_training:

Training
========

The Training page is where users can configure and monitor the training process of the |aml| model. It provides options to set training parameters, track the training progress, and compare the performance of the |aml| model with other classifiers.
Additionally, users can train both the |aml| model and a neural network model for future comparison.

It is divided in two sections:

1. **AML Model Training Information (Left Side)**:

   - **Training Information**: Users can set parameters such as the number of iterations, the percentage of data used for each execution or the target class when the classification is binary.

   - **Training Status**: Displays the current state of training.

2. **Comparison Model Training (Right Side)**:

   - **Model Parameters**: Users can set or alter parameters for a comparison model, such as a Multi-layer Perceptron (MLP) classifier.
     This model can be replaced with any other type of classifier for direct comparison with |aml|.

   - **Training Progress**: A loading bar shows the projected training duration.
     Below it, variations in loss and accuracy per epoch are visualized, helping experts assess the classification quality and data noise level.

.. _amldashboard_interfaces_fetching:

Fetching
========

This interface's purpose is to retrieve trained |aml| statistics and Models effortlessly.
It includes options to search for |aml| statistics and request an |aml| model.

It is divided into the following sections:

1. **Status Display**: Shows the current status of collaborative learning, statistics, and model fetching.

2. **AML Statistics Fetcher**:

   - **Search Button**: Search for |aml| statistics.

   - **Statistics Display**: Display the fetched statistics

3. **AML Model Fetcher**:

   - **Request Button**: Request an |aml| model.

   - **Model Display**: Display the fetched model.

.. _amldashboard_interfaces_evaluation:

Explore Models
==============

The model exploration interface provides space for developers to add any desired model comparison matrix.
The Marcelle framework supports various comparison modules and allows users to create custom :term:`GUI` elements for specific calculations.

In the current setup, a confusion matrix is provided based on the trained model.
Users must actively trigger the update of the matrix, facilitating a clear before-and-after comparison.
Future work aims to extend this section with more targeted visualizations utilizing the |aml| output structure.

Real Time Pattern Exploration
=============================

.. warning::

   This feature is only available when the dataset is ``Sensors``.

After training the models, users can move to the real time pattern exploration interface.
This part of *AML Dashboard* allows users to explore music patterns using the self-trained models.

Key features include:

1. **Model Selection**: Users can toggle between |aml| and *NN* models for real-time predictions.

2. **Camera Activation**: Starting the camera initiates real-time predictions from the activated model.

3. **Real-Time Predictions**: Predictions are shown in real-time.
   If both models run, the prediction confidence of the |aml| model determines the sound pattern volume.

Sound is produced by looping audio tracks of musical instruments assigned during data collection.
Users can recreate gestures to explore sound intersections using *AML Dashboard*.

.. _amldashboard_interfaces_context_broker:

Context Broker interaction
==========================

Create and update data in the Context Broker and receive solutions (inferences) from the |aml| model.

1. **Fiware Node**:

   - **Parameters**: Specify the Fiware Node parameters and Context Broker entity ID and attributes.

   - **Create Button**: Create the node using the provided parameters.

   - **Status Update**: Shows whether the node has been created successfully.

2. **Context Broker Data**:

   - **Data Upload**: Drag and drop an image or upload a file in the designated area to upload data.

   - **Post Data Button**: Send the data to the Context Broker.

   - **Data Status**: Indicates whether the data has been successfully loaded and posted.

   - **Solution Display**: Displays the solution received from the Context Broker, which is the inference received from the |aml| model after processing the data.

   - **Solution Status**: Indicates whether the solution has been successfully retrieved.

.. _amldashboard_interfaces_aml_ip:

AML-IP Nodes Management
=======================

Manage the |amlip| nodes within the network.

1. **Agent Nodes**:

   - **Create Agent Node**: Specify the necessary parameters for the corresponding Agent Node creation.

   - **Create Button**: Create the Agent Node.

   - **Status Update**: Indicates whether the node has been created successfully.

2. **Computing Nodes**:
   
   - **Create Button**: Create the Computing Node.

   - **ID of Computing Node to manage**: Enter the ID of the Computing Node to manage.

   - **Stop Button**: Stop the Computing Node.

   - **Run Button**: Run the Computing Node.
   
   - **Stop and Delete Button**: Delete the Computing Node.

   - **Status Update**: Indicates whether the node has been created, stopped, ran or delted successfully.

3. **Inference Nodes**:

   - **Create Button**: Create the Inference Node.

   - **ID of Inference Node to manage**: Enter the ID of the Inference Node to manage.

   - **Stop Button**: Stop the Inference Node.

   - **Run Button**: Run the Inference Node.

   - **Stop and Delete Button**: Delete the Inference Node.

   - **Status Update**: Indicates whether the node has been created, stopped, ran or delted successfully.

4. **Sender Nodes**:

   - **Create Button**: Create the Sender Node.

   - **Stop and Delete Button**: Delete the Sender Node.

   - **Status Update**: Indicates whether the node has been created, stopped, ran or delted successfully.

.. _amldashboard_interfaces_debugging:

Status
======

Get a detailed overview of the currently active |amlip| nodes within the network.

Here's what it entails:

* **ID**: Each node in the network has a unique Id.
  This Id is generated by combining the node's name with a randomly generated number, ensuring its uniqueness.

* **State**: This indicates the current operational status of each node, providing valuable insights into their functionality.

* **Kind**: Every node is categorized into a specific kind, defining their behavior and role within the network.
  There are no restrictions on the number of nodes of the same kind that can operate concurrently within the network.
