"""
Setup to install the 'factorymind' Python package
"""

import os

from setuptools import find_packages, setup


def read(file_name: str):
    """Utility function to read the README file.

    Used for the long_description.  It's nice, because now
        1) we have a top level README file and
        2) it's easier to type in the README file than to put a raw
           string in belows 'setup()' config

    Args:
        file_name (str): Path to file
    """
    return open(os.path.join(os.path.dirname(__file__), file_name)).read()


install_requires = ["numpy", "pandas", "pytest"]

setup_requirements = ["pytest-runner", "better-setuptools-git-version"]

test_requirements = ["pytest", "nbformat"]

setup(
    author="FactoryMind AS",
    author_email="enquiry@factorymind.ai",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
    name="factorymind",
    # version="0.1.3",
    version_config={"version_format": "{tag}.dev{sha}", "starting_version": "0.0.1"},
    description="Python module `factorymind` for the FactoryMind platform",
    long_description=open("README.md").read(),
    packages=find_packages("src"),
    package_dir={"": "src"},
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    install_requires=install_requires,
)
