"""
Utility functions for timing (e.g. tic-yoc functionality)

Code documentation
^^^^^^^^^^^^^^^^^^
"""
import logging
import time

# Import standard modules
from contextlib import contextmanager


@contextmanager
def timeit_context(name: str, logger=None, space="  ", logging_level="debug", tic=None):
    """Time a piece of code

    Example
        ^^^^^^^
        .. code-block:: python

            >>> from factorymind.timing_utils import timeit_context

            >>> with timeit_context("Time to do some random list computation"):
                    l = [i ** 2 for i in range(10000000)]
                    del l
    """
    if logger is None:
        logger = logging.getLogger("root")
    tic = time.time() if tic is None else tic
    yield
    elapsedTime = time.time() - tic
    if logging_level == "info":
        # logging.basicConfig(level=logging.INFO)
        logger.info(space + "{}: {:.2f} sec".format(name, elapsedTime))
    elif logging_level == "debug":
        # logging.basicConfig(level=logging.DEBUG)
        logger.debug(space + "{}: {:.2f} sec".format(name, elapsedTime))


def setup_logger(name):
    r"""Set up custom logger

    **References**

    * Stackoverflow \: `Python logging module globally <https://stackoverflow.com/questions/7621897/python-logging-module-globally>`_
    """
    formatter = logging.Formatter(
        fmt="%(levelname)s:  %(asctime)s - %(module)s - %(message)s",
        datefmt="%Y/%m/%d %H:%M:%S",
    )

    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    # logger.addHandler(handler)

    return logger
