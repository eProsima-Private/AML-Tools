.. include:: /rst/exports/alias.include
.. include:: /rst/exports/roles.include

.. _amldashboard_specification:

#############
AML Dashboard
#############

<<<<<<< HEAD
The *AML Dashboard* serves as a user-friendly tool for training, evaluating, and applying |aml| models to numerous classification problems, including expressive gestures in music exploration.
=======
The *AML Dashboard* serves as a user-friendly tool for training, evaluating, and applying |aml| models to several datasets.
>>>>>>> ef01f98 (Update amldashboard documentation to include changes)
Built upon the `Marcelle <https://marcelle.dev/>`__ framework, the dashboard offers standard interaction :term:`GUI`\s and the ability to create custom interactive widgets compatible with Marcelle's structure.

The primary goal of the *AML Dashboard* is to enable users to:

1. Collect personal gesture data or load existing datasets.
2. Train classifiers using the *AML Engine*.
3. Compare the performance of |aml| models with other :term:`ML` approaches.

To achieve this, the *AML Dashboard* integrates four main interfaces:

* **Dataset Interface**: Allows users to collect data through user-defined input gestures.
* **Training Interface**: Facilitates the training of |aml| models based on loaded datasets.
* **Model Exploration Interface**: Enables users to explore and compare the capabilities of |aml| models with other :term:`ML` approaches.
* **Real Time Exploration Interface**: Applies the trained |aml| algorithm in real-time. This feature is only available when the dataset chosen contains gesture data. It enables users to explore new sound patterns using personal gestures.

.. toctree::
   :maxdepth: 1
   :hidden:

   /rst/amldashboard/specification/implementation
