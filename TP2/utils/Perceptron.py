import numpy as np


class Perceptron:
    def __init__(self, activation_func, input_dim, learning_rate):
        self.func = activation_func
        self.weights = np.zeros(1 + input_dim)
        self.learning_rate = learning_rate

    def test(self, h):
        return self.func(np.dot(self.weights.transpose(), np.array([1] + h)))

    def cuadratic_error(self, expected, result):
        return (1 / 2) * pow(expected - result, 2)

    def train(self, train_data):
        error_min = float('inf')
        w_min = self.weights
        for example in train_data:
            input = example[:-1]
            expected_output = example[-1]
            test_result = self.test(input)
            delta_w = self.learning_rate * (expected_output - test_result) * np.array([1] + input)
            self.weights += delta_w
            error = self.cuadratic_error(expected_output, test_result)
            if error < error_min:
                error_min = error
                w_min = self.weights

        self.weights = w_min
