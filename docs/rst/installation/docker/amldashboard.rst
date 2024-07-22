.. include:: /rst/exports/alias.include
.. include:: /rst/exports/roles.include

.. _amldashboard_docker:

#############
AML Dashboard
#############

.. todo::

    Change the Dockerfile to use the main branch when it is merged.

To build the Docker image using the provided `Dockerfile <https://github.com/eProsima-Private/AML-Dashboard/blob/feature/dfki_demo_amlip/Dockerfile>`, execute the following command:

.. code-block:: bash

    docker build -t amldashboard --no-cache -f Dockerfile .

Run the docker container executing the following command:

.. code-block:: bash

    docker run -it \
        --net=host \
        --ipc=host \
        --privileged \
        amldashboard
