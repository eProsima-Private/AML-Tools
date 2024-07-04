.. include:: /rst/exports/alias.include
.. include:: /rst/exports/roles.include

.. _amlip_specification:

#################################
AML Integrating Platform (AML-IP)
#################################

*AML Integrating Platform (AML-IP)* is a communications framework in charge of data exchange between *Algebraic Machine Learning (AML)* nodes through local or remote networks.
It is designed to allow non-experts users to create and manage a cluster of |aml| nodes to exploit the distributed and concurrent learning capabilities of |aml|.
Thus, |amlip| is a communication framework that makes the transport protocols abstracted from the user, creating a platform that communicates each node without requiring the user to be concerned about communication issues.
It also allows the creation of complex distributed networks with one or multiple users working on the same problem.

This framework is developed as part of the `ALMA project <https://alma-ai.eu/>`_, which has received funding from the European Union's Horizon 2020 research and innovation programme under grant agreement No 952091.
The aim of the EU-funded ALMA project is to leverage |aml| properties to develop a new generation of interactive, human-centric machine learning systems.
These systems are expected to reduce bias and prevent discrimination, remember what they know when they are taught something new, facilitate trust and reliability and integrate complex ethical constraints into human-artificial intelligence systems.
Furthermore, they are expected to promote distributed, collaborative learning.

.. figure:: /rst/figures/amlip/amlip_overview.png

Following are the main scenarios that the current *AML-IP* supports:

* `Monitor Network State Scenario <https://aml-ip.readthedocs.io/en/latest/rst/user_manual/scenarios/monitor_state.html>`__:
  Analyze the state of a network remotely.
* `Workload Distribution Scenario <https://aml-ip.readthedocs.io/en/latest/rst/user_manual/scenarios/workload_distribution.html>`__:
  Distribute the machine learning training phase to multiple nodes to parallelize heavy computation.
* `Collaborative Learning Scenario <https://aml-ip.readthedocs.io/en/latest/rst/user_manual/scenarios/collaborative_learning.html>`__:
  Share models between nodes without having to share the private dataset with which the model was trained.
* `Distributed Inference Scenario <https://aml-ip.readthedocs.io/en/latest/rst/user_manual/scenarios/distributed_inference.html>`__:
  Distribute large amounts of data to multiple nodes to perform inference in parallel.

Check section :ref:`amlip_overview` to have a further explanation of the concepts of this project.

.. toctree::
   :maxdepth: 2
   :hidden:

   /rst/amlip/specification/overview
