.. include:: /rst/exports/roles.include

.. _demos_parallelize_aml_training_with_aml_ip:

####################################
Parallelize AML training with AML-IP
####################################

Background
==========

`AML-IP <https://aml-ip.readthedocs.io/en/latest/>`__ is a communications framework in charge of data exchange between Algebraic Machine Learning (AML) nodes through local or remote networks.
It is designed to allow non-experts users to create and manage a cluster of AML nodes to exploit the distributed and concurrent learning capabilities of AML.

The purpose of this demo is to show how to parallelize the training of an AML model using AML-IP nodes in the context of
the `Workload Distribution Scenario <https://aml-ip.readthedocs.io/en/latest/rst/user_manual/scenarios/workload_distribution.html#user-manual-scenarios-workload-distribution>`__.

The nodes involved in this scenario are Main Nodes and Computing Nodes.
By implementing these two nodes, users can deploy as many nodes of each kind as desired and check the behavior of a simulated AML-IP network running.

Prerequisites
=============

Before running this demo, ensure that :code:`AML-IP` is correctly installed using one of the following installation methods:

* `AML-IP on Linux <https://aml-ip.readthedocs.io/en/latest/rst/developer_manual/installation/sources/linux/linux.html>`__
* `AML-IP on Windows <https://aml-ip.readthedocs.io/en/latest/rst/developer_manual/installation/sources/windows/windows.html>`__
* `Docker image <https://aml-ip.readthedocs.io/en/latest/rst/installation/docker.html#docker-image>`

Once AML-IP packages are installed and built, import the libraries using the following command.

.. code-block:: bash

    source /AML-IP/install/setup.bash

Structure
=========

Running AML with AML-IP requires the following components:
* AML-IP Main Node with a custom Solution Listener
* AML-IP Computing Node with a custom Job Replier
* Correct preprocessing of the data
* A function in charge of the AML training process
* A function to process the results

Creating the Main Node
=======================

The Main Node is in charge of distributing the workload among the Computing Nodes.

Steps
*****

1. Import the necessary libraries.

.. code-block:: python

    import json
    import random

    from amlip_py.node.AsyncMainNode import AsyncMainNode, SolutionListener
    from amlip_py.types.JobDataType import JobDataType

    from py_utils.wait.IntWaitHandler import IntWaitHandler

.. note::
.. TODO :: Add the code ref to the section where loading the dataset is explained.

    The user should implement the loadDatasets function in the way that best suits their needs.
    In a future section, we provide an example of how to load the MNIST dataset.

    .. code-block:: python

        from loadDatasets import loadMNIST

2. Create global variables

.. code-block:: python

    # Global variables
    #  Domain ID
    DOMAIN_ID=2
    # Holds the solution data from the model training
    solution_data = None
    # IntWaitHandler object to manage waiting for training job completion
    waiter_job=IntWaitHandler(True)

3. Implement the custom SolutionListener class

.. code-block:: python

    def __init__(self):
        super().__init__() # Call the parent constructor

    def solution_received(
            self,
            solution,
            task_id,
            server_id):
        
        global solution_data
        if solution_data is None:
            solution_data = json.loads(solution.to_string())
        else:
            solution_data.update(json.loads(solution.to_string()))
            print('Solution received:', solution_data['0'])
        global waiter_jobç
        # Each time a solution is received, the waiter_job is increased
        waiter_job.increase()

4. Create the main routine

.. code-block:: python

    def main():
        """Execute maine routine."""
        # Create a waiter to avoid closing the main node before all jobs are finished
        global waiter_job
        # Initialize the waiter to 0
        waiter_job.set_value(0)
        global solution_data
        solution_data = None

* Create the Main Node object

.. code-block:: python

        print('Starting Async Main Node Py execution. Creating Node...')
        # Create the main node
        main_node = AsyncMainNode(
        'PyTestAsyncMainNode',
        listener=CustomSolutionListener(),
        domain=DOMAIN_ID)       

