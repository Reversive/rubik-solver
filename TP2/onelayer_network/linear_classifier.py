import math
from utils.DatasetUtils import DivideDatasetToTrainAndTest
from utils.Perceptron import Perceptron
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

class LinearClassifier:
    def __init__(self, linear_config):

        self.perceptron = Perceptron(input_dim=3, learning_rate=0.01, epochs=5)
        print("Linear exercise")
        dataset_df = pd.read_csv("./TP2-ej2-conjunto.csv", header=0)

        # standarize inputs
        dataset_df.iloc[:,0:-1] = StandardScaler().fit_transform(dataset_df.iloc[:,0:-1])

        # standarize expected outputs
        dataset_df.iloc[:,-1:] = StandardScaler().fit_transform(dataset_df.iloc[:,-1:])

        train_dataset_df, test_dataset_df = DivideDatasetToTrainAndTest(dataset_df, 0.8)

        self.perceptron.train_online(train_dataset_df.values)

                
        print(f'Total error: {self.perceptron.test(test_dataset_df.values)}')


