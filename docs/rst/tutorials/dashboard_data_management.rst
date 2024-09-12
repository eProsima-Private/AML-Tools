.. include:: /rst/exports/alias.include
.. include:: /rst/exports/roles.include

.. _tutorials_dashboard_train:

##################################
Manage data with the AML Dashboard
##################################

Background
==========

The :term:`AML` Dashboard is a web-based tool that allows users to interact with the |aml| framework.

This tutorial showcases the data collection step of an |aml| model training process using the *AML Dashboard*.

Prerequisites
=============

Ensure you have installed the *AML Dashboard* using one of the following methods:

- :ref:`Linux Installation <amldashboard_linux>`
- :ref:`Docker Image Installation <amldashboard_docker>`

For more information, check the :ref:`AML Dashboard Interfaces <amldashboard_interfaces_data_collection>` and :ref:`AML Dashboard Usage <amldashboard_usage_data_management>` sections.

Running the demo
================

To run the necessary components for collecting data using the |aml| Dashboard, follow these steps:

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

Start the AML Dashboard
-----------------------

1. Navigate to the ``frontend/aml_dashboard`` directory.

.. code-block:: bash

   cd frontend/aml_dashboard

2. Start the |aml| Dashboard:

.. code-block:: bash

   npm run dev

3. Access the dashboard at `http://localhost:5173/ <http://localhost:5173/>`__.

Collecting data
===============

To collect data using the |aml| Dashboard, follow these steps:

1. Navigate to the ``Data Management`` tab on the |aml| Dashboard.

2. In the *webcam* section, toggle the ``activate video`` button to enable the webcam.

3. Introduce a label for the class that will be recorded in the *Instance label* section.

4. Press the ``Hold to record instances`` button in the *Capture instances to the training set* section to start recording data.

.. raw:: html

   <video id=myVideo width=100% height=auto autoplay loop controls muted>
      <source src="../../_static/resources/tutorials/dashboard_data_management.mp4">
      Your browser does not support the video tag.
   </video>

   <script>
      // Set the speed of the video once the page is loaded
      window.onload = function() {
         document.getElementById('myVideo').playbackRate = 1.3; // Set speed to 1.3x
      };
   </script>
