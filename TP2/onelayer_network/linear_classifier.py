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

        self.perceptron.train_online(train_dataset_df.values, test_dataset_df.values)

        corrects_qualifications = 0
        for i in range(len(train_dataset_df)):
            result = self.perceptron.test(train_dataset_df.values[i][:-1])
            predicted = train_dataset_df.values[i][-1]
            print(result, predicted, i)
            if result == predicted:
                corrects_qualifications += 1
                
        print(f'Corrects qualifications: {corrects_qualifications}, incorrects: {len(train_dataset_df) - corrects_qualifications}')


