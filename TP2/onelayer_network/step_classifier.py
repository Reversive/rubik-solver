from utils.Perceptron import Perceptron
import numpy as np


class StepClassifier:
    def __init__(self, dataset, learning_rate, epochs, umbral = 0):
        self.perceptron = Perceptron(input_dim=len(dataset[0]) -1, learning_rate=learning_rate,\
             epochs=epochs, act_func=lambda x: np.sign(x - umbral))
        self.dataset = dataset

    def execute(self):
        self.perceptron.train_online(self.dataset)
        print(f'Total error: {self.perceptron.test(self.dataset)}')
