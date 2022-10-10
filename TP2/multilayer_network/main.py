import random
from .ui.numbers_grid import NumbersGrid
from ..utils.files import read_numbers_from_file
from ..utils.dataset_utils import DivideDatasetToTrainAndTest
from .multilayer_network import MultilayerNetwork
from sklearn.preprocessing import StandardScaler
from ..utils.activations_functions import ActivationFunctions
import numpy as np
import pandas as pd

ROWS_PER_NUMBER = 7
COLUMNS_PER_NUMBER = 5


def xor_exercise(batch=False):
    BETA = 1
    epochs = 250
    act_func_data = ActivationFunctions.TANH
    act_func = lambda x: act_func_data.value["act_func"](x, BETA)
    deriv_act_func = lambda x: act_func_data.value["deriv_act_func"](x, BETA)
    output_transform = act_func_data.value["output_transform"]

    multilayer_network = MultilayerNetwork(hidden_layers_perceptron_qty=[2], input_dim=2,
                                           output_dim=1, learning_rate=0.05, epochs=epochs,
                                           act_func=act_func, deriv_act_func=deriv_act_func)

    input_dataset_df = pd.DataFrame([
        [1, 1],
        [1, -1],
        [-1, 1],
        [-1, -1]])
    output_dataset_df = pd.DataFrame([
        [-1],
        [1],
        [1],
        [-1]])

    # scalarize or standarize inputs according to function
    input_dataset_df[input_dataset_df.columns] = output_transform.fit_transform(input_dataset_df)

    # scalarize eor standarize expected outputs according to function
    output_dataset_df[output_dataset_df.columns] = output_transform.fit_transform(output_dataset_df)

    train_data = []
    test_data = []
    for i in range(len(input_dataset_df)):
        train_data.append([input_dataset_df.iloc[i].tolist(), output_dataset_df.iloc[i].tolist()])
        test_data.append([input_dataset_df.iloc[i].tolist(), output_dataset_df.iloc[i].tolist()])

    if batch:
        train_accuracies, test_accuracies, train_errors, test_errors = multilayer_network.train_batch(train_data, test_data)
    else: train_accuracies, test_accuracies, train_er, test_errors = multilayer_network.train_online(train_data, test_data)

    return train_accuracies, test_accuracies, train_errors, test_errors


def even_numbers_exercise(noisy_test=False, batch=False, momentum=0.8, train_percentage=0.7, act_func_data=ActivationFunctions.EXP, learning_rate=0.05, epochs=250):
    BETA = 1
    ROWS_PER_NUMBER = 7
    COLUMNS_PER_NUMBER = 5
    act_func = lambda x: act_func_data.value["act_func"](x, BETA)
    deriv_act_func = lambda x: act_func_data.value["deriv_act_func"](x, BETA)
    output_transform = act_func_data.value["output_transform"]

    multilayer_network = MultilayerNetwork(hidden_layers_perceptron_qty=[COLUMNS_PER_NUMBER * ROWS_PER_NUMBER,
                                                                         COLUMNS_PER_NUMBER * ROWS_PER_NUMBER],
                                           input_dim=COLUMNS_PER_NUMBER * ROWS_PER_NUMBER,momentum_alpha=momentum,
                                           output_dim=2, learning_rate=learning_rate, epochs=epochs,
                                           act_func=act_func, deriv_act_func=deriv_act_func)

    expected_output = []
    for i in range(10):
        expected_output.append([i % 2, (i + 1) % 2])
        # for even numbers output is: [0,1], for odd: [1,0]

    dataset = get_numbers_dataset(expected_output, output_transform)

    train_dataset, test_dataset = DivideDatasetToTrainAndTest(dataset, train_percentage)

    if noisy_test:
        test_dataset = apply_noise_over_dataset(dataset)

    if batch:
        train_accuracies, test_accuracies, train_errors, test_errors = multilayer_network.train_batch(train_dataset, test_dataset)
    else: train_accuracies, test_accuracies, train_errors, test_errors = multilayer_network.train_online(train_dataset, test_dataset)

    return train_accuracies, test_accuracies, train_errors, test_errors


