from utils.Perceptron import Perceptron
import pandas as pd
import numpy as np


class LinearClassifier:
    def __init__(self):
        self.perceptron = Perceptron(3, 0.01)
        print("Linear exercise")
        train_dataset = pd.read_csv("./TP2-ej2-conjunto.csv", header=0)
        self.perceptron.train(train_dataset.values)
        
        corrects_qualifications = 0
        for i in range(len(train_dataset)):
            result = self.perceptron.test(train_dataset.values[i][:-1])
            predicted = train_dataset.values[i][-1]
            print(result, predicted, i)
            if result == predicted:
                corrects_qualifications += 1
                
        print(f'Corrects qualifications: {corrects_qualifications}, incorrects: {len(train_dataset) - corrects_qualifications}')


