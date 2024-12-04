.. include:: /rst/exports/alias.include
.. include:: /rst/exports/roles.include

.. _internal_architecture_aml_core:

#################################
Internal Architecture of AML Core
#################################

The internal hardware architecture of each core is designed to perform key set-like operations in linear algebra, such as the intersection, union, and subtraction of subspaces.
The intersection operation produces a new set by identifying vectors common to both input subspaces.
The union helps define relationships between different subspace structures.
These operations can be efficiently implemented using basic logical gates.
However, the primary challenge lies in managing the large data sizes involved in these computations.
To address this, our memory subsystem utilizes parallel memory channels to provide high bandwidth, allowing each core in the architecture to access and process data independently, ensuring efficient computation across multiple cores.

================================
Implementation and Demonstration
================================

In our experimental setup, we utilized the Xilinx Alveo U280 FPGA board, connected to a host server equipped with an Intel CPU.
The U280's high-bandwidth memory (HBM) and programmable logic enabled efficient handling of large datasets and parallel computations.
Custom hardware designs were developed using Xilinx Vitis HLS for high-level synthesis and Vivado for design synthesis and implementation.
The Intel CPU on the host server was responsible for managing the system, sending instructions to the FPGA, and coordinating data transfers via PCIe.
Xilinx Runtime (XRT) was used to compile and manage communication between the FPGA and the host, ensuring the smooth execution of our accelerator design across various test cases.

============
Software API
============

To streamline the use of our hardware platform, we have developed a high-level software API designed to abstract the underlying complexity of the FPGA-based accelerator.
This API allows users to fully utilize the hardware's computational capabilities without requiring in-depth knowledge of the accelerator's architecture or low-level operations.

* **High-Level Functionality:**
    The API offers a set of high-level functions that serve as replacements for traditional CPU-based AML (Accelerated Machine Learning) implementations.
    These functions automatically translate user requests into optimized hardware instructions, allowing seamless integration with the FPGA accelerator.
    By handling this translation, the API minimizes the need for manual configuration, improving usability for both novice and advanced users.

* **Data Management and Core Allocation:**
    The API efficiently manages the flow of data between the host CPU and the FPGA.
    It handles the transmission of user-provided data to the FPGA, ensuring that it is properly formatted and allocated for processing.
    In addition, the API dynamically activates the appropriate number of cores on the FPGA, optimizing resource allocation based on the specific computational task.
    Once the task is complete, the API retrieves the processed data from the FPGA and transfers it back to the host’s memory, making the results readily available for further processing or analysis.
    This streamlined approach enhances both performance and user experience, providing an efficient and transparent way to interact with the hardware accelerator while reducing the complexity traditionally associated with FPGA-based computing.

.. figure:: /rst/figures/amlhw/user_app_hw_api.png
    :align: center
    :width: 800px
    :alt: Workflow of User Application and Hardware API interaction with FPGA.
    :figclass: align-center

    Workflow of User Application and Hardware API interaction with FPGA.

===========
Scalability
===========

The compute platform is highly scalable.
Multiple FPGA nodes can be attached to a host system, providing massive computational power.
This scalability ensures that our hardware accelerator can handle increasing demands and larger AML tasks effectively.