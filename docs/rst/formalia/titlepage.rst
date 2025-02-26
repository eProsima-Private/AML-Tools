.. include:: /rst/exports/roles.include

.. image:: /rst/figures/intro/aml_toolkit_banner_light.png
   :align: center
   :width: 100%
   :alt: ALMA Toolkit
   :class: only-light

.. image:: /rst/figures/intro/aml_toolkit_banner_dark.png
   :align: center
   :width: 100%
   :alt: ALMA Toolkit
   :class: only-dark

|br|


*AML Toolkit* is a set of software tools that allows users to develop, train, and deploy Algebraic Machine Learning (AML) models.
These tools are designed to be used by researchers, developers, and industry professionals who want to implement AML models in their applications.
*AML Toolkit* aims to provide users, developers, and researchers with the documentation, guides, and examples needed to start working with AML.

These tools cover the entire process of developing AML applications, from data collection and preprocessing, to generating embeddings for problem description, validating those embeddings, training the model using an AML engine, perform inference using the resulted AML model, and validate the results.

This framework is developed as part of the `ALMA project <https://alma-ai.eu/>`__.
The aim of the EU-funded ALMA project is to leverage AML properties to develop a new generation of interactive, human-centric machine learning systems.
These systems are expected to reduce bias and prevent discrimination, remember what they know when they are taught something new, facilitate trust and reliability and integrate complex ethical constraints into human-artificial intelligence systems.
Furthermore, they are expected to promote distributed and collaborative learning.

########
Overview
########

*AML Toolkit* includes the following components:

* AML Description Language (AML-DL) specification, command set and examples to give the user the capability to describe elaborated embeddings with a concise code, and to establish a methodology to build embeddings for complex problems into semilattices and other algebras with idempotent operators.
* Architecture and usage of the AML-DL Interpreter, a software tool that transforms human-readable semantic embeddings, written in AML-DL, into AML input data for the AML Engine.
  The *AML Toolkit* also provides a set of examples of how to use the AML-DL Interpreter.
* AML-DL Consistency Checker user & developer guide, examples of usage, and consistent and inconsistent embedding catalog.
  The AMLDL Consistency Checker is a software tool to study the consistency of algebraic semantic embeddings into semilattices.
  Given a semantic embedding expressed using the AML-DL, it can determine if the embedding is consistent or not.
  If the embedding is not consistent the AML-DL Consistency Checker indicates the potential primary and secondary sources of the inconsistency.
* AML Integrating Platform (AML-IP). `AML-IP <https://aml-ip.readthedocs.io/en/latest/>`__ is a communications framework in charge of data exchange between AML nodes through local or remote networks.
  It is designed to allow non-experts users to create and manage a cluster of AML nodes to exploit the distributed and concurrent learning capabilities of AML.
  Thus, AML-IP is a communication framework that makes the transport protocols abstracted from the user, creating a platform that communicates each node without requiring the user to be concerned about communication issues.
  It also allows the creation of complex distributed networks with one or multiple users working on the same problem.

#################################
Get access to the Open AML Engine
#################################

.. _get_access_toolkit:

The Open AML Engine can be obtained at [github.com/Algebraic-AI/Open-AML-Engine](https://github.com/Algebraic-AI/Open-AML-Engine).

To contact the engine team, you can open a discussion on the Github repository or send an email to `info@algebraic.ai <info@algebraic.ai>`__.

Thank you for your interest in AML!

----

.. image:: /rst/figures/eu_flag.jpg
  :height: 45px
  :align: left

This project (ALMA: Human Centric Algebraic Machine Learning) has received funding from the European Union’s Horizon 2020 research and innovation programme under grant agreement No 952091.
