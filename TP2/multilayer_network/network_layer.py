import numpy as np

class NetworkLayer:
    def __init__(self, perceptrons_qty, input_dim, learning_rate, act_func, deriv_act_func):
        self.perceptrons_weights = np.random.uniform(low=0, high=0.3, size=(perceptrons_qty, input_dim + 1))
        # each row contains the weight of each perceptron for each input 
        self.learning_rate = learning_rate
        self.act_func = act_func
        self.deriv_act_func= deriv_act_func

    def classify(self, example):
        x = np.dot(np.append(1, example), self.perceptrons_weights.T)
        return self.act_func(x)

    def get_sigmas(self, input, inherit_sigmas):
        return inherit_sigmas * self.deriv_act_func(input)

    def update_weights(self, input, inherit_sigmas):
        self.perceptrons_weights += self.learning_rate * np.dot(np.matrix(inherit_sigmas).T, np.matrix(np.append(1, input)))
