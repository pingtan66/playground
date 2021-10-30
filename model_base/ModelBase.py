import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn import preprocessing
import sklearn.metrics as metrics

import typing

class ModelBase(object):

    def __init__(self, processor, csv_file_name: str, seed, logger=None):

        self.scaler = preprocessing.StandardScaler()
        self.seed = seed
        self.processor = processor
        self.csv_file_name = csv_file_name
