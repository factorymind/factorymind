"""
Functionality for interaction with factory data
on the FactoryMind platform
"""

# Standard library imports
# Third party imports
import pandas as pd
import requests

from factorymind.exceptions import (
    CouldNotFetchDataException,
    DatasetDoesNotExistException,
)

API_URL_BASE = "core-api"


class FactoryDB:
    """Class for FM interaction with factory data

    Class arguments:
    ----------------
    api_url_base : str, default "core-api:80"
        Url to FM api
    api_key : str, default None
        API key to use with FM API
    verbose : boolean, default True
        Indicator to print out list of data sources
    """

    def __init__(
        self,
        api_url_base: str = "core-api:80",
        api_key: str = None,
        verbose: bool = True,
    ):
        """Object initiator"""
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
        data_sources : list of strings
            List of data sources (collections) available on FactoryMind data platform
        """
        resp = requests.get(
            f"http://{self.api_url_base}/list_data_sources?verbose=true"
        )
        data_sources = self._get_response(resp)
        return data_sources

    def data_info(self, dataset):
        """More info on specific dataset.

        Arguments:
        ----------
        dataset : str
            Name of dataset (collection) to

        Returns:
        --------
        dataset_info : dict
            Info of dataset, keys "name", "nrows", "ncolumns"
        dataset_columns : list
            List of dataset columns (strings)
        dataset_sample : pd.DataFrame
            Sample of 5 last records in dataset
        """
        self._check_if_dataset_exists(dataset)
        resp = requests.get(f"http://{self.api_url_base}/data_info?dataset={dataset}")
        data_resp = self._get_response(resp)

        # Construct output
        dataset_info = {key: data_resp[key] for key in ["name", "nrows", "ncolumns"]}
        dataset_columns = data_resp["columns"]
        dataset_sample = pd.DataFrame(data_resp["sample"], columns=dataset_columns)

        return dataset_info, dataset_columns, dataset_sample

    def get_data(self, dataset, limit=10000):
        """Fetch batch dataset from DB

        Here 'args' represent filters on dataset, given as dicts.

        Example:
        --------
        >> from factorymind.data_loader import FactoryDB
        >> mydb = FactoryDB()
        >> df = mydb.get_data("my_dataset", {"timestamp"})

        Arguments:
        ----------
        dataset : str
            Name of dataset (collection)
        limit : int, default 10000
            Number of datapoints (rows) to limit query to

        Returns:
        --------
        data : pd.DataFrame
            Dataset, limited to last "limit" records
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

    def run_custom_query(self, query):
        """Run custom SQL query towards DB

        Example:
        --------
        >> from factorymind.data_loader import FactoryDB
        >> mydb = FactoryDB()
        >> df = mydb.get_data("my_dataset", {"timestamp"})

        Arguments:
        ----------
        dataset : str
            Name of dataset (collection)
        limit : int, default 10000
            Number of datapoints (rows) to limit query to

        Returns:
        --------
        data : pd.DataFrame
            Dataset, limited to last "limit" records
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
