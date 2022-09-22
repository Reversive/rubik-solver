from enum import Enum
from utils.Perceptron import Perceptron
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler, MaxAbsScaler

class NoLinearClassifierType(Enum):
    TANH = {
        "act_func": lambda x, BETA: np.tanh(BETA * x), 
        "deriv_act_func" : lambda x, BETA: BETA*(1 - np.tanh(BETA * x)**2),
        "OUTPUT_SCALER": MinMaxScaler(feature_range=(-1,1))
    }
    EXP = {
        "act_func": lambda x, BETA: 1/(1+np.exp(2*BETA*x)), 
        "deriv_act_func" : lambda x, BETA: 2*BETA*(1/(1+np.exp(2*BETA*x)))*(1 - 1/(1+np.exp(2*BETA*x))),
        "OUTPUT_SCALER": MinMaxScaler(feature_range=(0,1))
    }


class NoLinearClassifier:
    def __init__(self, CLASSIFIER_TYPE, BETA = 0.5):
        self.perceptron = Perceptron(3, 0.01, 
                                    act_func=lambda x: CLASSIFIER_TYPE.value["act_func"](x, BETA), 
                                    deriv_act_func=lambda x: CLASSIFIER_TYPE.value["deriv_act_func"](x, BETA))
        self.output_scaler = CLASSIFIER_TYPE.value["OUTPUT_SCALER"]

    def execute(self):
        print("NoLinear exercise")
        train_dataset_df = pd.read_csv("./TP2-ej2-conjunto.csv", header=0)

        # standarize inputs
        train_dataset_df.iloc[:,0:-1] = StandardScaler().fit_transform(train_dataset_df.iloc[:,0:-1])

        # scalar expected outputs
        train_dataset_df.iloc[:,-1:] = self.output_scaler.fit_transform(train_dataset_df.iloc[:,-1:])

        self.perceptron.train(train_dataset_df.values.tolist())
        
        corrects_qualifications = 0
        for i in range(len(train_dataset_df)):
            result = self.perceptron.test(train_dataset_df.values[i][:-1])
            predicted = train_dataset_df.values[i][-1]
            print(result, predicted, i)
            if result == predicted:
                corrects_qualifications += 1

        print(f'Corrects qualifications: {corrects_qualifications}, incorrects: {len(train_dataset_df) - corrects_qualifications}')

