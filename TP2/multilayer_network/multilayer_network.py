from multilayer_network.hidden_layer import HiddenLayer
from multilayer_network.output_layer import OutputLayer
from utils.Perceptron import Perceptron
import numpy as np

class MultilayerNetwork:
    def __init__(self, layers_qty):
        hidden_layers = [HiddenLayer(3, 3, 0.01, lambda x: x, lambda x: 1) for i in range(layers_qty)]
        output_layer = OutputLayer(3, 3, 0.01, lambda x: x, lambda x: 1)
        self.layers = hidden_layers + [output_layer]
        self.layers_qty = layers_qty