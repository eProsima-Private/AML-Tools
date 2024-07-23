.. include:: /rst/exports/alias.include
.. include:: /rst/exports/roles.include

.. _amldashboard_use_cases:

#########
Use Cases
#########

*AML Dashboard* addresses two primary use cases, catering to different audiences and purposes: creative professionals exploring sound variations and computer scientists exploring and developing new applications using |aml|.

Exploring Sound Variations with *AML Dashboard*
===========================================

Emilie is a musician who uses *AML Dashboard* to experiment with different instruments and create new sound patterns for an upcoming project.
She uses the camera to record her hand gestures, which are projected as a skeleton on the screen.
By selecting different instruments from a drop-down menu, she records gestures such as guitar strumming, piano key presses, and drum movements.

Steps Emilie follows:

1. **Gesture Recording**: She moves her hands in front of the camera and records gestures for different instruments.

2. **Model Training**: She selects ``train`` to use these gestures to generate sound patterns, and a loading bar shows the training progress.

3. **Sound Manipulation**: Emilie tests the system by repeating the gestures and listening to the sounds.
   The system allows her to manipulate tempo, pitch, and volume by varying her hand movements.

4. **Refinement**: Noticing difficulties with her piano gesture, she returns to the training page, deletes the problematic images, records new gestures, and retrains the model to improve the sound quality.

Exploring and Comparing the Potential of AML using *AML Dashboard*
=============================================================

Victor is a computer scientist exploring new machine learning approaches for his project.
He uses *AML Dashboard* to test and evaluate the potential of |aml| through a hands-on approach similar to Emilie's.

Steps Victor follows:

1. **Gesture Recording**: He uses the camera to record hand gestures for different musical instruments, selecting from a drop-down menu and pressing the ``record`` button.

2. **Model Training**: He trains the model and activates the evaluation mode to examine the confusion matrix and the atoms used in each class.

3. **Evaluation and Refinement**: Victor adds new recordings to each label, retrains the model, and evaluates the results.
   He investigates the classes and atoms triggered by varying the gestures, gaining a better understanding of *AML's* potential.
