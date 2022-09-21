from utils.Perceptron import Perceptron
import numpy as np


class StepClassifier:
    def __init__(self):
        UMBRAL = 0
        self.perceptron = Perceptron(2, 0.01, lambda x: np.sign(x - UMBRAL))

        print("AND exercise")
        and_train_dataset = [[-1, 1, -1], [1, -1, -1], [-1, -1, -1], [1, 1, 1]]
        self.perceptron.train(and_train_dataset)

        corrects_qualifications = 0
        for i in range(len(and_train_dataset)):
            if self.perceptron.test(and_train_dataset[i][:-1]) == and_train_dataset[i][-1]:
                corrects_qualifications += 1
        print(f'Corrects qualifications: {corrects_qualifications}, incorrects: {len(and_train_dataset) - corrects_qualifications}')

        print("XOR exercise")
        xor_train_dataset = [[-1, 1, 1], [1, -1, 1], [-1, -1, -1], [1, 1, -1]]
        self.perceptron.train(xor_train_dataset)

        corrects_qualifications = 0
        for i in range(len(xor_train_dataset)):
            if self.perceptron.test(xor_train_dataset[i][:-1]) == xor_train_dataset[i][-1]:
                corrects_qualifications += 1
        print(f'Corrects qualifications: {corrects_qualifications}, incorrects: {len(xor_train_dataset) - corrects_qualifications}')


