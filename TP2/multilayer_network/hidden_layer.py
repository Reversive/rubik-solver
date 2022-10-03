import numpy as np

class HiddenLayer:
    def __init__(self, perceptrons_qty, input_dim, learning_rate, act_func, deriv_act_func):
        self.perceptrons_weights = np.random.uniform(low=-1, high=1, size=(perceptrons_qty, input_dim + 1))
        # each row contains the weight of each perceptron for each input 
        self.learning_rate = learning_rate
        self.act_func = act_func
        self.deriv_act_func= deriv_act_func
        self.perceptrons_qty = perceptrons_qty

    def classify(self, input):
        return self.act_func(self.get_h(input))

    def get_h(self, input):
        return np.dot(self.perceptrons_weights, np.append(input, 1))

    def get_weighted_sigmas(self, input, inherited_weighted_sigmas):
        sigmas = np.zeros(self.perceptrons_qty)

        for i, h_i in enumerate(self.get_h(input)):
            sigmas[i] = self.deriv_act_func(h_i) * inherited_weighted_sigmas[i]

        return np.dot(self.perceptrons_weights.T, sigmas)

    def update_weights(self, delta):
        self.perceptrons_weights += delta * self.learning_rate
        print(self.perceptrons_weights)
    