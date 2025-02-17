.. include:: /rst/exports/alias.include
.. include:: /rst/exports/roles.include

.. _amldashboard_docker:

#############
AML Dashboard
#############

.. todo::

    Change the Dockerfile to use the main branch when it is merged.

The AML Dashboard is composed of two services: a backend and a frontend, each with its own Docker container. 
These services are managed using docker-compose for ease of deployment.

Prerequisites
-------------

Ensure you have `Docker <https://docs.docker.com/get-started/get-docker/>`_ and `Docker Compose <https://docs.docker.com/compose/install/linux/>`_ installed on your machine.

Building and Running the Containers
-----------------------------------

To build and run the Docker containers, execute the following steps:

1. Create a working directory and navigate into it:

.. code-block:: bash

    mkdir AML-Dashboard
    cd AML-Dashboard

2. Download the required Dockerfiles and docker-compose.yml:

.. code-block:: bash

    wget https://raw.githubusercontent.com/eProsima-Private/AML-Dashboard/refs/heads/feature/add_dockerfile/Dockerfile_Frontend
    wget https://raw.githubusercontent.com/eProsima-Private/AML-Dashboard/refs/heads/feature/add_dockerfile/Dockerfile_Backend
    wget https://raw.githubusercontent.com/eProsima-Private/AML-Dashboard/refs/heads/feature/add_dockerfile/docker-compose.yml

3. Start the services using docker-compose:

.. code-block:: bash

    docker compose up -d

4. After the containers are built move your ``aml_engine`` folder from your machine to the docker backend.

.. code-block:: bash

    docker cp <path_to_aml_engine/aml_engine> aml-dashboard-amldashboard-backend-1:/AML-Dashboard/backend/

The AML Dashboard will be available at `<http://localhost:5173>`_.

5. To stop the services, execute the following command:

.. code-block:: bash

    docker compose down

AML-Dashboard Deployment
------------------------

The Docker Compose launches the following containers:

* `AML Dashboard Backend <https://raw.githubusercontent.com/eProsima-Private/AML-Dashboard/refs/heads/feature/add_dockerfile/Dockerfile_Backend>`_ is responsible for managing the AML Dashboard's server, 
  including the AML-IP nodes, processing the data and results.
  It is built on ``ubuntu:jammy`` and it installs essential system dependencies, including ``git``, ``cmake``, ``g++``, ``libasio-dev``, ``libssl-dev``, ``libyaml-cpp-dev``, ``swig``, and ``Miniconda``.
  The Miniconda environment, ``aml_env``, is created with ``Python 3.11`` and includes essential Python libraries such as ``Flask``, ``NumPy``, ``scikit-learn``, ``pandas``, ``tensorflow[and-cuda]``, and other scientific computing and machine learning dependencies.
  The backend also clones and builds AML-IP, which is used for interaction processing, by importing the necessary repositories and compiling the software with ``colcon``. 
  The backend source code is cloned from the AML-Dashboard repository, and once the container is up, it runs ``server.py`` within the activated ``aml_env`` environment and sources the necessary AML-IP dependencies.
  The backend container runs in host network mode to ensure direct communication with the frontend.

* `AML Dashboard Frontend <https://raw.githubusercontent.com/eProsima-Private/AML-Dashboard/refs/heads/feature/add_dockerfile/Dockerfile_Frontend>`_ serves the web-based interface of the AML Dashboard and interacts with the backend to retrieve and display data.
  It is also based on ``ubuntu:jammy`` and and provides the web interface for the AML Dashboard. Is installs essential system dependencies, including ``git``, ``nodejs``, and ``npm``.
  The frontend uses Node.js with dependencies managed through ``npm``.
  Once built, it runs the frontend interface using ``npm run dev``.
  It also runs in host network mode to facilitate seamless communication between services.
