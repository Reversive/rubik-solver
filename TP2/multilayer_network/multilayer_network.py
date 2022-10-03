from .network_layer import NetworkLayer
import numpy as np

class MultilayerNetwork:
    def __init__(self, layers_qty):
        hidden_layers = [NetworkLayer(4, 2, 0.01, lambda x: x, lambda x: 1) for i in range(layers_qty)]
        output_layer = NetworkLayer(1, 4, 0.01, lambda x: x, lambda x: 1)

        self.layers = hidden_layers + [output_layer]

    def train(self, train_data):
        for example in train_data:
            activation_per_layer = [example[:-1]]
            for index, layer in enumerate(self.layers):
                input = activation_per_layer[index] # input for each layer is the output of the previous layer
                activation_per_layer.append(layer.classify(input))


            input = activation_per_layer[-1]
            inherit_error = [a - b for a, b in zip(example[-1], input)]
            inherit_sigmas = self.layers[-1].get_sigmas(input, inherit_error)

            for index in range(len(self.layers) - 1, -1, -1):
                current_layer = self.layers[index]
                current_layer.update_weights(activation_per_layer[index], inherit_sigmas)

                non_bias_weights = np.delete(current_layer.perceptrons_weights, 0, 1)
                inherit_sigmas = current_layer.get_sigmas(activation_per_layer[index], 
                                        np.dot(inherit_sigmas, non_bias_weights))


    def classify(self, example):
        for layer in self.layers:
            example = layer.classify(example)

        return example

    