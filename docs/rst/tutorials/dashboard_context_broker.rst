.. include:: /rst/exports/alias.include
.. include:: /rst/exports/roles.include

.. _tutorials_dashboard_context_broker:

######################################################
Send data to the Context Broker with the AML Dashboard
######################################################

Background
==========

The :term:`AML` Dashboard is a web-based tool that allows users to interact with the |aml| framework.

This tutorial guides you through the process of sending data to the Context Broker and retrieving inferences using the *AML Dashboard*.

.. figure:: /rst/figures/tutorials/context_broker_dashboard.png
    :align: center
    :width: 100%

Prerequisites
=============

Ensure you have installed the *AML Dashboard* using one of the following methods:

- :ref:`Linux Installation <amldashboard_linux>`
- :ref:`Docker Image Installation <amldashboard_docker>`

For more information, check the :ref:`AML Dashboard Interfaces <amldashboard_interfaces_context_broker>` and :ref:`AML Dashboard Usage <amldashboard_usage_context_broker>` sections.

Running the demo
================

To run the necessary components for interacting with the Context Broker using the |aml| Dashboard, follow these steps:

Start the backend server
------------------------

To begin, you need to launch the backend server:

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

Once the backend server is running, start the AML Dashboard frontend:

1. Navigate to the ``frontend/aml_dashboard`` directory.

.. code-block:: bash

   cd frontend/aml_dashboard

2. Start the |aml| Dashboard:

.. code-block:: bash

   npm run dev

3. Access the dashboard at `http://localhost:5173/ <http://localhost:5173/>`__.

Start the Context Broker
------------------------

To start the Context Broker, follow the instructions in `this document <https://github.com/telefonicaid/fiware-orion/blob/master/docker/README.md>`__.

Send data to the Context Broker
===============================

Create a Fiware Node
--------------------

To create a Fiware Node, follow these steps:

1. In the |aml| Dashboard, go to the ``Context Broker`` tab.

2. Specify the necessary parameters for the Fiware Node creation, including the Context Broker entity ID and attributes.

3. Click on the ``Create`` button in the *Fiware Node*.

4. Once the node is successfully created, the *Fiware Node Status* will update to **Created !**.

Upload data
-----------

To send data to the Context Broker, follow these steps:

1. Upload an image file from your computer by clicking on the ``Upload a file`` button and selecting an image.

2. After uploading, click on the ``Post data`` button in the *Context Broker Data* to send the image to the Context Broker.

3. Once the data is sent, the status will change to **Sended !** in the *Data Status*.

Receive the solution
====================

Start an Inference Node
-----------------------

1. Navigate to the ``backend`` directory.

.. code-block:: bash

   cd backend

2. Load the |amlip| environment.

.. code-block:: bash

   source /AML-IP/install/setup.bash

3. Start the Inference Node:

.. code-block:: bash

   python3 inference.py

Retrieve the solution
---------------------

1. The inference result (solution) will be displayed in the *Context Broker Solution* section.

2. The *Solution Status* will change to **Solution received !** to confirm that the inference has been successfully retrieved.

.. raw:: html

   <video id=myVideo width=100% height=auto autoplay loop controls muted>
      <source src="../../_static/resources/tutorials/dashboard_inference.mp4">
      Your browser does not support the video tag.
   </video>

   <script>
      // Set the speed of the video once the page is loaded
      window.onload = function() {
         document.getElementById('myVideo').playbackRate = 1.0; // Set speed to 1.0x
      };
   </script>
