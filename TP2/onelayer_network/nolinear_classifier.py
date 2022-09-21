from utils.Perceptron import Perceptron
import pandas as pd
import numpy as np


class NoLinearClassifier:

    def __init__(self):
        BETA = 0.5
        g = lambda x: np.tanh(BETA * x)

        self.perceptron = Perceptron(3, 0.01, act_func=g, deriv_act_func=lambda x: BETA*(1 - g(x)**2))
        print("NoLinear exercise")
        train_dataset = pd.read_csv("./TP2-ej2-conjunto.csv", header=0)

        # scalar expected outputs
        max = train_dataset["y"].max()
        min = train_dataset["y"].min()
        print(min,max)
        for i in range(len(train_dataset)):
            train_dataset.values[i][-1] = 2*(train_dataset.values[i][-1] - min) / (max - min) -1

        print(train_dataset)

        self.perceptron.train(train_dataset.values.tolist())
        
        corrects_qualifications = 0
        for i in range(len(train_dataset)):
            result = self.perceptron.test(train_dataset.values[i][:-1])
            predicted = train_dataset.values[i][-1]
            print(result, predicted, i)
            if result == predicted:
                corrects_qualifications += 1

        print(f'Corrects qualifications: {corrects_qualifications}, incorrects: {len(train_dataset) - corrects_qualifications}')
