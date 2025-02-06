.. include:: /rst/exports/alias.include
.. include:: /rst/exports/roles.include

.. _amldashboard_linux:

#############
AML Dashboard
#############

To get started with *AML Dashboard*, follow these steps.

Clone the repository using the following command:

.. code-block:: bash

    git clone https://github.com/eProsima-Private/AML-Dashboard.git

After cloning the repository, you must manually place the ``aml_engine`` inside the ``backend`` folder of the `AML Dashboard`.

.. note::
    The ``aml_engine`` is not included in the repository and must be obtained separately.
    Please refer to the section :ref:`Get access to AML Toolkit <get_access_toolkit>` for instructions on how to request access to the `AML Engine`.

Requirements
------------

If |amlip| is not already installed in your system, follow the installation instructions provided `here <https://aml-ip.readthedocs.io/en/latest/rst/installation/linux.html>`__.

Python dependencies
^^^^^^^^^^^^^^^^^^^

Ensure you have **Python3.11** installed together with the packages listed in the `requirements.txt <https://github.com/eProsima-Private/AML-Dashboard/main/requirements.txt>`__ file. If not, install them using the following commands:

.. code-block:: bash

<<<<<<< HEAD
    python3 -m venv amlip-venv
    source amlip-venv/bin/activate
=======
    python3 -m venv aml-ip-venv
    source aml-ip-venv/bin/activate
>>>>>>> 9d5b802 (Add some fixes to documentation)
    wget https://raw.githubusercontent.com/eProsima-Private/AML-Dashboard/main/requirements.txt
    pip3 install -r requirements.txt
    pip install tensorflow[and-cuda]

.. note::

    `pipx <https://pipx.pypa.io/stable/>`__ can also be used for users who prefer that as an alternative for managing Python packages in isolated environments.

Context Broker
^^^^^^^^^^^^^^^
Finally, ensure that FIWARE Context Broker is correctly installed, following the steps provided `here <https://github.com/telefonicaid/fiware-orion/blob/master/docker/README.md#1-the-fastest-way>`__.

npm and nodejs
^^^^^^^^^^^^^^

Ensure you have **npm (8.5.1)** and **nodejs (v12.22.9)** installed.
If not, install them using the following command:

.. code-block:: bash

    sudo apt install -y npm nodejs

Verify the installed versions using:

.. code-block:: bash

    npm -v
    node -v

Frontend Dependencies
^^^^^^^^^^^^^^^^^^^^^

Navigate to the ``frontend/aml_dashboard`` directory and install the frontend dependencies:

.. code-block:: bash

    cd frontend/aml_dashboard
    npm i


By following these steps, you'll have *AML Dashboard* equipped with all the necessary components and dependencies.
