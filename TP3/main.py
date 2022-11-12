import random
from .models.multilayer_network import MultilayerNetwork
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from .utils.activations_functions import ActivationFunctions
import numpy as np
import pandas as pd
from .data.font import SYMBOLS_IMAGE,SYMBOLS_VALUE


VALUES_PER_INPUT = 7

def train_guess_number(batch=False, act_func_data=ActivationFunctions.EXP, learning_rate=0.05, epochs=250):
    BETA = 1
    act_func = lambda x: act_func_data.value["act_func"](x, BETA)
    deriv_act_func = lambda x: act_func_data.value["deriv_act_func"](x, BETA)
    output_transform = act_func_data.value["output_transform"]

    network = MultilayerNetwork(hidden_layers_perceptron_qty=[VALUES_PER_INPUT, 2, VALUES_PER_INPUT],
                                           input_dim=VALUES_PER_INPUT,
                                           output_dim=VALUES_PER_INPUT, 
                                           learning_rate=learning_rate, epochs=epochs,
                                           act_func=act_func, deriv_act_func=deriv_act_func)

    X_train, X_test, y_train, y_test = train_test_split(SYMBOLS_IMAGE, SYMBOLS_IMAGE, test_size=0.33)

    if batch:
        train_accuracies, test_accuracies, train_errors, test_errors = network.train_batch(X_train, y_train)
    else: train_accuracies, test_accuracies, train_errors, test_errors = network.train_online(X_train, y_train)
    
    print_results(network,X_train)
    return train_accuracies, test_accuracies, train_errors, test_errors


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
    train_guess_number()
    
