Unpaired Device
===============

There are several reasons why the device might not be connected:

- The device is not connected to the USB port.
- The device is not in boot mode.
- The system does not have the necessary permissions to access the device.
- The driver is not installed.

To solve the problem, you can try the following steps:

1. Check if the device is connected to the USB port.
2. Check if the device is in boot mode.
3. Check if the system has the necessary permissions to access the device.

If the problem persists, you can try the following steps:

1. Check if the driver is installed.

Use Zadig to install the driver:

.. _figure_zadig:
.. figure:: /_static/driver.png
    :align: center
    :alt: Zadig interface
    :width: 90%

    Zadig interface

1. Go to the "Options" menu and select "List All Devices".
2. Locate the device with USB MODULE VID = 0x4348 and PID = 0x55E0.

.. _figure_device:
.. figure:: /_static/zadig_device.png
    :align: center
    :alt: Selected device
    :width: 90%

    Device selected

3. Select the driver "libusb-win32 (v1.2.6.0)" and press the "Install Driver" button.

.. _figure_install_driver:
.. figure:: /_static/zadig_driver.png
    :align: center
    :alt: Install driver
    :width: 90%

    Driver selected
    
.. _figure_device_success:
.. figure:: /_static/zadig_success.png
    :align: center
    :alt: Device successfully installed
    :width: 90%

    Device installed

After that, the device will be recognized by the system.
