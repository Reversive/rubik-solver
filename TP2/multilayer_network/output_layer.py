import numpy as np

from .hidden_layer import HiddenLayer

class OutputLayer(HiddenLayer):
    def __init__(self, perceptrons_qty, input_dim, learning_rate, act_func, deriv_act_func):
        super().__init__(perceptrons_qty, input_dim, learning_rate, act_func, deriv_act_func)

    def get_weighted_sigmas(self, input, expected_outputs):
        # output x (input +1) º (input +1) x1

        h = self.get_h(input)
        sigmas = np.zeros(self.perceptrons_qty)

        for i, h_i in enumerate(h):
            output = self.act_func(h_i)
            sigmas[i] = self.deriv_act_func(h) * (expected_outputs[i] - output) 

        return np.dot(self.perceptrons_weights.T, sigmas)



