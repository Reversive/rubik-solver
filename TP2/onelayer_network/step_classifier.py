from utils.Perceptron import Perceptron
import numpy as np


class StepClassifier:
    def __init__(self):
        UMBRAL = 0
        self.perceptron = Perceptron(input_dim=2, learning_rate=0.01, epochs=5, act_func=lambda x: np.sign(x - UMBRAL))

        print("AND exercise")
        and_train_dataset = [[-1, 1, -1], [1, -1, -1], [-1, -1, -1], [1, 1, 1]]
        self.perceptron.train_online(and_train_dataset)
  
        print(f'Total error: {self.perceptron.test(and_train_dataset)}')
                

        print("XOR exercise")
        xor_train_dataset = [[-1, 1, 1], [1, -1, 1], [-1, -1, -1], [1, 1, -1]]
        self.perceptron.train_online(xor_train_dataset)

        print(f'Total error: {self.perceptron.test(xor_train_dataset)}')
