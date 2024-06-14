Usage
======
To use the Loadupch, you can run the following command:

.. code-block:: bash

    python -m loadupch

The software will open a window with the interface. You can select the device press the "Connect" button.

.. _figure_connect:

.. figure:: /_static/loadupch_connect.png
   :align: center
   :alt: Loadupch interface
   :width: 50%

   Loadupch interface

.. note::
    Before connect the device, press the "boot" button on the CH552 board.

.. _figure_flash:
.. figure:: /_static/CH552_boot.png
    :align: center
    :alt: button boot
    :width: 80%

    Cocket Nova CH552 button boot

The interface will show the message "Device connected" and you can select the firmware file and press the "flash firmware" button.

.. _figure_message:
.. figure:: /_static/device_found.png
    :align: center
    :alt: message
    :width: 50%

    Device found message


Flash firmware
==============

For the up load firmware, press the "flash firmware" button. 

.. note::
    Only ``.bin`` files are supported.

Automatically the software open the file dialog, you can select the firmware file and press the "open" button.

.. _figure_flash_firmware:
.. figure:: /_static/loadupch_firmware.png
    :align: center
    :alt: flash firmware
    :width: 50%

    Flash firmware dialog

The software will show the message "Firmware flashed" and the device will be ready to use.

.. _figure_success:
.. figure:: /_static/success_flas.png
    :align: center
    :alt: success
    :width: 50%

    Firmware flashed message


Verify firmware loaded
-----------------------

To verify the firmware loaded, press the "verify firmware" button.

.. _figure_verify:
.. figure:: /_static/verify_firmware.png
    :align: center
    :alt: verify firmware
    :width: 50%

    Verify firmware dialog

The software will show the message "Firmware verified" if the firmware is loaded correctly.

