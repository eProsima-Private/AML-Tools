.. include:: /rst/exports/alias.include
.. include:: /rst/exports/roles.include

.. _tutorials_dashboard_aml_ip:

##########################################
Manage AML-IP nodes with the AML Dashboard
##########################################

Background
==========

The :term:`AML` Dashboard is a web-based tool that allows users to interact with the |aml| framework.

This tutorial guides you through the process of managing AML-IP nodes (creating, stopping and deleting) using the *AML Dashboard*.

Prerequisites
=============

Ensure you have installed the *AML Dashboard* using one of the following methods:

- :ref:`Linux Installation <amldashboard_linux>`
- :ref:`Docker Image Installation <amldashboard_docker>`

For more information, check the :ref:`AML Dashboard Interfaces <amldashboard_interfaces_aml_ip>` and :ref:`AML Dashboard Usage <amldashboard_usage_amlip>` sections.

Running the demo
================

To run the necessary components for managing AML-IP nodes using the |aml| Dashboard, follow these steps:

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

Manage AML-IP nodes
====================

To manage AML-IP nodes, in the |aml| Dashboard, go to the ``AML-IP`` tab.

Manage Agent Nodes
==================

Create an Agent Node
--------------------

To create an Agent Node (Client, Server or Repeater), follow these steps:

1. In the ``AML-IP`` tab, go to the ``Agent Node`` tab.

2. Specify the necessary parameters for the corresponding Agent Node creation.

.. warning:: 

      In UDP communication the internal and the external port must coincide.

3. Click on the ``Create`` button in the *Create Agent Node*.

4. Once the node is successfully created, the corresponding *Agent Node Status* will update to **Created !**.

.. note::

    Currently, each Agent Node can only be created once.

Stop and Delete an Agent Node
------------------------------

To stop an Agent Node, follow these steps:

1. In the ``AML-IP`` tab, go to the ``Agent Node`` tab.

2. Click on the ``Delete`` button in the *Delete Agent Node*.

3. Once the node is successfully deleted, the corresponding *Agent Node Status* will update to **Deleted !**.

.. raw:: html

   <video id=myVideo width=100% height=auto autoplay loop controls muted>
      <source src="../../_static/resources/tutorials/dashboard_amlip_agent.mp4">
      Your browser does not support the video tag.
   </video>

   <script>
      // Set the speed of the video once the page is loaded
      window.onload = function() {
         document.getElementById('myVideo').playbackRate = 1.0; // Set speed to 1.0x
      };
   </script>

Manage Computing Nodes
======================

Create a Computing Node
-----------------------

To create a Computing Node, follow these steps:

1. In the ``AML-IP`` tab, go to the ``Computing Node`` tab.

2. Click on the ``Create`` button in the *Computing Node*.

3. Once the node is successfully created, the *Computing Node Status* will update to **Created and running !**.

Stop a Computing node
---------------------

Computing nodes can be stopped without deleting them. This allows you to restart the node later when needed. To stop a Computing Node, follow these steps:

1. In the ``AML-IP`` tab, go to the ``Computing Node`` tab.

2. Indicate the ID of the node you want to stop.

3. Alternatively, if you want to stop all Computing nodes, in the *Indicate the ID of Computing Node to manage* section, write ``all``.

4. Click on the ``Stop`` button in the *Stop Computing Node*.

5. Once the node is successfully stopped, the corresponding *Computing Node Status* will update to **Stopped !**.

Run a Computing node
--------------------

To run a stopped Computing Node, follow these steps:

1. In the ``AML-IP`` tab, go to the ``Computing Node`` tab.

2. Indicate the ID of the node you want to run.

3. Alternatively, if you want to run all stopped Computing nodes, in the *Indicate the ID of Computing Node to manage* section, write ``all``.

4. Click on the ``Run`` button in the *Run Computing Node*.

5. Once the node is successfully running, the corresponding *Computing Node Status* will update to **Running !**.

Delete a Computing Node
-----------------------

To delete a Computing Node, follow these steps:

1. In the ``AML-IP`` tab, go to the ``Computing Node`` tab.

2. Indicate the ID of the node you want to delete.

