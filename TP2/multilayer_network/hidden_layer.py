import numpy as np



class HiddenLayer:
    def __init__(self, perceptrons_qty, input_dim, learning_rate, act_func, deriv_act_func):
        self.perceptrons_weights = np.random.uniform(low=0, high=0.3,size=(perceptrons_qty, 1 + input_dim))
        self.learning_rate = learning_rate
        self.act_func = act_func
        self.deriv_act_func= deriv_act_func

    def classifiy(self, example):
        x = np.dot(self.perceptrons_weights, np.append(1, example))
        return [self.act_func(x_i) for x_i in x]

    def update_weights(self, input, sigmas):
        new_sigmas = []
        for weights, sigma in zip(self.perceptrons_weights, sigmas):
            h = np.dot(self.perceptrons_weights, np.append(1, input[:-1]))
            predicted = self.act_func(h)
            
            new_sigma = self.deriv_act_func(h) * np.dot(weights, sigma)
            weights += self.learning_rate * new_sigma * predicted

            new_sigmas.append(new_sigma)

        return new_sigmas
                