import numpy as np
import csv
THRESHOLD = 0.00001

class Perceptron:
    def __init__(self, input_dim, learning_rate, epochs, act_func = lambda x: x, deriv_act_func = lambda x: 1):
        self.weights = np.zeros(1 + input_dim)
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.act_func = act_func
        self.deriv_act_func= deriv_act_func
        file = open('perceptron.csv', 'a', newline='')
        self.writer = csv.writer(file)
        self.writer.writerow(["EPOCH", "ERROR", "LEARNING_RATE"])
        file.close()


    def classify(self, example):
        return self.act_func(np.dot(self.weights, np.append(1, example)))

    def test(self, data):
        error = 0
        for example in data:
            error += (1 / 2) * pow(example[-1] - self.classify(example[:-1]), 2)

        return error

    def train_batch(self, train_data):
        continue_condition = lambda i: i < len(train_data)
        self.train(train_data, continue_condition)

    def train_online(self, train_data):
        continue_condition = lambda i, error_min: error_min > THRESHOLD and i < len(train_data)        
        self.train(train_data, continue_condition, lambda: np.random.choice(len(train_data)))

    def write_to_csv(self, iteration, epoch_error, learning_rate):
        file = open('perceptron.csv', 'a', newline='')
        self.writer = csv.writer(file)
        self.writer.writerow([str(iteration), str(epoch_error), str(learning_rate)])
        file.close()

    def train(self, train_data, continue_condition, next_example_idx = None):
        error_min = float('inf')
        w_min = self.weights
        iterations = 0

        for _ in range(self.epochs):
            epoch_error_min = float('inf')
            iteration = 0

            while continue_condition(iteration, error_min):
                example = train_data[next_example_idx() if next_example_idx is not None else i]
                inputs = np.append(1, example[:-1])
                expected_output = example[-1]
                output = self.act_func(np.dot(self.weights, inputs))

                delta_w = self.learning_rate * (expected_output - output) * inputs * self.deriv_act_func(output)
                self.weights += delta_w

                epoch_error = self.test(train_data)
                if epoch_error < epoch_error_min:
                    epoch_error_min = epoch_error
                    epoch_w_min = self.weights

                iteration += 1
                self.write_to_csv(iteration,epoch_error,self.learning_rate)


            iterations += iteration

            self.weights = epoch_w_min
            error = self.test(train_data)
            if error < error_min:
                error_min = error
                w_min = self.weights

        self.weights = w_min
        print(f'Error min: {error_min}, iterations: {iterations}, weights: {self.weights}')

        