"""
Test suite for example functions
"""

import os
import sys

import pytest

from factorymind import examplemodule

# Explicitly set path so don't need to run setup.py - if we have multiple
# copies of the code we would otherwise need to setup a separate environment
# for each to ensure the code pointers are correct.
sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "src"))
)  # noqa

# from pandas.util.testing import assert_frame_equal


def test_hello_world():
    """Test hello world"""
    assert (
        examplemodule.hello_world() == "Hello World"
    ), "The Hello World strings should be the same"


def test_add_value_to_numpy_wrong_type():
    """Test add_value_to_numpy with wrong type"""
    with pytest.raises(ValueError) as _:
        examplemodule.add_value_to_numpy([1, 1], 1)


def test_add_value_to_numpy_empty():
    """Test add_value_to_numpy with empty type"""
    with pytest.raises(ValueError) as _:
        examplemodule.add_value_to_numpy(None, 1)
