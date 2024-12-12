.. include:: /rst/exports/alias.include
.. include:: /rst/exports/roles.include

.. _tutorials_dashboard_data_management:

##################################
Manage data with the AML Dashboard
##################################

Background
==========

The :term:`AML` Dashboard is a web-based tool that allows users to interact with the |aml| framework.

This tutorial showcases the data collection step of an |aml| model training process using the *AML Dashboard*.

Prerequisites
=============

Ensure you have installed the *AML Dashboard* using one of the following methods:

- :ref:`Linux Installation <amldashboard_linux>`
- :ref:`Docker Image Installation <amldashboard_docker>`

For more information, check the :ref:`AML Dashboard Interfaces <amldashboard_interfaces_data_collection>` and :ref:`AML Dashboard Usage <amldashboard_usage_data_management>` sections.

Running the demo
================

To run the necessary components for collecting data using the |aml| Dashboard, follow these steps:

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

Collecting data
===============

There are several options available for dataset creation:

* **Webcam**: Record instances using the webcam.

    1. Navigate to the ``Data Management`` tab on the |aml| Dashboard.
 
    2. Choose ``Sensors`` from the drop-down menu in the *Choose the model for the training set* section.
 
    3. In the *webcam* section, toggle the ``activate video`` button to enable the webcam.
 
    4. Introduce a label for the class that will be recorded in the *Instance label* section.
 
    5. Press the ``Hold to record instances`` button in the *Capture instances to the training set* section to start recording data.
 
    .. raw:: html
 
       <video id=myVideo width=100% height=auto autoplay loop controls muted>
          <source src="../../_static/resources/tutorials/dashboard_data_management.mp4">
          Your browser does not support the video tag.
       </video>
 
       <script>
          // Set the speed of the video once the page is loaded
          window.onload = function() {
             document.getElementById('myVideo').playbackRate = 1.3; // Set speed to 1.3x
          };
       </script>

* **Standard dataset**: Load a standard dataset from the system.

    1. Navigate to the ``Data Management`` tab on the |aml| Dashboard.
 
    2. Choose a dataset from the drop-down menu in the *Choose the model for the training set* section.
 
    3. Click on the ``Load dataset`` button to load the dataset.
 
    .. TODO : Add video for loading a standard dataset

* **Custom dataset**: Load a custom dataset.

    1. Navigate to the ``Data Management`` tab on the |aml| Dashboard.
 
    2. Choose 'Custom' from the drop-down menu in the *Choose the model for the training set* section.
 
    3. Click on the ``Load dataset`` button to load the custom dataset.
 
    4. A popup will appear, allowing you to select the desired dataset from your local machine.
 
    .. warning::
 
       The custom dataset must be a json file in the correct format.
 
       To create the dataset in the desired format, the code snippet below can be used as a reference:
 
       .. code-block:: python
 
          def save_in_format(images, labels):
             """
             Function that formats the data to be saved in the required format.
             Arguments:
             images: List of images. Each image is a one-dimensional list.
             labels: List of labels. Each label is an integer.
             returns: Formatted data
             """
 
             def generate_data_uri(image):
                 """
                 Convert a 2D image list or array to a PNG data URI.
                 """
                 # Convert the list to a NumPy array for processing
                 image_len = len(image)
                 one_side = int(math.sqrt(image_len))
                 image_array = np.array(image, dtype=np.uint8).reshape(one_side, one_side)
                 img = Image.fromarray(image_array, mode="L")  # Create a PIL image from the array
                 buffered = io.BytesIO()
                 img.save(buffered, format="PNG")  # Save the image to the buffer in PNG format
                 img_data = buffered.getvalue()
                 data_uri = f"data:image/png;base64,{base64.b64encode(img_data).decode('utf-8')}"
                 return data_uri
 
             combined_data = list(zip(images, labels))
             sampled_data = random.sample(combined_data, 100)
             sampled_images, sampled_labels = zip(*sampled_data)
             # Prepare the data in the required format
             formatted_data = {
                 "total": len(images),
                 "limit": 1000,  
                 "skip": 0,
                 "instances": [
                     {
                         "datasetName": "training2-set-models", # This must be kept as is
                         "x": image, # The image must be a one-dimensional list
                         "thumbnail": generate_data_uri(image),
                         "y": label, # The label must be numeric
                         "id": idx,
                     }
                     for idx, (image, label) in enumerate(zip(sampled_images, sampled_labels))
                 ]
             }
 
             return formatted_data
 
    .. TODO : Add video for loading a custom dataset