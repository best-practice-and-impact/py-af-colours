# py_af_colours
from setuptools import setup, find_packages

setup(
    name = "py_af_colours",
    version = "1.0.5",
    author = "Analysis standards and Pipelines team",
    author_email = "asap@ons.gov.uk",
    url = "https://best-practice-and-impact.github.io/py-af-colours/",
    install_requires = [
        "pyyaml"
        ],
    packages = find_packages(),
    include_package_data=True,
)