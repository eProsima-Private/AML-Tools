.. include:: /rst/exports/alias.include
.. include:: /rst/exports/roles.include

.. _amldashboard_implementation:

##############
Implementation
##############

The implementation is divided into three stages:

1. :ref:`amldashboard_user_interface`
2. :ref:`amldashboard_aml_training_server`
3. :ref:`amldashboard_real_time_prediction`

.. figure:: /rst/figures/amldashboard/aml-dashboard_implementation.png

.. _amldashboard_user_interface:

User Interface and Data Processing
==================================

The first stage involves the user interface, implemented using Marcelle and a web framework that handles data collection and processing.

This stage combines:

- **Frontend**: Implemented in JavaScript, it includes the Marcelle interface (:term:`GUI`) where users interact with the system to collect training data.
- **Backend**: Developed in Python, it processes the collected data and prepares it for model training.

.. _amldashboard_aml_training_server:

AML Training Server
===================

The second stage is the |aml| training server, responsible for creating trained |aml| models from the user-provided training examples.

Key components include:

- **Server Implementation**: Built using Python and Flask, leveraging the |aml| *Engine's* Python bindings.
- **Model Serialization**: The model structure is serialized to JSON and sent to the web application.
- **JavaScript Integration**: A JavaScript counterpart of the model is created for real-time predictions.
  For comparison algorithms, *TensorFlow.js* is used, allowing easy integration into Marcelle and enabling the user to compare |aml| results with various models.
  In our use case, we added a neural network that can be trained in-browser without additional components.

.. _amldashboard_real_time_prediction:

Real-time Prediction
====================

.. warning::

  This feature is only available when the dataset is ``Sensors``.

The third stage involves mapping user-defined gestures to sound patterns using real-time predictions based on the selected model.

This stage includes:

- **Real-time Predictions**: Utilizing the JavaScript model created from the |aml| server, the system maps gestures to sound patterns in real-time.
- **Sound Patterns**: For demonstration purposes, we used four pre-determined musical instruments to showcase the system's potential.
