import math
from ...utils.DatasetUtils import DivideDatasetToTrainAndTest
from ...utils.Perceptron import Perceptron
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler


class LinearClassifier:

    def __init__(self, dataset_df, learning_rate, epochs):
        self.perceptron = Perceptron(input_dim=len(dataset_df.columns)-1, learning_rate=learning_rate, epochs=epochs)
        self.dataset_df = dataset_df

    def execute(self):
        print("Linear exercise")
        # standarize inputs
        self.dataset_df.iloc[:,0:-1] = StandardScaler().fit_transform(self.dataset_df.iloc[:,0:-1])

        # standarize expected outputs
        self.dataset_df.iloc[:,-1:] = StandardScaler().fit_transform(self.dataset_df.iloc[:,-1:])

        train_dataset_df, test_dataset_df = DivideDatasetToTrainAndTest(self.dataset_df, 0.75)

        self.perceptron.train_online(train_dataset_df.values, test_dataset_df.values)

                
        print(f'Accuracy: {self.perceptron.test(test_dataset_df.values)}')


