import numpy as np


class OutputLayer:
    def __init__(self, perceptrons_qty, input_dim, learning_rate, act_func, deriv_act_func):
        self.perceptrons_weights = np.random.uniform(low=0, high=0.3,size=(perceptrons_qty, 1 + input_dim))
        self.learning_rate = learning_rate
        self.act_func = act_func
        self.deriv_act_func= deriv_act_func

    def classifiy(self, example):
        x = np.dot(self.weights, np.append(1, example))
        return [self.act_func(x_i) for x_i in x]

    def update_weights(self, input):
        sigmas = []
        for weights in self.perceptrons_weights:
            h = np.dot(weights, np.append(1, input[:-1]))
            predicted = self.act_func(h)
            sigma =  (input[-1] - predicted) * self.deriv_act_func(h)
            weights += self.learning_rate * sigma * predicted

            sigmas.append(sigma)

        return sigmas
        