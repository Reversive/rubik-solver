from typing import Deque
import numpy as np
import math
import csv

MIN_ERROR_TRESHOLD = np.exp(-10000)
WEIGHTS_BACKUP_DIR = 'TP3/data/weights_backup.txt'

class MultilayerNetwork:
    def __init__(self, hidden_layers_perceptron_qty, input_dim, output_dim, learning_rate, epochs, act_func,
                 deriv_act_func, momentum_alpha = 0.8):
        self.act_func = act_func
        self.deriv_act_func = deriv_act_func
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.output_dim = output_dim

        self.hidden_layers_perceptron_qty = hidden_layers_perceptron_qty
        self.layers_size = [input_dim] + hidden_layers_perceptron_qty + [output_dim]
        self.layers_weights = []

        # adam
        # self.momentum_alpha = 0.001
        # self.beta_1 = 0.9
        # self.beta_2 = 0.999
        # self.adam_error = 10 ^ -8
        # self.t = 1
        # self.adam_m = []
        # self.adam_v = []

        # momentum
        self.deltas = []
        self.momentum_alpha = momentum_alpha

        for i in range(len(self.layers_size) - 1):
            # self.adam_m.append(np.zeros(self.layers_size[i + 1]))
            # self.adam_v.append(np.zeros(self.layers_size[i + 1]))
            self.deltas.append(np.zeros([self.layers_size[i + 1], self.layers_size[i] + 1]))
            self.layers_weights.append(
                np.random.uniform(low=-1, high=1, size=(self.layers_size[i + 1], self.layers_size[i] + 1)))
            # cantidad de pesos es lo que toma de input +1 por el BIAS

    def forward_propagation(self, example, start_layer=0):
        example = np.append(example, 1)  # add bias
        self.V = [example]
        self.H = [example]
        for m in range(start_layer, len(self.layers_weights) - 1):
            self.H.append(np.append(np.dot(self.layers_weights[m], example), 1))
            self.V.append(self.act_func(self.H[-1]))
            self.V[-1][-1] = 1
            example = self.V[-1]

        # output layer doesnt have BIAS
        self.H.append(np.dot(self.layers_weights[-1], example))
        self.V.append(self.act_func(self.H[-1]))

        return self.V[-1]

    def forward_propagation_from_latent_space(self, example):
        return self.forward_propagation(example, start_layer=int((len(self.layers_size)-1)/2))

    def back_propagation(self, expected_output):
        sigmas = Deque()
        sigmas.append(self.deriv_act_func(self.H[-1]) * (expected_output - self.V[-1]))

        for m in range(len(self.layers_weights) - 2, -1, -1):
            sigmas.appendleft(self.deriv_act_func(self.H[m + 1]) * np.dot(self.layers_weights[m + 1].T, sigmas[0]))
            sigmas[0] = sigmas[0][:-1]  # remove bias of the one just added

        self.gradient_descent(sigmas)

    def gradient_descent(self, sigmas):
        for m in range(len(self.layers_weights)):
            new_delta = self.learning_rate * np.dot(np.matrix(sigmas[m]).T, np.matrix(self.V[m]))
            self.deltas[m] = self.momentum_alpha * self.deltas[m] + new_delta
            
        for m in range(len(self.layers_weights)):
            self.layers_weights[m] += self.deltas[m]

    # def adam(self, sigmas):
    #     for m in range(len(self.layers_weights)):
    #         # g_t = sigmas, tita = self.layers_weights
    #         self.adam_m[m] = self.beta_1 * self.adam_m[m] + (1 - self.beta_1) * sigmas[m]
    #         self.adam_v[m] = self.beta_2 * self.adam_v[m] + (1 - self.beta_2) * np.power(sigmas[m], 2)
    #         adam_prime_m = self.adam_m[m] / (1 - (np.power(self.beta_1, self.t)))
    #         adam_prime_v = self.adam_v[m] / (1 - (np.power(self.beta_2, self.t)))
    #
    #         self.layers_weights[m] = np.subtract(np.matrix(self.layers_weights[m]),
    #                                              self.momentum_alpha * np.matrix(adam_prime_m).T / (
    #                                                      np.sqrt(adam_prime_v) + self.adam_error))
    def train_batch(self, X_train, y_train, X_test = None, y_test = None):
        continue_condition = lambda i, error_min: i < len(X_train)
        return self.train(X_train, y_train, continue_condition, X_test, y_test)

    def train_online(self, X_train, y_train, X_test = None, y_test = None):
        continue_condition = lambda i, error_min: error_min > MIN_ERROR_TRESHOLD and i < len(X_train)
        return self.train(X_train, y_train, continue_condition, lambda: np.random.choice(len(X_train)), X_test, y_test)

    def cuadratic_error(self, output, expected):
        error = 0
        for j in range(self.output_dim):
            error += pow(expected[j] - output[j], 2)
        return error

    def cuadratic_mean_error(self, X_test, y_test):
        error = 0
        for i in range(len(X_test)):
            output = self.forward_propagation(X_test[i])
            expected = y_test[i]
            error += self.cuadratic_error(output, expected)

        return error / len(X_test)

    def train(self, X_train, y_train, continue_condition, next_example_idx_generator=None, X_test = None, y_test = None):
        error_min = float('inf')
        w_min = self.layers_weights
        iterations = 0

        train_accuracies = []
        test_accuracies = []
        train_errors = []
        test_errors = []

        for epoch in range(self.epochs):
            epoch_error_min = float('inf')
            iteration = 0
            self.t = 1
            epoch_w_min = self.layers_weights

            while continue_condition(iteration, error_min):
                next_example_id = next_example_idx_generator() if next_example_idx_generator is not None else iteration
                input = X_train[next_example_id]
                output = y_train[next_example_id]
                self.forward_propagation(input)
                self.back_propagation(output)

                epoch_error = self.cuadratic_mean_error(X_train, y_train)
                if epoch_error < epoch_error_min:
                    epoch_error_min = epoch_error
                    epoch_w_min = self.layers_weights

                iteration += 1
                self.t += 1

            # use best epoch weights
            self.layers_weights = epoch_w_min

            if X_test is not None:
                # epoch_test_accuracy = self.test(X_test) TODO implement accuracy
                test_accuracies.append(epoch_test_accuracy)
                
                epoch_test_error = self.cuadratic_mean_error(X_test, y_test)
                test_errors.append(epoch_test_error)
            else: epoch_test_accuracy = epoch_test_error = None

            # train_accuracies.append(self.test(X_train)) TODO implement accuracy
            train_errors.append(epoch_error_min)

            if epoch_error_min < error_min:
                error_min = epoch_error_min
                w_min = self.layers_weights

            iterations += iteration  # add epoc iterations to total iterations

        self.layers_weights = w_min

        # max_train_accuracy = max(train_accuracies) TODO implement accuracy
        # max_test_accuracy = max(test_accuracies) TODO implement accuracy
        min_train_error = min(train_errors)
        if X_test is None:
            min_test_error = None
        else: min_test_error = min(test_errors)
        #            \nAccuracy max en training: {max_train_accuracy}\nAccuracy max en test: {max_test_accuracy}\
        print(f'Error min en training: {min_train_error}\nError min en test: {min_test_error}\
            \nIterations: {iterations}')
        

        with open(WEIGHTS_BACKUP_DIR, 'w') as file:
            file.write("Layers weights\n")
            for layer_weights in self.layers_weights:
                for neuron_weights in layer_weights:
                    for weight in neuron_weights:
                        file.write(str(weight) + " ")
                    file.write("\n")

            file.write("\nEpochs: " + str(self.epochs))
            file.write("\train_dataset_len: " + str(len(X_train)))

        return train_accuracies, test_accuracies, train_errors, test_errors

    def load_backup_weights(self):
        with open(WEIGHTS_BACKUP_DIR, 'r') as file:
            lines = file.readlines()
            lineCount = 1 # skip headers

            for i in range(len(self.layers_weights)):
                for j in range(len(self.layers_weights[i])):
                    neuron_weights = lines[i + lineCount + j].split()
                    self.layers_weights[i][j] = np.array(neuron_weights).astype(float)

                lineCount += len(self.layers_weights[i]) -1
            
            lineCount += len(self.layers_weights) -1
