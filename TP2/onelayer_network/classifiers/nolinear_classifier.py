from enum import Enum
from ...utils.DatasetUtils import DivideDatasetToTrainAndTest
from ...utils.Perceptron import Perceptron
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler, MaxAbsScaler

TANH_FUNC = lambda x, BETA: np.tanh(BETA * x)
EXP_FUNC = lambda x, BETA: 1/(1+np.exp(-2*BETA*x))
class NoLinearClassifierType(Enum):
    TANH = {
        "act_func": TANH_FUNC, 
        "deriv_act_func" : lambda x, BETA: BETA*(1 - TANH_FUNC(x,BETA)**2),
        "OUTPUT_SCALER": MinMaxScaler(feature_range=(-1,1))
    }
    EXP = {
        "act_func": EXP_FUNC, 
        "deriv_act_func" : lambda x, BETA: EXP_FUNC(x,BETA)*(1 - EXP_FUNC(x,BETA)),
        "OUTPUT_SCALER": MinMaxScaler() # default range is (0,1)
    }
    RELU = {
        "act_func": lambda x, BETA: max(0,BETA*x),
        "deriv_act_func" : lambda x, BETA: BETA if x > 0 else 0,
        "OUTPUT_SCALER": MinMaxScaler() # default range is (0,1)
    }


class NoLinearClassifier:
    def __init__(self, dataset_df, learning_rate, epochs, CLASSIFIER_TYPE, BETA = 0.5):
        self.perceptron = Perceptron(input_dim=len(dataset_df.columns)-1, 
                                    learning_rate=learning_rate, 
                                    epochs=epochs, 
                                    act_func=lambda x: CLASSIFIER_TYPE.value["act_func"](x, BETA), 
                                    deriv_act_func=lambda x: CLASSIFIER_TYPE.value["deriv_act_func"](x, BETA),
                                    )
        self.output_scaler = CLASSIFIER_TYPE.value["OUTPUT_SCALER"]
        self.classifier_type = CLASSIFIER_TYPE.name
        self.dataset_df = dataset_df

    def execute(self, test_data_ratio = 0.1, batch_train = False):
        print(self.classifier_type + " exercise")

        # standarize inputs
        self.dataset_df.iloc[:,0:-1] = StandardScaler().fit_transform(self.dataset_df.iloc[:,0:-1])

        # scalar expected outputs
        self.dataset_df.iloc[:,-1:] = self.output_scaler.fit_transform(self.dataset_df.iloc[:,-1:])

        train_dataset_df, test_dataset_df = DivideDatasetToTrainAndTest(self.dataset_df, test_data_ratio)

        if batch_train:
            self.perceptron.train_batch(train_dataset_df.values, test_dataset_df.values)
        else:
            self.perceptron.train_online(train_dataset_df.values, test_dataset_df.values)
        
        print(f'Accuracy: {self.perceptron.test(test_dataset_df.values)}')
