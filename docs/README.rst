Documentation
=============
This is the documentation for the Python package
``factorymind`` which makes it easier to interact with the data
on the FactoryMind platform.

.. image:: https://github.com/factorymind/factorymind/blob/master/docs/logo.png
   :width: 200px


************
Installation
************
From PyPi:

.. code:: bash

    pip install factorymind

From source:

.. code:: bash

    <TODO: Document>

***
Use
***
To interact with your data on the FactoryMind platform,
run

.. code:: python

    >>> from factorymind.data_loader import FactoryDB

    >>> mydb = FactoryDB(apikey=YOUR-API-KEY)
    >>> mydb.list_data_sources()

    ['example_data.energy_demand', 'example_data.sensors', 'sensor_data.sensors', 'sensor_data.sensors_metadata']

See the `official docs <https://factorymind.readthedocs.io>`_ for more information and examples.