3. Alternatively, if you want to delete all Computing nodes, in the *Indicate the ID of Computing Node to manage* section, write ``all``.

4. Click on the ``Stop and Delete`` button in the *Stop and Delete Computing Node*.

5. Once the node is successfully deleted, the corresponding *Computing Node Status* will update to **Deleted !**.

.. raw:: html

   <video id=myVideo width=100% height=auto autoplay loop controls muted>
      <source src="../../_static/resources/tutorials/dashboard_amlip_computing.mp4">
      Your browser does not support the video tag.
   </video>

   <script>
      // Set the speed of the video once the page is loaded
      window.onload = function() {
         document.getElementById('myVideo').playbackRate = 1.0; // Set speed to 1.0x
      };
   </script>

Manage Inference Nodes
======================

Create an Inference Node
------------------------

To create an Inference Node, follow these steps:

1. In the ``AML-IP`` tab, go to the ``Inference Node`` tab.

2. Click on the ``Create`` button in the *Inference Node*.

3. Once the node is successfully created, the *Inference Node Status* will update to **Created !**.

Stop an Inference node
---------------------

Inference nodes can be stopped without deleting them. This allows you to restart the node later when needed. To stop an Inference Node, follow these steps:

1. In the ``AML-IP`` tab, go to the ``Inference Node`` tab.

2. Indicate the ID of the node you want to stop.

3. Alternatively, if you want to stop all Inference nodes, in the *Indicate the ID of Inference Node to manage* section, write ``all``.

4. Click on the ``Stop`` button in the *Stop Inference Node*.

5. Once the node is successfully stopped, the corresponding *Inference Node Status* will update to **Stopped !**.

Run an Inference node
---------------------

To run a stopped Inference Node, follow these steps:

1. In the ``AML-IP`` tab, go to the ``Inference Node`` tab.

2. Indicate the ID of the node you want to run.

3. Alternatively, if you want to run all stopped Inference nodes, in the *Indicate the ID of Inference Node to manage* section, write ``all``.

4. Click on the ``Run`` button in the *Run Inference Node*.

5. Once the node is successfully running, the corresponding *Inference Node Status* will update to **Running !**.

Delete an Inference Node
------------------------

To delete an Inference Node, follow these steps:

1. In the ``AML-IP`` tab, go to the ``Inference Node`` tab.

2. Indicate the ID of the node you want to delete.

3. Alternatively, if you want to delete all Inference nodes, in the *Indicate the ID of Inference Node to manage* section, write ``all``.

4. Click on the ``Stop and Delete`` button in the *Stop and Delete Inference Node*.

5. Once the node is successfully deleted, the corresponding *Inference Node Status* will update to **Deleted !**.

.. raw:: html

   <video id=myVideo width=100% height=auto autoplay loop controls muted>
      <source src="../../_static/resources/tutorials/dashboard_amlip_inference.mp4">
      Your browser does not support the video tag.
   </video>

   <script>
      // Set the speed of the video once the page is loaded
      window.onload = function() {
         document.getElementById('myVideo').playbackRate = 1.0; // Set speed to 1.0x
      };
   </script>

Manage Sender Node
==================

Create a Sender Node
--------------------

To create a Sender Node, follow these steps:

1. In the ``AML-IP`` tab, go to the ``Sender Node`` tab.

2. Click on the ``Create`` button in the *Sender Node*.

3. Once the node is successfully created, the *Sender Node Status* will update to **Created !**.

.. note::

    Currently, a Sender Node can only be created once.


Delete a Sender Node
--------------------

To delete a Sender Node, follow these steps:

1. In the ``AML-IP`` tab, go to the ``Sender Node`` tab.

2. Click on the ``Delete`` button in the *Delete Sender Node*.

3. Once the node is successfully deleted, the corresponding *Sender Node Status* will update to **Deleted !**.


.. raw:: html

   <video id=myVideo width=100% height=auto autoplay loop controls muted>
      <source src="../../_static/resources/tutorials/dashboard_amlip_sender.mp4">
      Your browser does not support the video tag.
   </video>

   <script>
      // Set the speed of the video once the page is loaded
      window.onload = function() {
         document.getElementById('myVideo').playbackRate = 1.0; // Set speed to 1.0x
      };
   </script>