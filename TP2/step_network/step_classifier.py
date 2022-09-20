from utils.Perceptron import Perceptron
import numpy as np


class StepClassifier:
    def __init__(self):
        self.perceptron = Perceptron(np.sign, 2, 0.01)
        train_dataset = [[1, 1, 1], [0, 1, -1], [1, 0, -1], [0, 0, -1]]
        self.perceptron.train(train_dataset)
        print(self.perceptron.test([1, 1]) == 1)
        print(self.perceptron.test([0, 1]) == -1)
        print(self.perceptron.test([1, 0]) == -1)
        print(self.perceptron.test([0, 0]) == -1)
