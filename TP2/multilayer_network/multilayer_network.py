from typing import Deque
import numpy as np
import math

MIN_ERROR_TRESHOLD = np.exp(-10000)
PREDICTION_THRESHOLD = 0.001


class MultilayerNetwork:
    def __init__(self, hidden_layers_perceptron_qty, input_dim, output_dim, learning_rate, epochs, act_func,
                 deriv_act_func):
        self.act_func = act_func
        self.deriv_act_func = deriv_act_func
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.output_dim = output_dim

        self.hidden_layers_perceptron_qty = hidden_layers_perceptron_qty
        self.layers_size = [input_dim] + hidden_layers_perceptron_qty + [output_dim]
        self.layers_weights = []

        # adam
        self.alpha = 0.001
        self.beta_1 = 0.9
        self.beta_2 = 0.999
        self.adam_error = 10 ^ -8
        self.t = 0

        for i in range(len(self.layers_size) - 1):
            self.layers_weights.append(
                np.random.uniform(low=-1, high=1, size=(self.layers_size[i + 1], self.layers_size[i] + 1)))
            # cantidad de pesos es lo que toma de input +1 por el BIAS

    def forward_propagation(self, example):
        example = np.append(example, 1)  # add bias
        self.V = [example]
        self.H = [example]

        for m in range(len(self.layers_weights) - 1):
            self.H.append(np.append(np.dot(self.layers_weights[m], example), 1))
            self.V.append(self.act_func(self.H[-1]))
            example = self.V[-1]

        # output layer doesnt have BIAS
        self.H.append(np.dot(self.layers_weights[-1], example))
        self.V.append(self.act_func(self.H[-1]))

        return self.V[-1]

    def back_propagation(self, expected_output):
        sigmas = Deque()
        sigmas.append(self.deriv_act_func(self.H[-1]) * (expected_output - self.V[-1]))

        for m in range(len(self.layers_weights) - 2, -1, -1):
            sigmas.appendleft(self.deriv_act_func(self.H[m + 1]) * np.dot(self.layers_weights[m + 1].T, sigmas[0]))
            sigmas[0] = sigmas[0][:-1]  # remove bias of the one just added

        if False:
            self.gradient_descent(sigmas)
        else:
            self.adam(sigmas)

    def gradient_descent(self, sigmas):
        deltas = Deque()
        for m in range(len(self.layers_weights)):
            deltas.append(self.learning_rate * np.dot(np.matrix(sigmas[m]).T, np.matrix(self.V[m])))
        for m in range(len(self.layers_weights)):
            self.layers_weights[m] += deltas[m]
            # self.layers_weights[m] = np.add(self.layers_weights[m], deltas[m])

    def adam(self, sigmas):
        for m in range(1, len(self.layers_weights)):
            adam_m = 0
            adam_v = 0
            t = 0
            while t < 500:
                # g_t = sigmas, tita = self.layers_weights
                adam_m = self.beta_1 * adam_m + (1 - self.beta_1) * sigmas[m]
                adam_v = self.beta_2 * adam_v + (1 - self.beta_2) * np.power(sigmas[m], 2)
                adam_prime_m = adam_m / (1 - (np.power(self.beta_1, m)))
                adam_prime_v = adam_v / (1 - (np.power(self.beta_2, m)))
                self.layers_weights[m] = np.subtract(self.layers_weights[m], self.alpha * np.matrix(adam_prime_m).T / (
                        np.sqrt(adam_prime_v) + self.adam_error))
                t += 1

    def train_batch(self, train_data, test_data=None):
        continue_condition = lambda i, error_min: i < len(train_data)
        return self.train(train_data, continue_condition, test_data=test_data)

    def train_online(self, train_data, test_data=None):
        continue_condition = lambda i, error_min: error_min > MIN_ERROR_TRESHOLD and i < len(train_data)
        return self.train(train_data, continue_condition, lambda: np.random.choice(len(train_data)), test_data)

    def cuadratic_error(self, output, expected):
        error = 0
        for j in range(self.output_dim):
            error += pow(expected[j] - output[j], 2)
        return error

    def cuadratic_mean_error(self, test_data):
        error = 0
        for i in range(len(test_data)):
            output = self.forward_propagation(test_data[i][0])
            expected = test_data[i][1]
            error += self.cuadratic_error(output, expected)

        return error / len(test_data)

    def train(self, train_data, continue_condition, next_example_idx_generator=None, test_data=None):
        error_min = float('inf')
        w_min = self.layers_weights
        iterations = 0

        train_accuracies = []
        test_accuracies = []
        for epoch in range(self.epochs):
            epoch_error_min = float('inf')
            iteration = 0
            epoch_w_min = self.layers_weights

            while continue_condition(iteration, error_min):
                example = train_data[
                    next_example_idx_generator() if next_example_idx_generator is not None else iteration]
                input = example[0]
                output = example[1]
                self.forward_propagation(input)
                self.back_propagation(output)

                epoch_error = self.cuadratic_mean_error(train_data)
                if epoch_error < epoch_error_min:
                    epoch_error_min = epoch_error
                    epoch_w_min = self.layers_weights

                iteration += 1

            # use best epoch weights
            self.layers_weights = epoch_w_min

            error = self.cuadratic_mean_error(train_data)
            if error < error_min:
                error_min = error
                w_min = self.layers_weights

            iterations += iteration  # add epoc iterations to total iterations

        self.layers_weights = w_min
        print(f'Error min: {error_min}, iterations: {iterations}')
        # print("weights: ")
        # for i in range(len(self.layers_weights)):
        #     print("Layer ", i)
        #     print(self.layers_weights[i])

        return train_accuracies, test_accuracies
