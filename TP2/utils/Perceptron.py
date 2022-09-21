import numpy as np

THRESHOLD = 0.00001
MAX_ITERS = 1000000


class Perceptron:
    def __init__(self, activation_func, input_dim, learning_rate):
        self.func = activation_func
        self.weights = np.zeros(1 + input_dim)
        self.learning_rate = learning_rate

    def test(self, h):
        return self.func(np.dot(self.weights, np.array([1] + h)))

    def cuadratic_error(self, train_data):
        error = 0
        for example in train_data:
            error += (1 / 2) * pow(example[-1] - self.test(example[:-1]), 2)

        return error

    def train(self, train_data):
        error_min = float('inf')
        w_min = self.weights
        i = 0
        np.random.seed(12345)
        while error_min > THRESHOLD and i < MAX_ITERS:
            example = train_data[np.random.choice(range(len(train_data)))]
            inputs = example[:-1]
            expected_output = example[-1]
            test_result = self.test(inputs)
            delta_w = self.learning_rate * (expected_output - test_result) * np.array([1] + inputs)
            self.weights += delta_w
            error = self.cuadratic_error(train_data)
            if error < error_min:
                error_min = error
                w_min = self.weights

            i += 1

        self.weights = w_min
