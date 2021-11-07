"""
These are custom FM exception classes.

References:
- https://towardsdatascience.com/how-to-define-custom-exception-classes-in-python-bfa346629bca
"""


class FactoryMindException(Exception):
    """Base class for other exceptions"""

    def __init__(self, msg="FMException"):
        self.message = msg
        super().__init__(self.message)


class CouldNotFetchDataException(FactoryMindException):
    """Raised when data cannot be fetched from FM database"""

    def __init__(self, msg="Could not fetch data from the FactoryMind DB"):
        self.message = msg
        super().__init__(self.message)

    def __str__(self):
        """Objects own message (self.message)"""
        if self.message:
            return "CouldNotFetchDataException, {} ".format(self.message)
        else:
            return "CouldNotFetchDataException has been raised"


class DatasetDoesNotExistException(FactoryMindException):
    """Raised when dataset (collection) does not exist in DB"""

    def __init__(
        self,
        dataset_name="",
        msg="",
    ):
        self.message = (
            msg
            + f"Could not find dataset in FactoryMind DB that matches the name '{dataset_name}'. Please check name of dataset."
        )
        super().__init__(self.message)
