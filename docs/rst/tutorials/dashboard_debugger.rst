.. include:: /rst/exports/alias.include
.. include:: /rst/exports/roles.include

.. _tutorials_dashboard_debugger:

##############################################
Debug an AML-IP network with the AML Dashboard
##############################################

Background
==========

The :term:`AML` Dashboard is a web-based tool that allows users to interact with the |aml| framework.

This tutorial showcases the debugging process of an |amlip| network using the *AML Dashboard*.

.. figure:: /rst/figures/tutorials/debugger_dashboard.png
    :align: center
    :width: 100%

Prerequisites
=============

Ensure you have installed the *AML Dashboard* using one of the following methods:

- :ref:`Linux Installation <amldashboard_linux>`
- :ref:`Docker Image Installation <amldashboard_docker>`

For more information, check the :ref:`AML Dashboard Interfaces <amldashboard_interfaces_debugging>` and :ref:`AML Dashboard Usage <amldashboard_usage_debugging>` sections.

Running the demo
================

To run the necessary components for debugging an |amlip| network using the |aml| Dashboard, follow these steps:

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

Debugging the AML-IP network
============================

To debug an |amlip| network:

1. Navigate to the ``Status`` tab on the |aml| Dashboard.

The ``Status`` tab provides a detailed overview of all active nodes within the |amlip| network, automatically refreshing every second to offer real-time updates.

In this tab, you can confirm whether all expected nodes are properly connected and operating as intended.

If the table shows no nodes, this typically indicates that the backend server or the individual nodes have not been correctly initialized.
Ensure that you have followed the setup instructions provided earlier.

By default, the backend server starts with the following three nodes:

* `Main Node <https://aml-ip.readthedocs.io/en/latest/rst/user_manual/nodes/main.html>`__
* `Model Manager Receiver Node <https://aml-ip.readthedocs.io/en/latest/rst/user_manual/nodes/model_manager_receiver.html>`__
* `Edge Node <https://aml-ip.readthedocs.io/en/latest/rst/user_manual/nodes/edge.html>`__

If no modifications have been made, these three nodes should be visible in the table once the backend is running.

.. raw:: html

   <video id=myVideo width=100% height=auto autoplay loop controls muted>
      <source src="../../_static/resources/tutorials/dashboard_status.mp4">
      Your browser does not support the video tag.
   </video>

   <script>
      // Set the speed of the video once the page is loaded
      window.onload = function() {
         document.getElementById('myVideo').playbackRate = 1.0; // Set speed to 1.0x
      };
   </script>
