"""
Functionality for interaction with factory data
on the FactoryMind platform

Code documentation
^^^^^^^^^^^^^^^^^^
"""

# Standard library imports
# Third party imports
import pandas as pd
import requests

from factorymind.exceptions import (
    CouldNotFetchDataException,
    DatasetDoesNotExistException,
)

# API_URL_BASE = "core-api"


class FactoryDB(object):
    """Class for FM interaction with factory data

    Class arguments
    ---------------
    :param api_url_base: str, defaults to "core-api:80".
        Url to FM api
    :param api_key: str, default `None`.
        API key to use with FM API
    :param verbose: boolean, default `True`
        Indicator to print out list of data sources
    """

    def __init__(
        self,
        api_url_base: str = "core-api:80",
        api_key: str = None,
        verbose: bool = True,
    ):
        """Constructor method"""
        self.api_url_base = api_url_base
        self.api_key = api_key
        self.verbose = verbose
        self.datasets = self.list_data_sources()

    def list_data_sources(self):
        """List available data sources on factory data platform

        Arguments:
        ----------

        Returns:
        --------
        :return data_sources: list of strings.
            List of data sources (collections) available on FactoryMind data platform
        :rtype: list

        Example
        ^^^^^^^
        .. code-block:: python

            >>> from factorymind.data_loader import FactoryDB

            >>> mydb = FactoryDB(apikey=YOUR-API-KEY)
            >>> mydb.list_data_sources()

            ['example_data.energy_demand', 'example_data.sensors', 'sensors.sensors', 'sensors.sensors_metadata']
        """
        resp = requests.get(
            f"http://{self.api_url_base}/list_data_sources?verbose=true"
        )
        data_sources = self._get_response(resp)
        return data_sources

    def data_info(self, dataset: str):
        """More info on specific dataset.

        Arguments:
        ----------
        :param dataset: str.
            Name of dataset (table) to get info about.

        Returns:
        --------
        :return dataset_info: dict.
            Info of dataset, keys "name", "nrows", "ncolumns"
        :return dataset_columns: list.
            List of dataset columns (strings)
        :return dataset_sample: pd.DataFrame.
            Sample of 5 last records in dataset

        Example
        ^^^^^^^
        .. code-block:: python

            >>> from factorymind.data_loader import FactoryDB

            >>> mydb = FactoryDB(apikey=YOUR-API-KEY)
            >>> table_info, _, df_sample = mydb.data_info(dataset='example_data.energy_demand')
            >>> print(table_info)

            {'name': 'example_data.energy_demand', 'nrows': 35064, 'ncolumns': 29}
        """
        self._check_if_dataset_exists(dataset)
        resp = requests.get(f"http://{self.api_url_base}/data_info?dataset={dataset}")
        data_resp = self._get_response(resp)

        # Construct output
        dataset_info = {key: data_resp[key] for key in ["name", "nrows", "ncolumns"]}
        dataset_columns = data_resp["columns"]
        dataset_sample = pd.DataFrame(data_resp["sample"], columns=dataset_columns)

        return dataset_info, dataset_columns, dataset_sample

    def get_data(self, dataset: str, limit: int = 10000):
        """Fetch batch dataset from DB

        Arguments:
        ----------
        :param dataset: str.
            Name of dataset (collection)
        :param limit: int, default 10000.
            Number of datapoints (rows) to limit query to

        Returns:
        --------
        :return data: pd.DataFrame.
            Dataset, limited to last "limit" records

        Example
        ^^^^^^^
        .. code-block:: python

            >>> from factorymind.data_loader import FactoryDB

            >>> mydb = FactoryDB(apikey=YOUR-API-KEY)
            >>> df = mydb.get_data(dataset="example_data.sensors", limit=100)
        """
        self._check_if_dataset_exists(dataset)
        resp = requests.get(
            f"http://{self.api_url_base}/get_data?dataset={dataset}&limit={limit}"
        )
        data_resp = self._get_response(resp)

        # Construct output
        if "columns" in data_resp.keys():
            data = pd.DataFrame(data_resp["data"], columns=data_resp["columns"])
        else:
            data = pd.DataFrame(data_resp["data"])

        return data

    def run_custom_query(self, query: str):
        """Run custom SQL query towards DB

        :param dataset: str.
            Name of dataset (collection)
        :param limit: int, default 10000.
            Number of datapoints (rows) to limit query to

        :return data: pd.DataFrame.
            Dataset, limited to last "limit" records

        Example
        ^^^^^^^
        .. code-block:: python

            >>> from factorymind.data_loader import FactoryDB

            >>> mydb = FactoryDB(apikey=YOUR-API-KEY)
            >>> query = \"\"\"
                        SELECT timestamp, sensor_00
                        FROM example_data.sensors
                        WHERE sensor_00 > 2.30;
                    \"\"\"
            >>> df = mydb.run_custom_query(query)
        """
        # self._check_if_dataset_exists(dataset)
        resp = requests.get(f"http://{self.api_url_base}/custom_query?query={query}")
        data_resp = self._get_response(resp)

        # Construct output
        if "columns" in data_resp.keys():
            data = pd.DataFrame(data_resp["data"], columns=data_resp["columns"])
        else:
            data = pd.DataFrame(data_resp["data"])

        return data

    def _check_if_dataset_exists(self, dataset):
        """Check if specified dataset name exists in DB"""
        if dataset not in self.datasets:
            raise DatasetDoesNotExistException(dataset)

    @staticmethod
    def _get_response(response):
        """Get response of API call"""
        if response.status_code != 200:
            # Something went wrong in API call
            raise CouldNotFetchDataException()
        else:
            data = response.json()
            return data
