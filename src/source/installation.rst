Installation
============

.. warning::

    Loadupch is freely available for use. However, the software is currently under development and may contain bugs.


Requirements
------------
Loadupch requires  `Python 3.6 or higher <https://www.python.org/>`_ and the following libraries:

.. code-block:: bash

    pip install pyusb

.. code-block:: bash

    pip install tkinter


Loadupch Installation
---------------------

For easy installation, you can use the following command:


.. code-block:: bash

    pip install loadupch


Driver Installation
-------------------

.. tabs:: 

    .. tab:: Windows
            
        To install the driver, you can use the Zadig software. Download the latest version of ``Zadig``. You can download it from the official website.
        
            .. raw:: html

                <a href="https://zadig.akeo.ie/" target="_blank">Zadig</a>
        
    .. tab:: Ubuntu
        If you use Linux, you may need to install the following packages:

        .. code-block:: bash

            sudo apt-get install libusb-1.0-0-dev libudev-dev









Uninstallation
--------------

In the case that software is not useful for you, you can uninstall it using the following command:

.. code-block:: bash

    pip uninstall loadupch