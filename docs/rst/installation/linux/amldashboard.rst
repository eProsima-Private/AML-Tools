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

Python dependencies
^^^^^^^^^^^^^^^^^^^

Ensure you have **python3.11** installed together with the packages listed in the ``requirements.txt`` file. If not, install them using the following command:
Ensure you have python3.11 intsalled together with the packages listed in the requirements.txt file. If not, install them using the following command:  

.. code-block:: bash
    curl https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -o Miniconda3-latest-Linux-x86_64.sh

    #To activate the conda environment automatically when opening shell. For changes to take effect, close and re-open current shell.
    bash Miniconda3-latest-Linux-x86_64.sh

    #To activate the conda environment manually each time you open the shell:
    eval "$(/home/user/miniconda3/bin/conda shell.zsh hook)" 

    conda create --name aml-ip-venv python=3.11
    conda activate aml-ip-venv
    cd AML-Dashboard
    pip3 install -r requirements.txt

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
