from utils.Perceptron import Perceptron
import numpy as np


class StepClassifier:
    def __init__(self):
        self.perceptron = Perceptron(np.sign, 2, 0.01)
        self.perceptron.train([[1, 1, 1], [0, 1, 0], [1, 0, 0], [0, 0, 0]])
        print(self.perceptron.test([1, 1]))
        print(self.perceptron.test([0, 1]))
        print(self.perceptron.test([1, 0]))
        print(self.perceptron.test([0, 0]))

        self.perceptron = Perceptron(np.sign, 2, 0.01)
        self.perceptron.train([[1, 1, 0], [0, 1, 1], [1, 0, 1], [0, 0, 0]])
        print(self.perceptron.test([1, 1]))
        print(self.perceptron.test([0, 1]))
        print(self.perceptron.test([1, 0]))
        print(self.perceptron.test([0, 0]))
