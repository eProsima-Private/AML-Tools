.. include:: /rst/exports/alias.include
.. include:: /rst/exports/roles.include

.. _amldashboard_interfaces:

##########
Interfaces
##########

The *AML Dashboard* integrates six main interfaces:

Data Collection
===============

The first screen comprises five distinct areas that enable users to swiftly create their own data sets for training an |aml| model.

1. **Exploring Data Input**: The *AML Dashboard* collection interface is designed to help non-computer scientists easily create and understand data collection.
   It features two video representations:

   - **Ground Truth Video Stream**: Shows the actual video feed.

   - **Overlaid Skeleton Video**: Displays the skeleton recognized by the hand recognition algorithm.

   These visual aids allow users to test and explore the aspects captured by the model.

2. **Collecting Data**: Users can create their own data sets to train an |aml| model.
   A drop-down menu allows the selection of one out of four musical instruments for demonstration purposes.

3. **Data Set Overview**: Each collected image is displayed in a data set overview, where users can explore, move, or delete images in the training stack.
   This feature is crucial for iterative training, enabling users to remove or add new labeled data to improve the |aml| algorithm as needed.

Training
========

The training page is separate from the data collection page to educate users on the various stages of the :term:`ML` life-cycle.

It is divided into two sections:

1. **AML Model Training Information (Left Side)**:

   - **Training Information**: Users can set parameters such as the number of iterations.

   - **Training Visualization**: Displays the current state of training.

2. **Comparison Model Training (Right Side)**:

   - **Model Parameters**: Users can set or alter parameters for a comparison model, such as a Multi-layer Perceptron (MLP) classifier.
     This model can be replaced with any other type of classifier for direct comparison with |aml|.

   - **Training Progress**: A loading bar shows the projected training duration.
     Below it, variations in loss and accuracy per epoch are visualized, helping experts assess the classification quality and data noise level.

Fetching
========

Retrieve trained |aml| statistics and Models effortlessly.
It includes options to search for |aml| statistics and request an |aml| model.

It is divided into the following sections:

1. **Status Display**: Shows the current status of collaborative learning, statistics, and model fetching.

2. **AML Statistics Fetcher**:

   - **Search Button**: Search for |aml| statistics.

   - **Statistics Display**: Display the fetched statistics

3. **AML Model Fetcher**:

   - **Request Button**: Request an |aml| model.

   - **Model Display**: Display the fetched model.

Explore Models
==============

The model exploration interface provides space for developers to add any desired model comparison matrix.
The Marcelle framework supports various comparison modules and allows users to create custom :term:`GUI` elements for specific calculations.

In the current setup, a confusion matrix is provided based on the trained model.
Users must actively trigger the update of the matrix, facilitating a clear before-and-after comparison.
Future work aims to extend this section with more targeted visualizations utilizing the |aml| output structure.

Music Exploration
=================

After training the models, users can move to the music exploration tab.
This part of *AML Dashboard* allows users to explore music patterns using the self-trained models.

Key features include:

1. **Model Selection**: Users can toggle between |aml| and *NN* models for real-time predictions.

2. **Camera Activation**: Starting the camera initiates real-time predictions from the activated model.

3. **Real-Time Predictions**: Predictions are shown in real-time.
   If both models run, the prediction confidence of the |aml| model determines the sound pattern volume.

Sound is produced by looping audio tracks of musical instruments assigned during data collection.
Users can recreate gestures to explore sound intersections using *AML Dashboard*.

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

   - **Data Status**: Indicates whether the data has been successfully posted.

   - **Solution Display**: Displays the solution received from the Context Broker, which is the inference received from the |aml| model after processing the data.

   - **Solution Status**: Indicates whether the solution has been successfully retrieved.

Status
======

Get a detailed overview of the currently active |amlip| nodes within the network.

Here's what it entails:

* **ID**: Each node in the network has a unique Id.
  This Id is generated by combining the node's name with a randomly generated number, ensuring its uniqueness.

* **State**: This indicates the current operational status of each node, providing valuable insights into their functionality.

* **Kind**: Every node is categorized into a specific kind, defining their behavior and role within the network.
  There are no restrictions on the number of nodes of the same kind that can operate concurrently within the network.
