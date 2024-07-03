.. include:: /rst/exports/alias.include
.. include:: /rst/exports/roles.include

.. _amlip_user_manual:

###########
User Manual
###########

.. _amlip_scenarios:

Scenarios
=========

The |amlip| framework is divided in different **scenarios** or **use cases** that allow it to exploit all the capabilities :term:`AML` has to offer.
These scenarios work independently of each other and make sense separately, but can be seamlessly combined to create a more complex network.
Each of the scenarios rely on a different set of **Nodes** that perform the different actions required.

For more infromation, check the AML-IP Scenarios sections:

* `Monitor Network State Scenario <https://aml-ip.readthedocs.io/en/latest/rst/user_manual/scenarios/monitor_state.html>`__: performs monitoring, analysis and debugging of the network.
  The main node in this scenario is the Status Node.
* `Workload Distribution Scenario <https://aml-ip.readthedocs.io/en/latest/rst/user_manual/scenarios/workload_distribution.html>`__: distributes high-computation tasks, specifically training data-sets for an :term:`AML` model, across remote nodes using `MultiService over DDS <https://aml-ip.readthedocs.io/en/latest/rst/developer_manual/protocols/protocols.html#multiservice-over-dds>`__ communication.
  Tasks are divided into *Jobs*, which are processed by Computing Nodes to parallelize the workload, freeing the Main Node to perform other tasks.
* `Collaborative Learning Scenario <https://aml-ip.readthedocs.io/en/latest/rst/user_manual/scenarios/collaborative_learning.html>`__: involves Model Manager Receiver and Sender nodes sharing locally obtained models without exchanging private datasets.
  Using `RPC over DDS <https://aml-ip.readthedocs.io/en/latest/rst/developer_manual/protocols/protocols.html#rpc-over-dds>`__ communication, Receiver Nodes request models based on published statistics from Sender Nodes, aiming to develop more complex and accurate models.
* `Distributed Inference Scenario <https://aml-ip.readthedocs.io/en/latest/rst/user_manual/scenarios/distributed_inference.html>`__: distributes large datasets to remote Inference Nodes for parallel processing, ensuring other critical tasks on the main device are not blocked.
  Using `MultiService over DDS <https://aml-ip.readthedocs.io/en/latest/rst/developer_manual/protocols/protocols.html#multiservice-over-dds>`__, data is efficiently published and distributed, optimizing system performance.
  Inferences are performed on Inference Nodes and results are sent back to Edge Nodes.

.. _amlip_nodes:

Nodes
=====

An |amlip| network is divided in independent stand-alone individuals named :term:`Nodes <Node>`.
A Node, understood as a software piece that performs one or multiple :term:`Actions <Action>` in a auto-managing way, does not require external orchestration neither a central point of computation.
These actions can be local actions such as calculations, data process, algorithm executions, etc., or communication actions as send messages, receive data, wait for data or specific status, etc.
Each Node belongs to one and only one :term:`Scenario`.

There are different ways to run or to work with a Node.
Some of them are applications that can be executed and perform a fixed action.
Others, however, require a user interaction as specifying the action such Node must perform depending on its status and the data received.
In this last case, the Nodes are programming *Objects* that can be instantiated and customized regarding the action that must be performed.

For more information, check the AML-IP Nodes sections:

* `Agent Node <https://aml-ip.readthedocs.io/en/latest/rst/user_manual/nodes/agent.html>`__: uses the |eddsrouter| to connect distributed :term:`DDS` networks, enabling communication between :term:`DDS` entities across different geographic locations as if on the same network.
  It bridges local |amlip| clusters with the broader network over :term:`WAN`\s, centralizing :term:`WAN` discovery and communication.
  The node supports three types: Client Node (connects to a server), Server Node (waits for client connections), and Repeater Node (forwards messages across :term:`LAN`\s).
* `Status Node <https://aml-ip.readthedocs.io/en/latest/rst/user_manual/nodes/status.html>`__: subscribes to the Status Topic, receiving status data from all other nodes in the network, and executing a user-defined callback function for each message.
  It is the main component of the Monitor Network State Scenario.
  Users can start and stop this node using :code:`process_status_async` and :code:`stop_processing` methods, respectively.
