from typing import Deque
from .output_layer import OutputLayer
from .hidden_layer import HiddenLayer
import numpy as np

class MultilayerNetwork:
    def __init__(self, layers_qty):
        hidden_layers = [HiddenLayer(4, 2, 0.01, lambda x: x, lambda x: 1)]
        output_layer = OutputLayer(1, 4, 0.01, lambda x: x, lambda x: 1)

        self.layers = hidden_layers + [output_layer]

    def train(self, train_data):
        for example in train_data:
            input = example[:-1]
            layers_input = [input]

            for layer in self.layers:
                layers_input.append(layer.classify(layers_input[-1]))

            weighted_sigmas = Deque()
            weighted_sigmas.appendleft(self.layers[-1].get_weighted_sigmas(layers_input[-2], example[2]))
            self.layers[-1].update_weights(weighted_sigmas[0])

            for m in range(len(self.layers) - 2, -1, -1):
                weighted_sigmas.appendleft(self.layers[m].get_weighted_sigmas(layers_input[m], weighted_sigmas[0]))
                self.layers[m].update_weights(weighted_sigmas[0])
        

    def classify(self, example):
        for layer in self.layers:
            example = layer.classify(example)

        return example

    