"""
pfriskmgmt config
==================================
Financial portfolio risk management framework. 
Code based on EDHEC Business School specialization course 'Investment Management with Python and Machine Learning'.
https://www.coursera.org/specializations/investment-management-python-machine-learning

Author: Casokaks (https://github.com/Casokaks/)
Created on: Aug 15th 2021

"""

# data path
from os.path import dirname, join
from pathlib import Path
DIR_NAME = str(Path(dirname(__file__)).parent)
DATA_PATH = join(DIR_NAME, 'data/')
