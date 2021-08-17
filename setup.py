"""
Package setup
==================================

Author: Casokaks (https://github.com/Casokaks/)
Created on: Aug 15th 2021

"""

from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='pfriskmgmt',
    version='0.0.1',
    author='Casokaks',
    author_email='casokaks@gmail.com',
    description='Financial portfolio risk management framework.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/Casokaks/pfriskmgmt',
    project_urls = {
        "Bug Tracker": "https://github.com/Casokaks/pfriskmgmt/issues"
    },
    license='MIT',
    packages=['pfriskmgmt'],
    install_requires=[
        'pandas', 
        'numpy', 
        'scipy', 
        'statsmodels', 
    ],  
)

