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

Requirements
------------

If |amlip| is not already installed in your system, follow the installation instructions provided `here <https://aml-ip.readthedocs.io/en/latest/rst/installation/linux.html>`__.

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