* Load and preprocess the data

.. code-block:: python

        # Load the dataset
        training_images, training_labels = loadMNIST('MNIST').load_training()
        # Number of parallel trainings to perform. The user can change this value to the desired number of parallel trainings
        # The number of parallel trainings should be less than the number of computing nodes
        nJobs = 2

        for i in range(0, nJobs):
        
            # Calculate data
            # Zip the two lists together to maintain correspondence
            zipped_data = list(zip(training_images.tolist(), training_labels.tolist()))
            # Take a random sample of the data
            num_items = len(zipped_data) // nJobs
            sampled_zipped_data = random.sample(zipped_data, num_items)
            # Unzip the sampled data back into separate lists
            sampled_data_images, sampled_data_labels = zip(*sampled_zipped_data)
            # Create job data
            job_data =JobDataType('x: ' + json.dumps(sampled_data_images) + ' y: ' + json.dumps(sampled_data_labels))
            # Send data to a remote Computing Node and waits for the solution
            task_id = main_node.request_job_solution(job_data)

        # Wait for all jobs to finish
        waiter_job.wait_equal(nJobs)

        print('All jobs finished. Stopping Async Main Node Py execution.')

5. Run the main routine

.. code-block:: python

    if __name__ == '__main__':
        main()

Creating the Computing Node
============================

The Computing Node is in charge of processing the data and training the AML model.

Steps
*****

1. Import the necessary libraries.

.. code-block:: python

    import json
    import signal

    from amlip_py.node.AsyncComputingNode import AsyncComputingNode, JobReplier
    from amlip_py.types.JobSolutionDataType import JobSolutionDataType

.. note::

    The user should implement the `train_alma` and `get_results` functions in the way that best suits their needs.
    In a future section, we provide an example of how to create these functions in a form for demonstration purposes.

    .. code-block:: python

        from AML_binary_classifier import train_alma, get_results

2. Create global variables

.. code-block:: python

    # Global variables
    # Domain ID
    DOMAIN_ID=2

3. Implement the custom JobReplier class

.. code-block:: python

    class CustomJobReplier(JobReplier):

        def process_job(
            self,
            job,
            task_id,
            client_id):

            data = job.to_string()

            # Find the indices of 'x: ' and ' y: ' in the data string
            x_index = data.find('x: ')
            y_index = data.find(' y: ')
            # Extract the substring between 'x: ' and ' y: ' to get the value of x
            x = json.loads(data[x_index + len('x: '):y_index])
            ## Extract the substring between ' y: ' and : to get the value of y
            y = json.loads(data[y_index + len(' y: '):])

            print('Received job, calling train_alma')

            # OPTIONAL: The user can change the values of the parameters
            #target_digit=int(args.targetClass)
            #size=int(args.imageSize)
            #iterations=int(args.iterations)
            #batch_size=int(args.batchSize)

            model = get_results(x, y, target_digit, size, iterations, batch_size)
            print(type(model))
            print('train_alma finished!')
            solution = JobSolutionDataType(json.dumps({task_id: model})) 
            return solution

4. Create the main routine

.. code-block:: python

    def main():
        """Execute main routine."""

        # Create node
        print('Starting Async Computing Node Py execution. Creating Node...')
        computing_node = AsyncComputingNode(
            'PyTestAsyncComputingNode',
            listener=CustomJobReplier(),
            domain=DOMAIN_ID)

        # Create job data
        print(f'Node created: {computing_node.get_id()}. '
              'Already processing jobs. Waiting SIGINT (C^)...')

        # Start node
        computing_node.run()

        # Wait for signal
        def handler(signum, frame):
            pass
        signal.signal(signal.SIGINT, handler)
        signal.pause()

        # Stop node
        computing_node.stop()

        print('Finishing Async Computing Node Py execution.')

5. Run the main routine

.. code-block:: python

    if __name__ == '__main__':
        main()