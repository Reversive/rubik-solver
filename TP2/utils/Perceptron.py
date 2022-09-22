import numpy as np

THRESHOLD = 0.00001
MAX_ITERS = 10000


class Perceptron:
    def __init__(self, input_dim, learning_rate, act_func = lambda x: x, deriv_act_func = lambda x: 1):
        self.weights = np.zeros(1 + input_dim)
        self.learning_rate = learning_rate
        self.act_func = act_func
        self.deriv_act_func= deriv_act_func

    def test(self, inputs_without_constant):
        return self.act_func(np.dot(self.weights, np.append(1, inputs_without_constant)))

    def cuadratic_error(self, train_data):
        error = 0
        for example in train_data:
            error += (1 / 2) * pow(example[-1] - self.test(example[:-1]), 2)

        return error

    def train(self, train_data):
        # ONLINE TODO: BATCH
        error_min = float('inf')
        w_min = self.weights
        i = 0
        np.random.seed(12345)
        while error_min > THRESHOLD and i < MAX_ITERS:
            example = train_data[np.random.choice(range(len(train_data)))]
            inputs = np.append(1, example[:-1])
            expected_output = example[-1]
            output = self.act_func(np.dot(self.weights, inputs))

            delta_w = self.learning_rate * (expected_output - output) * inputs * self.deriv_act_func(output)
            self.weights += delta_w

            # si hubiesen muchos datos deberia estar afuera, despues de recorrer una epoca (CREO)
            error = self.cuadratic_error(train_data)
            if error < error_min:
                error_min = error
                w_min = self.weights

            i += 1

        self.weights = w_min
        print(f'Error min: {error_min}, iterations: {i}, weights: {self.weights}')
        