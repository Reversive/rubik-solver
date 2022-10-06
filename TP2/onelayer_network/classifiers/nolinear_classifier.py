from enum import Enum
from ...utils.DatasetUtils import DivideDatasetToTrainAndTest
from ...utils.Perceptron import Perceptron
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler, MaxAbsScaler

class NoLinearClassifier:
    def __init__(self, dataset_df, learning_rate, epochs, act_functions, BETA = 0.5):
        self.perceptron = Perceptron(input_dim=len(dataset_df.columns)-1, 
                                    learning_rate=learning_rate, 
                                    epochs=epochs, 
                                    act_func=lambda x: act_functions.value["act_func"](x, BETA), 
                                    deriv_act_func=lambda x: act_functions.value["deriv_act_func"](x, BETA)
                                    )
        self.output_scaler = act_functions.value["OUTPUT_SCALER"]
        self.classifier_type = act_functions.name
        self.dataset_df = dataset_df

    def execute(self, test_data_ratio = 0.1, batch_train = False):
        print(self.classifier_type + " exercise")

        # standarize inputs
        self.dataset_df.iloc[:,0:-1] = StandardScaler().fit_transform(self.dataset_df.iloc[:,0:-1])

        # scalar expected outputs
        self.dataset_df.iloc[:,-1:] = self.output_scaler.fit_transform(self.dataset_df.iloc[:,-1:])

        train_dataset_df, test_dataset_df = DivideDatasetToTrainAndTest(self.dataset_df, test_data_ratio)

        if batch_train:
            train_accuracies, test_accuracies = self.perceptron.train_batch(train_dataset_df.values, test_dataset_df.values)
        else:
            train_accuracies, test_accuracies = self.perceptron.train_online(train_dataset_df.values, test_dataset_df.values)
        
        print(f'Accuracy: {self.perceptron.test(test_dataset_df.values)}')
        return train_accuracies, test_accuracies
