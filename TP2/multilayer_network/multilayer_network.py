from utils.Perceptron import Perceptron
import numpy as np

class MultilayerNetwork:
    def __init__(self, layers_qty):
        self.layers = [[Perceptron(np.sign, 2, 0.01) for i in range(layers_qty)] for j in range(layers_qty)]
        self.layers_qty = layers_qty