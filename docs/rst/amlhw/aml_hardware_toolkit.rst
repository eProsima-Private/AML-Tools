.. include:: /rst/exports/alias.include
.. include:: /rst/exports/roles.include

.. _aml_hw_toolkit:

####################
AML Hardware Toolkit
####################

Introduction
============

Modern computing predominantly relies on general-purpose processors like CPUs because of their flexibility and ease of programming.
However, this convenience comes with a significant energy cost and low throughput, as CPUs consume much more power and time for fetching and decoding instructions than performing basic operations.
To address the need for both higher performance and energy efficiency, domain-specific accelerators, such as FPGAs and ASICs, offer a compelling alternative.
These accelerators are tailored to specific computational tasks, making them far more efficient for workloads.
While CPUs and GPUs are flexible and capable of handling a wide range of tasks, they struggle with irregular parallelism and limited precision support.
In contrast, FPGAs can be reprogrammed for different tasks, and ASICs offer efficiency, though at the cost of flexibility and development complexity. 
In the ALMA project, the RPTU team was responsible for designing and developing a hardware accelerator specifically for Algebraic Machine Learning (AML).
Existing hardware platforms, such as GPUs, are primarily optimized for AI applications, which have substantially different computational characteristics compared to AML.
The compute demand of AML requires a platform specifically optimized for this algorithm.
Our task was to design a hardware architecture that efficiently accelerates AML tasks.

.. toctree::
   :maxdepth: 2
    /rst/amlhw/overview
    /rst/amlhw/internal_architecture_aml_core