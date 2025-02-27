.. include:: /rst/exports/alias.include
.. include:: /rst/exports/roles.include

.. _tutorials_dashboard_add_custom_model:

##########################################
Add Your Custom Model to the AML-Dashboard
##########################################

Background
==========

The :term:`AML` Dashboard is a web-based tool that allows users to interact with the |aml| framework.
This tutorial will guide you through the process of integrating your custom model into the AML Dashboard for training, inference, and batch prediction.

Prerequisites
=============

Ensure you have installed the *AML Dashboard* using one of the following methods:

- :ref:`Linux Installation <amldashboard_linux>`
- :ref:`Docker Image Installation <amldashboard_docker>`

For more information about, check the :ref:`Parallelize AML training with AML-IP <parallelize_aml_training_with_aml_ip>` and :ref:`MNIST binary classifier with AML <tutorials_aml_pipeline>` sections.

Step 1: Implement Training Functions
====================================

Develop your training functions using the AML-Toolkit documentation as a reference.
You can also leverage existing functions in:

* ``backend/AML_binary_classifier.py``
* ``backend/load_and_preprocess_datasets.py``
* ``backend/process_aml_model_results.py``

These files contain useful functions for processing training results and utilizing the trained model for inference.
You can also follow the steps provided in :ref:`Parallelize AML training with AML-IP <parallelize_aml_training_with_aml_ip>` and :ref:`MNIST binary classifier with AML <tutorials_aml_pipeline>` tutorials.

Step 2: Integrate Your Model into the AML-Dashboard
===================================================

Backend modifications
---------------------

1. Navigate to the ``backend`` directory.
2. Add Your Training Functions.  Place your file containing training and post-processing functions inside the ``backend`` directory of the AML-Dashboard.
3. Modify ``computing.py``.

    Import your training function and integrate it within the ``ComputingNode`` class by modifying the ``process_job`` method:

    .. code-block:: python
        :emphasize-lines: 28, 29, 30, 31, 32

        def process_job(
            self,
            job,
            task_id,
            client_id):

            data = job.to_string()
            # Find the indices of 'x: ' and ' y: ' in the data string
            x_index = data.find('x: ')
            y_index = data.find(' y: ')
            n_iter_index = data.find(' n_iter: ')
            target_class_index = data.find(' target_class: ')
            model_index = data.find(' model: ')
            atomization_index = data.find(' atomization_uploaded: ')
            # Extract the substring between 'x: ' and ' y: ' to get the value of x
            x = json.loads(data[x_index + len('x: '):y_index])
            # Extract the substring between ' y: ' and ' n_iter: ' to get the value of y
            y = json.loads(data[y_index + len(' y: '):n_iter_index])
            # Extract the substring from ' n_iter: ' to the end of the string to get the value of n_iter
            n_iter = int(data[n_iter_index + len(' n_iter: '):target_class_index])
            # Extract the substring from ' target_class: ' to the end of the string to get the value of target_class
            target_class = int(data[target_class_index + len(' target_class: '):model_index])
            # Extract the substring from ' model: ' to the end of the string to get the value of model
            model_type = data[model_index + len(' model: '):atomization_index]
            # Extract the substring from ' atomization_uploaded: ' to the end of the string to get the value of atomization_uploaded
            atomization_uploaded = bool(data[atomization_index + len(' atomization_uploaded: '):] == 'True')
            print('Received job, calling train_alma')
            if model_type == 'Sensors':
                model = train_alma(x, y, n_iter)
            else: 
                print ('calling train_binary_classifier')
                model = train_binary_classifier(model_type, x, y, target_digit=target_class, iterations=n_iter, uploaded_atomization=atomization_uploaded)
            print('train_alma finished!')
            solution = JobSolutionDataType(json.dumps(model))
            return solution

    Modify this section to call your custom model instead of the predefined ones.
    If your model is independent of the dataset, you can remove the ``if`` conditions.

Frontend modifications
----------------------