def train_guess_number(noisy_test=False, batch=False, train_percentage=0.7, act_func_data=ActivationFunctions.EXP, learning_rate=0.05, epochs=250):
    BETA = 1
    act_func = lambda x: act_func_data.value["act_func"](x, BETA)
    deriv_act_func = lambda x: act_func_data.value["deriv_act_func"](x, BETA)
    output_transform = act_func_data.value["output_transform"]

    multilayer_network = MultilayerNetwork(hidden_layers_perceptron_qty=[COLUMNS_PER_NUMBER * ROWS_PER_NUMBER,
                                                                         COLUMNS_PER_NUMBER * ROWS_PER_NUMBER],
                                           input_dim=COLUMNS_PER_NUMBER * ROWS_PER_NUMBER,
                                           output_dim=10, learning_rate=learning_rate, epochs=epochs,
                                           act_func=act_func, deriv_act_func=deriv_act_func)

    expected_output = [
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 0
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],  # 1
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],  # 8
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]   # 9
    ]

    dataset = get_numbers_dataset(expected_output, output_transform)

    train_dataset, test_dataset = DivideDatasetToTrainAndTest(dataset, train_percentage)

    if noisy_test:
        test_dataset = apply_noise_over_dataset(dataset)

    if batch:
        train_accuracies, test_accuracies, train_errors, test_errors = multilayer_network.train_batch(train_dataset, test_dataset)
    else: train_accuracies, test_accuracies, train_errors, test_errors = multilayer_network.train_online(train_dataset, test_dataset)

    return train_accuracies, test_accuracies, train_errors, test_errors


def guess_numbers_exercise():
    multilayer_network, train_dataset = train_guess_number()
    print_results(multilayer_network, train_dataset)


def interactive_guess_numbers(act_func_data=ActivationFunctions.EXP, learning_rate=0.05, epochs=1000):
    BETA = 1
    act_func = lambda x: act_func_data.value["act_func"](x, BETA)
    deriv_act_func = lambda x: act_func_data.value["deriv_act_func"](x, BETA)
    output_transform = act_func_data.value["output_transform"]

    multilayer_network = MultilayerNetwork(hidden_layers_perceptron_qty=[COLUMNS_PER_NUMBER * ROWS_PER_NUMBER,
                                                                         COLUMNS_PER_NUMBER * ROWS_PER_NUMBER],
                                           input_dim=COLUMNS_PER_NUMBER * ROWS_PER_NUMBER,
                                           output_dim=10, learning_rate=learning_rate, epochs=epochs,
                                           act_func=act_func, deriv_act_func=deriv_act_func)

    expected_output = [
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 0
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],  # 1
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],  # 8
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]   # 9
    ]

    dataset = get_numbers_dataset(expected_output, output_transform)

    train_dataset, test_dataset = DivideDatasetToTrainAndTest(dataset, 1)

    multilayer_network.train_online(train_dataset, None)

    board = NumbersGrid(multilayer_network.forward_propagation)
    board.numbers_grid()


def apply_noise_over_dataset(dataset):
    MAX_NOISE_CHANGES = 6
    noisy_dataset = []
    for example in dataset:
        elements_to_change = random.randint(0, MAX_NOISE_CHANGES)
        noisy_example = example[0].copy()
        expected_result = example[1].copy()
        for _ in range(elements_to_change):
            index = random.randint(0, (ROWS_PER_NUMBER - 1) * (COLUMNS_PER_NUMBER - 1))
            noisy_example[index] = 1 - noisy_example[index]

        noisy_dataset.append([noisy_example, expected_result])

    return noisy_dataset


def get_numbers_dataset(expected_output, output_transform):
    input_dataset_df = pd.DataFrame(read_numbers_from_file("TP2/multilayer_network/data/TP2-ej3-digitos.txt",
                                                           ROWS_PER_NUMBER, COLUMNS_PER_NUMBER))
    # cada input tiene 35 binarios de información, cada uno correspondiente a uno de los "pixeles"

    output_dataset_df = pd.DataFrame(expected_output)

    # scalarize or standarize inputs according to function
    input_dataset_df[input_dataset_df.columns] = output_transform.fit_transform(input_dataset_df)

    # scalarize eor standarize xpected outputs according to function
    output_dataset_df[output_dataset_df.columns] = output_transform.fit_transform(output_dataset_df)

    dataset = []
    for i in range(len(input_dataset_df)):
        dataset.append([input_dataset_df.iloc[i].tolist(), output_dataset_df.iloc[i].tolist()])

    return dataset


def print_results(multilayer_network, dataset):
    corrects = 0
    for i, example in enumerate(dataset):
        output = np.argmax(multilayer_network.forward_propagation(example[:-1]))
        expected = np.argmax(example[-1])
        print("OUTPUT: ", output, "EXPECTED: ", expected)
        if output == expected:
            corrects += 1

    print("accuracy: ", corrects / len(dataset))


if __name__ == "__main__":
    random.seed(123456789)
    # xor_exercise()
    # even_numbers_exercise()
    # guess_numbers_exercise()
    interactive_guess_numbers()
