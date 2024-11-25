.. include:: /rst/exports/alias.include
.. include:: /rst/exports/roles.include

.. _aml_hw_toolkit_overview:

#################################
Overview of Hardware Architecture
#################################

The proposed hardware architecture is a Single Instruction, Multiple Data (SIMD) processor designed to utilize parallel compute units for accelerating AML tasks.
This parallelism makes them highly effective for tasks that involve large amounts of data that can be processed in parallel.
The architecture groups multiple data into vectors, allowing one instruction to perform the same operation across all elements, thereby improving efficiency and reducing the overhead associated with repetitive instruction fetches.
Although SIMD processors excel at tasks with regular, parallel data structures, they are less suited for irregular computations, which limits their flexibility in certain applications.
Despite this, their ability to enhance performance and energy efficiency for specific workloads makes them a critical component in modern computing architectures.
This architecture features numerous parallel cores as shown in Fig.1, each with its own memory hierarchy. Given that AML is a highly memory-bound application, we have incorporated High Bandwidth Memory (HBM) DRAM into our design.
HBM is an advanced type of memory designed to provide significantly higher data transfer rates than traditional memory technologies, such as DDR (Double Data Rate) or GDDR (Graphics Double Data Rate).
HBM achieves this by stacking multiple memory dies vertically, connected through TSVs (Through-Silicon Vias), and placing them in close proximity to the processor.
This three-dimensional architecture minimizes the distance that data needs to travel, reducing latency and power consumption while greatly increasing bandwidth.
HBM is particularly effective in applications that require massive data throughput, such as AML workloads.
Its architecture allows for multiple parallel data paths, enabling data transfers at rates exceeding hundreds of gigabytes per second.

Key Features
============

1. **Parallel Cores and Memory Hierarchy:**

    * The hardware architecture consists of parallel cores, each capable of independently computing an AML task.
    * Each core consists of computing units specifically designed for AML tasks. These units are internally parallelized, providing high throughput.
    * Each core is connected to a channel of HBM memory, enabling independent operation from other cores with high memory bandwidth.
    * Cores contain local scratchpad buffers, allowing data reuse and prefetching to minimize off-chip memory access.

2. **Custom Instruction Set:**

    * The core operations are controlled through an in-house defined instruction set.
    * This instruction set includes details about the type of operation, size, and address of data, which the control unit uses to fetch data and activate the corresponding compute unit.

3. **PCIe Interface:**

    * The architecture is equipped with a PCIe interface, making it compatible with any existing computing platform.
    * Users can offload time-consuming AML tasks to the hardware accelerator, leveraging parallelization to improve throughput.
    * Results from each task can be accessed through the PCIe interface.

.. figure:: /rst/figures/amlhw/amlhw_overview.png
    :align: center
    :width: 800px
    :alt: Overview of AML Hardware Architecture.
    :figclass: align-center
    
    Overview of AML Hardware Architecture.