Installation
============

.. warning::
    The Loadupch is a project under development. The software is not stable and may have bugs.

Requirements
------------
The Loadupch requires the following software:

- `Python 3.6 or higher <https://www.python.org/>`_

The Loadupch requires the following libraries:

.. code-block:: bash

    pip install pyusb

.. code-block:: bash

    pip install tkinter

Loadupch Installation
-----------------

For easy installation, you can use the following command:

.. code-block:: bash

    pip install loadupch

If you use Linux, you may need to install the following packages:

.. code-block:: bash

    sudo apt-get install libusb-1.0-0-dev libudev-dev

.. note::

    For more information, you can check the documention `Documentation for Compiled examples <https://github.com/UNIT-Electronics/CH55x_SDCC_Doc>`_ on the section CH55x with SDCC and Ubuntu
    



Usage
-----

To use the Loadupch, you need to connect the CH552 microcontroller to the USB port of your computer. 
Then, you can run the following command:

.. code-block:: bash

    python -m loadupch

The software will open a window with the interface. You can select the device press the "Connect" button.

.. note::
    Before connect the device, press the "boot" button on the CH552 board.


After that, you can select the firmware file and press the "flash firmware" button.


Uninstallation
--------------

In the case that software is not useful for you, you can uninstall it using the following command:

.. code-block:: bash

    pip uninstall loadupch