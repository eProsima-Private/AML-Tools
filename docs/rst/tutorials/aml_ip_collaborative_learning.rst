.. include:: /rst/exports/alias.include
.. include:: /rst/exports/roles.include

.. _aml_ip_collaborative_learning:

#############################
AML-IP Collaborative Learning
#############################


Background
==========

This demo shows a `Collaborative Learning Scenario <https://aml-ip.readthedocs.io/en/latest/rst/user_manual/scenarios/collaborative_learning.html#user-manual-scenarios-collaborative-learning>`__ and the |amlip| nodes involved: `Model Manager Receiver Node <https://aml-ip.readthedocs.io/en/latest/rst/user_manual/nodes/model_manager_receiver.html#user-manual-nodes-model-receiver>`__ and `Model Manager Sender Node <https://aml-ip.readthedocs.io/en/latest/rst/user_manual/nodes/model_manager_sender.html#user-manual-nodes-model-sender>`__.
With these 2 nodes implemented, the user can deploy as many nodes of each kind as desired and check the behavior of a simulated |amlip| network running.
They are implemented in Python to prove the communication between the 2 implementations.

The purpose of the demo is to show how a *Sender* and a *Receiver* node can communicate.
The *Receiver* node awaits model statistics from the *Sender*.
Since the *Sender* doesn't have a real *AML Engine*, it sends the model statistics as a string.
Upon receiving the statistics, the *Receiver* sends a model request, also as a string since it doesn't have an *AML Engine*.
Then, the *Sender* converts the received model request to uppercase and sends it back as a model reply.

.. figure:: /rst/figures/tutorials/collaborative_demo.png
    :align: center
    :width: 80%

Prerequisites
=============

Before running this demo, ensure that :code:`AML-IP` is correctly installed using one of the following installation methods:

* `AML-IP on Linux <https://aml-ip.readthedocs.io/en/latest/rst/installation/linux.html#aml-ip-on-linux>`__
* `AML-IP on Windows <https://aml-ip.readthedocs.io/en/latest/rst/installation/windows.html#aml-ip-on-windows>`__
* `Docker image <https://aml-ip.readthedocs.io/en/latest/rst/installation/docker.html#docker-image>`__

Building the demo
=================

If the demo package is not compiled, please refer to `Build demos <https://aml-ip.readthedocs.io/en/latest/rst/developer_manual/installation/sources/linux/linux_colcon.html#developer-manual-installation-sources-linux-colcon-demos>`__ or run the command below.

.. code-block:: bash

    colcon build --packages-up-to amlip_collaborative_learning_demo

Once AML-IP packages are installed and built, import the libraries using the following command.

.. code-block:: bash

    source install/setup.bash

Explaining the demo
===================

In this section, we will delve into the details of the demo and how it works.

Model Manager Receiver Node
---------------------------

This is the Python code for the `Model Manager Receiver Node <https://aml-ip.readthedocs.io/en/latest/rst/user_manual/nodes/model_manager_receiver.html#user-manual-nodes-model-receiver>`__ application.
It does not use real *AML Models*, but strings.
It is implemented in |python| using :code:`amlip_py` API.

This code can be found `here <https://github.com/eProsima/AML-IP/blob/main/amlip_demo_nodes/amlip_collaborative_learning_demo/amlip_collaborative_learning_demo/model_receiver_custom.py>`__.

The next block includes the Python header files that allow the use of the AML-IP Python API.

.. code-block:: python

    from amlip_py.node.ModelManagerReceiverNode import ModelManagerReceiverNode, ModelListener
    from amlip_py.types.AmlipIdDataType import AmlipIdDataType
    from amlip_py.types.ModelReplyDataType import ModelReplyDataType
    from amlip_py.types.ModelRequestDataType import ModelRequestDataType
    from amlip_py.types.ModelStatisticsDataType import ModelStatisticsDataType

Let's continue explaining the global variables.

``DOMAIN_ID`` variable isolates the execution within a specific domain. Nodes with the same domain ID can communicate with each other.

.. code-block:: python

    DOMAIN_ID = 166

``waiter`` is a ``WaitHandler`` that waits on a boolean value.
Whenever this value is ``True``, threads awake.
Whenever it is ``False``, threads wait.