4. Navigate to the ``frontend/aml_dashboard/src`` directory.
5. Modify the ``index.js`` file.

    Modify the training section to fit your model.
    If your model doesn’t rely on the dataset, remove the ``if`` clause. 

    .. code-block:: javascript
        :emphasize-lines: 4, 5, 6, 7, 8, 9, 10

        b.$click.subscribe(async () =>
            {
            const model = choose_model.$value.get();
            if (model === 'Sensors') {
            classifier.train(trainingSet)
            } else {
              const target_class = features.parameters['Target class'].value;
              await create_binary_dataset(target_class);
              classifier.train(trainingSet3);
            }
        }
        );

    .. code-block:: javascript
        :emphasize-lines: 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40

        b_train_AML.$click.subscribe( async () => {

          if (atomizationUploaded === true && textAMLTrainStatus.$value.get() === '<h2>Finished training with provided atomization :)</h2> '){
        	const userResponse = await showCustomModal();
        	if (userResponse === false) {
          	deleteAtomization();
          	atomizationUploaded = false;
        	}
          }

          textAMLTrainStatus.$value.set(' <h2>Training...</h2> <br> <img src="https://i.gifer.com/origin/05/05bd96100762b05b616fb2a6e5c223b4_w200.gif">');

          const model = choose_model.$value.get();
          const n_job = n_jobs.$value.get().toString();
          const n_iter = features.parameters['Iterations'].value;
          const percentage_data = features.parameters['Percentage of data'].value;
          const target_class = features.parameters['Target class'].value;

          const json_dt = {x : [], y : []};
          if (model == 'Sensors') {
        	const v = await trainingSet.find();
        	save_to_file(v, "training_set_.json"); // Save the training set to a file

        	const dt = v.data;
        	for(let i = 0; i < dt.length; i++) {
          	json_dt.x.push(dt[i].x);
          	json_dt.y.push(dt[i].y);
        	}
          } else {
        	await create_binary_dataset(target_class);

        	const v = await trainingSet3.find();

        	save_to_file(v, "training_set_.json");

        	const dt = v.data;
        	for(let i = 0; i < dt.length; i++) {
          	json_dt.x.push(dt[i].x);
          	json_dt.y.push(dt[i].y);
        	}
          }

Step 3: Implement Inference Functions
=====================================

Backend Modifications
---------------------

6. Modify ``inference.py``.

    Import your inference functions and integrate them into the ``InferenceNode`` class.
    Modify the ``process_inference`` function to use your model.
    If your model does not depend on a specific dataset, remove the ``if`` conditions.

    .. code-block:: python
        :emphasize-lines: 35, 36, 37, 38, 39, 40, 41

        def process_inference(
    	    self,
    	    inference,
    	    task_id,
    	    client_id):
    
    	    # Get the path to the Downloads directory
    	    downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
    	    # Create the full path to the most recent file
    	    training_path=use_most_recent_file(downloads_path, "training_set_")
    	    model_path=use_most_recent_file(downloads_path, "model_")
    	    try:
            	with open(model_path, 'r') as file:
                	json_file = file.read()
            	json_data = json.loads(json_file)
    	    except Exception as e:
            	print(f'Error reading model file: {e}')
            	exit(1)
    	    try:
            	with open(training_path, 'r') as file:
                	training_set = file.read()
    	    except Exception as e:
            	print(f'Error reading training set file: {e}')
            	exit(1)
    
    	    global aml_model_predict

    	    data = json.loads(inference.to_string().replace("'",'"'))

    	    try:
            	model = json_data['model_name']
    	    except:
            	model = 'Sensors'

    	    if model == 'Sensors':
            	aml_model_predict = process_model_data(json_file, training_set)
            	pred = aml_model_predict(data['data'])
    	    else:
            	aml_model_predict = calculate_misses(training_set, json_file)
            	print(aml_model_predict)
            	pred = aml_model_predict(data['data'])

    	    print('pred: ' + str(pred))
    	    inference_solution = InferenceSolutionDataType(json.dumps(pred))

    	    print(f'Data received from client: {client_id}\n'
            	f' with id: {task_id}\n'
            	f' job: {inference.to_string()}\n'
            	f' inference: {inference_solution.to_string()}')
    	    return inference_solution

Frontend Modifications
----------------------

7. Update the Batch Prediction Section. 

    Modify the ``index.js`` file to include your model in the batch prediction section.ç
    If the model is not dependent on the dataset, you can freely remove the ``if`` conditions.

    .. code-block:: javascript
        :emphasize-lines: 6, 7, 8, 9, 10, 11, 12

        predictButton.$click.subscribe(async () => {
          if (!classifier.ready) {
        	throwError(new Error('No classifier has been trained'));
          }
          await batchMLP.clear();
          if (choose_model.$value.get() === 'Sensors') {
        	batchMLP.clear();
        	await batchMLP.predict(classifier, trainingSet);
          } else {
        	batchMLP.clear();
        	await batchMLP.predict(classifier, trainingSet3);
          }
        });

    .. code-block:: javascript
        :emphasize-lines: 5, 6, 7, 8, 9, 10, 11, 12, 13, 14

        predictButtonAML.$click.subscribe(async () => {
          if (!aml_model['ready']) {
        	throwError(new Error('No AML model has been trained'));
          } else {
        	if (choose_model.$value.get() === 'Sensors') {
          	await batchAML.clear();
          	await batchAML.predict(mockAMLModel, trainingSet);

          	console.log('Predictions done');
          	console.log(batchAML.items().service)
        	} else {
          	batchAML.clear();
          	batchAML.predict(mockAMLModel, trainingSet3);
        	}
          }
        });

Conclusion
==========

By following these steps, you have successfully integrated your custom model into the AML-Dashboard for training, inference, and batch prediction. 
Adjust the code as necessary to fit your model’s specific requirements. 
Happy coding!
