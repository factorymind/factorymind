"""
Test suite for factorymind.timingutils
"""

import logging
import os
import sys

import pytest

from factorymind import timing_utils

# Explicitly set path so don't need to run setup.py - if we have multiple
# copies of the code we would otherwise need to setup a separate environment
# for each to ensure the code pointers are correct.
sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "src"))
)  # noqa


def test_setup_logger():
    """Test setup logger function"""
    assert isinstance(
        timing_utils.setup_logger("test_logger"), logging.Logger
    ), "Should return a Logger object"
    with pytest.raises(TypeError):
        _ = timing_utils.setup_logger(1)


def test_timeit_context():
    """Test timeit context function"""
    return
