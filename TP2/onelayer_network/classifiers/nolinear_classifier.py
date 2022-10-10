from enum import Enum
from ...utils.dataset_utils import DivideDatasetDfToTrainAndTest
from ...utils.perceptron import Perceptron
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
        self.output_transform = act_functions.value["output_transform"]
        self.classifier_type = act_functions.name
        self.dataset_df = dataset_df

    def execute(self, train_dataset_df = None, test_dataset_df = None, train_data_ratio = 0.9, batch_train = False):
        print(self.classifier_type + " exercise")

        # standarize inputs
        self.dataset_df.iloc[:,0:-1] = StandardScaler().fit_transform(self.dataset_df.iloc[:,0:-1])

        # scalar expected outputs
        self.dataset_df.iloc[:,-1:] = self.output_transform.fit_transform(self.dataset_df.iloc[:,-1:])

        if train_dataset_df is None or test_dataset_df is None:
            train_dataset_df, test_dataset_df = DivideDatasetDfToTrainAndTest(self.dataset_df, train_data_ratio)

        if batch_train:
            train_accuracies, test_accuracies, train_errors, test_errors = self.perceptron.train_batch(train_dataset_df.values, test_dataset_df.values)
        else:
            train_accuracies, test_accuracies, train_errors, test_errors = self.perceptron.train_online(train_dataset_df.values, test_dataset_df.values)
        
        print(f'Accuracy: {test_accuracies[-1]}')
        return train_accuracies, test_accuracies, train_errors, test_errors


class NoLinearClassifierType:
    pass



