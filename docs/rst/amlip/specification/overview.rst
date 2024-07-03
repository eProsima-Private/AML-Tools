.. include:: /rst/exports/alias.include
.. include:: /rst/exports/roles.include

.. _amlip_overview:

########
Overview
########

AML
===

:term:`AML` is a cutting edge :term:`ML` technology based on algebraic representations of data.
Unlike statistical learning, |aml| algorithms are robust regarding the statistical properties of the data and are parameter-free.
This makes |aml| a great candidate in the future of ML, as it is far less sensitive to statistical characteristics of the training data, and can integrate unstructured and complex abstract information apart from the training data.

|aml| algorithm has several characteristics that makes it a great player in distributed learning.
First, |aml| can be trained in parallel from different remote machines, and can merge the training information without losing information.
It can also be shared and merged with other already trained models and share their learnt information without revealing the training data-set.


AML-IP
======

|eamlip| is a framework based on different libraries and graphical and non-graphical tools that allow to create a network of nodes focused no different tasks of the |aml| environment.
Every running part of the |amlip| is considered a **Node**.
This is an **independent** and **distributed** software that could perform a specific **action**.

* *Independent* means that it is auto-sufficient and does not require the presence of any other node.
* *Distributed* means that can communicate with different nodes in the network, interacting and solving tasks collaboratively.
* *Action* is every part of the |aml| or any satellite action required in order to perform the correct execution of the algorithm or to support or facilitate the communication and managing of the different nodes.

These nodes are separated in different scenarios, that are explained more in detail in the :ref:`following section <amlip_scenarios>`.

.. figure:: /rst/figures/amlip/amlip_overview.png


Usage
=====

|amlip| is a complex framework composed of different tools that run independently and out-of-the-box.
But it also features some libraries that allow to instantiate |amlip| entities or :term:`Nodes <Node>` whose behavior and functionality must be specified by the user.
These libraries are presented in 2 main programming languages:

C++
---

This is the main programming language in |amlip|.
|cpp| has been chosen because it is a very versatile and complete language that allows to easily implement complex concepts maintaining high performance.
Also |fastdds| is mainly built in |cpp| and using the same programming language allows to easily interact without losing performance with the middleware layer.

There is a public :term:`API` found in :code:`AML-IP/amlip_cpp/include` with all the installed headers that can be used from the user side.
The API, implementation and testing of this part of the code can be found mainly under sub-package `amlip_cpp <https://github.com/eProsima/AML-IP/tree/main/amlip_cpp>`__.

Python
------

This is the programming language though to be used by a final user.
|python| has been chosen as it is easier to work with state-of-the-art :term:`ML` projects.

Nodes and classes that the user needs to instantiate in order to implement their own code are parsed from |cpp| by using |swig| tool, giving the user a |python| API.
The API, implementation and testing of this part of the code can be found mainly under sub-package `amlip_py <https://github.com/eProsima/AML-IP/tree/main/amlip_py>`__.


Architecture and Infrastructure
===============================

|amlip| is a software project based on different programming languages.
It is a **public** **open-source** project focused to be used by the :term:`ML` and scientific community.
The whole project is hosted on a |github| repository, and can be found in the following url: |amlipgithubpage|.
The code project is divided in sub-packages that can be built, installed and tested independently.

|amlip| is a software project that does not rely on any specific hardware or Operating System, and does not require any physical infrastructure.
The storage and CI is hosted by |github|.

Enabling technologies
=====================

The technologies supporting |amlip| development emphasize communication between nodes, protocols used to support such communication, and the libraries and tools used to handle the different types of data to be transmitted.

.. _technologies_dds:

DDS (Data Distribution Service)
-------------------------------

:term:`DDS` is a distributed dynamic real-time middleware protocol based on a specification defined by the :term:`OMG`.
It relies on the underlying :term:`RTPS` wire protocol.

|amlip| framework relies on :term:`DDS` communication protocol to connect and communicate each of its :term:`Nodes <Node>`.
:term:`DDS` protocol support :term:`publications <Publish>` and :term:`subscriptions <Subscribe>` in different :term:`Topics <Topic>` in order to create a distributed network of entities where communication takes place peer-to-peer, avoiding centralized systems and creating an homogeneous and stand-alone network.
:term:`DDS` relies on :term:`QoS` to configure different characteristics for each of the communication channels, allowing to create really dynamic and complex networks.

Fast DDS
^^^^^^^^

|amlip| uses |efastdds|, a C++ open-source library that implements :term:`DDS` specification.
|efastdds| has all the features and characteristics needed to power |amlip| communications.
A whole documentation for the |fastdds| project can be found in |FastDDSDocs|.
