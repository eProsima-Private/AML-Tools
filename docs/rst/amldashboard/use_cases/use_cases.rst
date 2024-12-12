.. include:: /rst/exports/alias.include
.. include:: /rst/exports/roles.include

.. _amldashboard_use_cases:

#########
Use Cases
#########

.. warning::

   The mentioned implementation is a work in progress and is not yet available in the current version of *AML Dashboard*.

*AML Dashboard* addresses two primary use cases, catering to different audiences and purposes:
creative professionals exploring sound variations in order to enhance creativity and create unique sound experiences;
and computer scientists exploring and developing new applications using |aml| needing a practical tool to to asses the efficiency of the |aml| algorithm.

.. _aml_sound_exploration: 

Exploring Sound Variations with *AML Dashboard*
===============================================

Emilie is a musician who uses *AML Dashboard* to experiment with different instruments and create new sound patterns for an upcoming project.
She uses the camera to record her hand gestures, which are projected as a skeleton on the screen.
By selecting different instruments from a drop-down menu, she records gestures such as guitar strumming, piano key presses, and drum movements.

Steps Emilie follows:

1. **Gesture Recording**: She moves her hands in front of the camera and records gestures for different instruments.

2. **Model Training**: She trains an AML model using the recorded gestures to generate sound patterns, and the training progress is shown by a loading bar.

3. **Sound Manipulation**: Emilie tests the system by repeating the gestures and listening to the sounds.
   The system allows her to manipulate tempo, pitch, and volume by varying her hand movements.

4. **Refinement**: Noticing difficulties with the generated results, she returns to the training page, deletes the images with the problematic gestures, records new ones, and retrains the model to improve the sound quality.

.. _aml_comparison_exploring_exploration: 

Exploring and Comparing the Potential of AML using *AML Dashboard*
=============================================================

Victor is a computer scientist exploring new machine learning approaches for his project.
He uses *AML Dashboard* to test and evaluate the potential of |aml| through a hands-on approach.

Steps Victor follows:

1. **Dataset Creation**: There are several options available: record hand gestures for different musical instruments, selecting from a drop-down menu and pressing the ``record`` button; select a standard dataset from the system or load a custom dataset.

2. **Model Training**: He trains the model and activates the evaluation mode to examine the confusion matrix and the atoms used in each class.

3. **Evaluation and Refinement**: Victor adds new data to each label, retrains the model, and evaluates the results.
   He investigates the classes and atoms triggered by varying the gestures, gaining a better understanding of *AML's* potential.
