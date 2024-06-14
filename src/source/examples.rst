Examples
========

.. note::
   There exists a repository with examples for the Cocket Nova CH552 board, which you can find here:

    .. raw:: html
        
        <a href="https://github.com/UNIT-Electronics/CH55x_SDCC_Examples" target="_blank">CH552 SDCC examples</a>

This repository provides examples for developing software in C using the SDCC compiler for the CH552 microcontroller. It serves as an excellent resource for both beginners and experienced developers, offering versatile and affordable solutions for CH552 development.

Although the examples are written in C, you can use Loadupch to upload the firmware to the CH552 microcontroller. Loadupch is software dedicated to uploading firmware to the CH552 microcontroller. 

Clone the repository and follow the instructions to compile and upload the firmware to the CH552 microcontroller:

.. raw:: html

   <a href="https://github.com/UNIT-Electronics/CH55x_SDCC_Doc" target="_blank">Documentation for Compiled examples</a>

Flash Firmware Using Loadupch
-----------------------------

To flash the firmware using Loadupch, follow the steps below:

1. Clone the repository with the examples:

.. code-block:: bash

    git clone https://github.com/UNIT-Electronics/CH55x_SDCC_Examples.git

2. Open the Loadupch software:

.. code-block:: bash

    python -m loadupch

3. Press the ```boot``` button on the CH552 board and connect the device to the USB port of your computer.

4. Press the ```Connect``` button on the Loadupch interface.

5. Select the firmware file from the ``Software/examples/Blink`` repository and press the ```flash firmware```` button.

.. _figure_example:
.. figure:: /_static/example_blink.png
   :align: center
   :alt: example blink
   :width: 100%

   Path to example blink

6. The software will show the message ```Firmware flashed``` and the device will be ready to use.

7. Finally, press the ```run programmer Exit``` button on the Loadupch interface.

.. _figure_flash_firmware:

.. figure:: /_static/led.png
   :align: center
   :alt: flash firmware
   :width: 80%

   Blink example
