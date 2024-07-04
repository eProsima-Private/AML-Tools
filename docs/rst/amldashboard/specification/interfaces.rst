.. include:: /rst/exports/alias.include
.. include:: /rst/exports/roles.include

.. _amldashboard_interfaces:

##########
Interfaces
##########

The *AML Dashboard* integrates four main interfaces:

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
   By holding the collect button, the camera records the hand gesture to build a stack of labeled training data for |aml|.

3. **Data Set Overview**: Each collected image is displayed in a data set overview, where users can explore, move, or delete images in the training stack.
   This feature is crucial for iterative training, enabling users to remove or add new labeled data to improve the |aml| algorithm as needed.

.. figure:: /rst/figures/amldashboard/interfaces_data_collection.png

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

.. figure:: /rst/figures/amldashboard/interfaces_training.png

Explore Models
==============

The model exploration interface provides space for developers to add any desired model comparison matrix.
The Marcelle framework supports various comparison modules and allows users to create custom :term:`GUI` elements for specific calculations.

In the current setup, a confusion matrix is provided based on the trained model.
Users must actively trigger the update of the matrix, facilitating a clear before-and-after comparison.
Future work aims to extend this section with more targeted visualizations utilizing the |aml| output structure.

.. figure:: /rst/figures/amldashboard/interfaces_explore_models.png

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
While the demo is limited to four instruments, users can easily change this.
Users can recreate gestures to explore sound intersections using *AML Dashboard*.

.. figure:: /rst/figures/amldashboard/interfaces_music_exploration.png