.. code-block:: python

    waiter = BooleanWaitHandler(True, False)

The ``CustomModelListener`` class listens to `Model Statistics Data Type <https://aml-ip.readthedocs.io/en/latest/rst/user_manual/scenarios/collaborative_learning.html#model-statistics-data-type>`__ and `Model Reply Data Type <https://aml-ip.readthedocs.io/en/latest/rst/user_manual/scenarios/collaborative_learning.html#model-reply-data-type>`__ messages received from a `Model Manager Sender Node <https://aml-ip.readthedocs.io/en/latest/rst/user_manual/nodes/model_manager_sender.html#model-manager-sender-node>`__.
This class is supposed to be implemented by the user in order to process the messages received from other nodes in the network.

.. code-block:: python

    class CustomModelListener(ModelListener):

        def statistics_received(
                self,
                statistics: ModelStatisticsDataType):

            print(f'Statistics received: {statistics.to_string()}')

            # Store the server id of the statistics
            self.server_id = statistics.server_id()

            waiter.open()

        def model_received(
                self,
                model: ModelReplyDataType) -> bool:

            print(f'Model reply received from server\n'
                  f' solution: {model.to_string()}')

            return True

The `main` function orchestrates the execution of the Model Manager Receiver node.
It creates an instance of the `ModelManagerReceiverNode` and starts its execution with the specified listener.

.. code-block:: python

    def main():
        """Execute main routine."""

        # Create request
        data = ModelRequestDataType('MobileNet V1')

        id = AmlipIdDataType('ModelManagerReceiver')
        id.set_id([15, 25, 35, 45])

        # Create node
        print('Starting Manual Test Model Manager Receiver Node Py execution. Creating Node...')
        model_receiver_node = ModelManagerReceiverNode(
            id=id,
            data=data,
            domain=DOMAIN_ID)

        print(f'Node created: {model_receiver_node.get_id()}. '
              'Already processing models.')

        model_receiver_node.start(
            listener=CustomModelListener())

After starting the node, it waits for statistics to arrive from the `Model Manager Sender Node <https://aml-ip.readthedocs.io/en/latest/rst/user_manual/nodes/model_manager_sender.html#model-manager-sender-node>`__.

.. code-block:: python

        # Wait statistics
        waiter.wait()

Then, it requests a model from the `Model Manager Sender Node <https://aml-ip.readthedocs.io/en/latest/rst/user_manual/nodes/model_manager_sender.html#model-manager-sender-node>`__ using the received server ID.

.. code-block:: python

        # Request model
        model_receiver_node.request_model(model_receiver_node.listener_.server_id)

Finally, the node stops.

.. code-block:: python

    model_receiver_node.stop()

Model Manager Sender Node
-------------------------

This is the Python code for the `Model Manager Sender Node <https://aml-ip.readthedocs.io/en/latest/rst/user_manual/nodes/model_manager_sender.html#model-manager-sender-node>`__ application.
It does not use real *AML Models*, but strings.
It does not have a real *AML Engine* but instead the calculation is an *upper-case* conversion of the string received.
It is implemented in |python| using :code:`amlip_py` API.

This code can be found `here <https://github.com/eProsima/AML-IP/blob/main/amlip_demo_nodes/amlip_collaborative_learning_demo/amlip_collaborative_learning_demo/model_sender_custom.py>`__.

The following block includes the Python header files necessary for using the AML-IP Python API.

.. code-block:: python

    from amlip_py.node.ModelManagerSenderNode import ModelManagerSenderNode, ModelReplier
    from amlip_py.types.AmlipIdDataType import AmlipIdDataType
    from amlip_py.types.ModelReplyDataType import ModelReplyDataType
    from amlip_py.types.ModelRequestDataType import ModelRequestDataType

Let's continue explaining the global variables.

``DOMAIN_ID`` isolates the execution within a specific domain.
Nodes with the same domain ID can communicate with each other.

.. code-block:: python

    DOMAIN_ID = 166

``waiter`` is a ``WaitHandler`` that waits on a boolean value.
Whenever this value is ``True``, threads awake.
Whenever it is ``False``, threads wait.

