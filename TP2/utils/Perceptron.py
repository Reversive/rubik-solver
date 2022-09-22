import numpy as np

THRESHOLD = 0.00001

class Perceptron:
    def __init__(self, input_dim, learning_rate, epochs, act_func = lambda x: x, deriv_act_func = lambda x: 1):
        self.weights = np.zeros(1 + input_dim)
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.act_func = act_func
        self.deriv_act_func= deriv_act_func

    def test(self, inputs_without_constant):
        return self.act_func(np.dot(self.weights, np.append(1, inputs_without_constant)))

    def cuadratic_error(self, train_data):
        error = 0
        for example in train_data:
            error += (1 / 2) * pow(example[-1] - self.test(example[:-1]), 2)

        return error

    def train_batch(self, train_data, test_data):
        continue_condition = lambda i: i < len(train_data)
        self.train(train_data, test_data, continue_condition)

    def train_online(self, train_data, test_data):
        np.random.seed(12345)
        continue_condition = lambda i, error_min: error_min > THRESHOLD and i < len(train_data)        
        self.train(train_data, test_data, continue_condition, lambda: np.random.choice(len(train_data)))

    def train(self, train_data, test_data, continue_condition, next_example_idx = None):
        error_min = float('inf')
        w_min = self.weights
        i = 0

        for _ in range(self.epochs):
            epoch_error_min = float('inf')

            while continue_condition(i, error_min):
                example = train_data[next_example_idx() if next_example_idx is not None else i]
                inputs = np.append(1, example[:-1])
                expected_output = example[-1]
                output = self.act_func(np.dot(self.weights, inputs))

                delta_w = self.learning_rate * (expected_output - output) * inputs * self.deriv_act_func(output)
                self.weights += delta_w

                epoch_error = self.cuadratic_error(test_data)
                if epoch_error < epoch_error_min:
                    epoch_error_min = epoch_error
                    epoch_w_min = self.weights

                i += 1

            self.weights = epoch_w_min
            error = self.cuadratic_error(test_data)
            if error < error_min:
                error_min = error
                w_min = self.weights

        self.weights = w_min
        print(f'Error min: {error_min}, iterations: {i}, weights: {self.weights}')

        