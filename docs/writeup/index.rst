.. You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Documentation
=============
This is the documentation for the Python package
``factorymind`` which makes it easier to interact with the data
on the FactoryMind platform.

.. toctree::
   :maxdepth: 3
   :caption: Contents:

   source/modules

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

    ['example_data.energy_demand', 'example_data.sensors', 'sensors.sensors', 'sensors.sensors_metadata']

See module :doc:`source/factorymind.data_loader` for more information and examples.

******************
Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