.. code-block:: python

    waiter = BooleanWaitHandler(True, False)

The ``CustomModelReplier`` class listens to `Model Request Data Type <https://aml-ip.readthedocs.io/en/latest/rst/user_manual/scenarios/collaborative_learning.html#model-request-data-type>`__ request messages received from a `Model Manager Receiver Node <https://aml-ip.readthedocs.io/en/latest/rst/user_manual/nodes/model_manager_receiver.html#user-manual-nodes-model-receiver>`__.
This class is supposed to be implemented by the user in order to process the messages.

.. code-block:: python

    class CustomModelReplier(ModelReplier):

        def fetch_model(
                self,
                request: ModelRequestDataType) -> ModelReplyDataType:

            reply = ModelReplyDataType(request.to_string().upper())

            print(f'Model request received from client\n'
                  f' request: {request.to_string()}\n'
                  f' reply: {reply.to_string()}')

            waiter.open()

            return reply

The `main` function orchestrates the execution of the Model Manager Sender node.
It creates an instance of `ModelManagerSenderNode`.

.. code-block:: python

    def main():
        """Execute main routine."""

        id = AmlipIdDataType('ModelManagerSender')
        id.set_id([10, 20, 30, 40])

        # Create node
        print('Starting Manual Test Model Manager Sender Node Py execution. Creating Node...')
        model_sender_node = ModelManagerSenderNode(
            id=id,
            domain=DOMAIN_ID)

After starting the node, it publishes statistics using the ``publish_statistics()`` function, which fills a `Model Statistics Data Type <https://aml-ip.readthedocs.io/en/latest/rst/user_manual/scenarios/collaborative_learning.html#model-statistics-data-type>`__  and publishes it.

.. code-block:: python

        model_sender_node.publish_statistics(
            'ModelManagerSenderStatistics',
            'hello world')

Then we start the node execution, passing the previously defined ``CustomModelReplier()`` class, which is responsible for managing the request received.

.. code-block:: python

        model_sender_node.start(
            listener=CustomModelReplier())

Waits for the response model to be sent to the `Model Manager Receiver Node <https://aml-ip.readthedocs.io/en/latest/rst/user_manual/nodes/model_manager_receiver.html#user-manual-nodes-model-receiver>`__.

.. code-block:: python

        # Wait for the solution to be sent
        waiter.wait()

Finally, it stops and closes the node.

.. code-block:: python

        model_sender_node.stop()

Running the demo
================

This demo runs the implemented nodes in `amlip_demo_nodes/amlip_collaborative_learning_demo <https://github.com/eProsima/AML-IP/tree/main/amlip_demo_nodes/amlip_collaborative_learning_demo>`__.

Run Model Manager Receiver Node
-------------------------------

Run the following command:

.. code-block:: bash

    # Source colcon installation
    source install/setup.bash

    # To execute Model Manager Receiver Node
    cd ~/AML-IP-ws/src/AML-IP/amlip_demo_nodes/amlip_collaborative_learning_demo/amlip_collaborative_learning_demo
    python3 model_receiver_custom.py

The expected output is the following:

.. code-block:: bash

    Starting Manual Test Model Manager Receiver Node Py execution. Creating Node...
    Node created: ModelManagerReceiver.0f.19.23.2d. Already processing models.
    Model reply received from server
    solution: MOBILENET V1
    Finishing Manual Test Model Manager Receiver Node Py execution.


Run Model Manager Sender Node
-----------------------------

Run the following command to answer before closing:

.. code-block:: bash

    # Source colcon installation
    source install/setup.bash

    # To execute Model Manager Sender Node
    cd ~/AML-IP-ws/src/AML-IP/amlip_demo_nodes/amlip_collaborative_learning_demo/amlip_collaborative_learning_demo
    python3 model_sender_custom.py

This execution expects an output similar to the one shown below:

.. code-block:: bash

    Starting Manual Test Model Manager Sender Node Py execution. Creating Node...
    Node created: ModelManagerSender.0a.14.1e.28. Already processing models.
    Model request received from client
    model: MobileNet V1
    solution: MOBILENET V1
    Finishing Manual Test Model Manager Sender Node Py execution.
