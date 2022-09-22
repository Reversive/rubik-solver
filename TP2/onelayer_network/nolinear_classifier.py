from enum import Enum
from utils.DatasetUtils import DivideDatasetToTrainAndTest
from utils.Perceptron import Perceptron
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
        "OUTPUT_SCALER": MinMaxScaler(feature_range=(0,1))
    }


class NoLinearClassifier:
    def __init__(self, CLASSIFIER_TYPE, BETA = 0.5, epochs = 5):
        self.perceptron = Perceptron(input_dim=3, learning_rate=0.01, epochs=epochs, 
                                    act_func=lambda x: CLASSIFIER_TYPE.value["act_func"](x, BETA), 
                                    deriv_act_func=lambda x: CLASSIFIER_TYPE.value["deriv_act_func"](x, BETA))
        self.output_scaler = CLASSIFIER_TYPE.value["OUTPUT_SCALER"]
        self.classifier_type = CLASSIFIER_TYPE.name

    def execute(self):
        print(f"NoLinear {self.classifier_type}")
        dataset_df = pd.read_csv("./TP2-ej2-conjunto.csv", header=0)

        # standarize inputs
        dataset_df.iloc[:,0:-1] = StandardScaler().fit_transform(dataset_df.iloc[:,0:-1])

        # scalar expected outputs
        dataset_df.iloc[:,-1:] = self.output_scaler.fit_transform(dataset_df.iloc[:,-1:])

        train_dataset_df, test_dataset_df = DivideDatasetToTrainAndTest(dataset_df, 0.8)

        self.perceptron.train_online(train_dataset_df.values)
        


        print(f'Total error: {self.perceptron.test(test_dataset_df.values)}')
