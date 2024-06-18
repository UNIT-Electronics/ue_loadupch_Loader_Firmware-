.. Loadupch documentation master file, created by
   sphinx-quickstart on Fri Jun 14 13:01:21 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Loadupch v0.0.1
========================


.. warning::
    
    Loadupch is freely available for use. However, the software is currently under development and may contain bugs.



Loadupch is a software tool specifically designed for uploading firmware to the CH552 microcontroller. 
Developed in Python, this application leverages the PyUSB library to facilitate communication with the device.

Loadupch is based on the loader implementation by Stefan Wagner, available at `Stefan Wagner's GitHub <https://github.com/wagiminator>`_.
Originally inspired by the ``chprog.py`` project found at `chprog.py on GitHub <https://github.com/wagiminator/CH552-USB-OLED/tree/main/software/cdc_i2c_bridge/tools>`_,
Loadupch enhances the original by introducing a graphical user interface, making it significantly more user-friendly.

.. figure:: /_static/loadupch.png
   :align: center
   :alt: Loadupch interface

   Loadupch interface


This documentation is divided into the following sections:

.. toctree::
   :maxdepth: 2
   :caption: Contents:
   
   installation
   usage
   flash
   examples
   error





Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
