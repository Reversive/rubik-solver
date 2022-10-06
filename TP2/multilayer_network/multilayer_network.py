from typing import Deque
import numpy as np

class MultilayerNetwork:
    def __init__(self, hidden_layers_perceptron_qty, input_dim, output_dim, learning_rate):
        self.act_func = lambda x: np.sign(x)
        self.deriv_act_func = lambda x: 1
        self.learning_rate = learning_rate
        
        self.hidden_layers_perceptron_qty = hidden_layers_perceptron_qty
        self.layers_size = [input_dim] + hidden_layers_perceptron_qty + [output_dim]
        self.layers_weights = []
        for i in range(len(self.layers_size)-1):
            self.layers_weights.append(np.random.uniform(low=-1, high=1, size=(self.layers_size[i+1], self.layers_size[i] +1))) 
            # cantidad de pesos es lo que toma de input +1 por el BIAS

    def feed_forward(self, example):
        example = np.append(example, 1) # add bias
        self.V = [example]
        self.H = [example]

        for m in range(len(self.layers_weights)-1):
            self.H.append(np.append(np.dot(self.layers_weights[m], example), 1))
            self.V.append(self.act_func(self.H[-1]))
            example = self.V[-1]
        
        # output layer doesnt have BIAS
        self.H.append(np.dot(self.layers_weights[-1], example))
        self.V.append(self.act_func(self.H[-1]))

        return self.V[-1]

    def back_propagation(self, expected_output):
        sigmas = Deque()
        sigmas.append(self.deriv_act_func(self.H[-1])*(expected_output - self.V[-1]))
        
        for m in range(len(self.layers_weights)-2, -1, -1):
            sigmas.appendleft(self.deriv_act_func(self.H[m+1]) * np.dot(self.layers_weights[m+1].T, sigmas[0]))
            sigmas[0] = sigmas[0][:-1] # remove bias of the one just added

        deltas = Deque()
        for m in range(len(self.layers_weights)):
            deltas.append(self.learning_rate * np.dot(np.matrix(sigmas[m]).T, np.matrix(self.V[m])))

        for m in range(len(self.layers_weights)):
            self.layers_weights[m] += deltas[m]

    def train(self, examples, epochs):
        for epoch in range(epochs):
            for example in examples:
                input = example[:-1]
                output = example[-1]
                self.feed_forward(input)
                self.back_propagation(output)