* `Main Node <https://aml-ip.readthedocs.io/en/latest/rst/user_manual/nodes/main.html>`__: participates in the Workload Distribution Scenario by sending serialized Job Data Types to remote Computing Nodes and receiving solutions as Job Solution Data Types.
  It operates synchronously or asynchronously: in synchronous mode, it waits for each job to complete before sending the next, using :code:`request_job_solution` to handle each task sequentially.
  In asynchronous mode, it employs a callback or listener to process solutions as they arrive, enabling parallel task execution without blocking.
* `Computing Node <https://aml-ip.readthedocs.io/en/latest/rst/user_manual/nodes/computing.html>`__: acts as a server in the Workload Distribution Scenario, receiving serialized Job Data Types from Main Nodes and processing them to produce Job Solution Data Types.
  It operates synchronously or asynchronously: in synchronous mode, it waits for each job to arrive and completes processing before handling the next task, using :code:`request_job_solution` to initiate and manage tasks sequentially.
  In asynchronous mode, it employs a callback or listener to handle tasks concurrently, allowing for parallel processing and efficient resource utilization.
* `Edge Node <https://aml-ip.readthedocs.io/en/latest/rst/user_manual/nodes/edge.html>`__: facilitates the sending of data, serialized as Inference Data Type, to remote Inference Nodes for processing.
  It receives results as Inference Solution Data Types.
  Operating synchronously or asynchronously, in synchronous mode it waits for each inference to complete before sending the next data batch, using :code:`request_inference` to manage tasks sequentially.
  Asynchronous operation employs callbacks or listeners to handle multiple inferences concurrently, optimizing throughput and responsiveness in distributed inference scenarios.
* `Inference Node <https://aml-ip.readthedocs.io/en/latest/rst/user_manual/nodes/inference.html>`__: functions as a server in the distributed inference process, awaiting serialized data in the form of Inference Data Types from Edge Nodes.
  It calculates the inference based on the received data and returns the result as Inference Solution Data Types.
  In synchronous mode, it handles tasks sequentially using :code:`process_inference` to wait for and process each inference request.
  Asynchronous operation utilizes callbacks or listeners to process multiple requests concurrently, optimizing performance in distributed computing environments.
* `Model Manager Receiver Node <https://aml-ip.readthedocs.io/en/latest/rst/user_manual/nodes/model_manager_receiver.html>`__: acts as an active client that interacts with Model Manager Sender Nodes.
  It receives statistics about available models via :code:`statistics_received`, then sends requests for specific models using :code:`request_model`.
  Once a requested model, serialized as Model Reply Data Type, arrives, it is processed by :code:`model_received`.
  This node facilitates collaborative learning by enabling efficient model sharing across distributed networks, enhancing model accuracy and complexity without sharing private training datasets.
* `Model Manager Sender Node <https://aml-ip.readthedocs.io/en/latest/rst/user_manual/nodes/model_manager_sender.html>`__: acting as a passive server that manages and distributes models.
  It sends out statistics about the models it manages using :code:`publish_statistics`, then waits for incoming requests for specific models serialized as Model Request Data Type.
  Upon receiving a request, it executes a user-defined callback function :code:`fetch_model` to generate and return the requested model as Model Reply Data Type.
  This node facilitates collaborative model sharing across distributed systems, enabling efficient and secure model exchange without sharing underlying training data.

.. _amlip_tools:

Tools
=====

Agent Tool
----------

This tool launches an `Agent Node <https://aml-ip.readthedocs.io/en/latest/rst/user_manual/nodes/agent.html>`__, which is the node in charge of communicating a local node or |amlip| cluster with the rest of the network in :term:`WAN`\s.
It centralizes the :term:`WAN` discovery and communication, i.e. it is the bridge for all the nodes in their :term:`LAN`\s with the rest of the |amlip| components.

For more information, check the `AML-IP Agent tool section <https://aml-ip.readthedocs.io/en/latest/rst/user_manual/tools/agent.html>`__.
