import random
from .models.multilayer_network import MultilayerNetwork
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.model_selection import train_test_split
from .utils.activations_functions import ActivationFunctions
import numpy as np
import pandas as pd
from .data.font import SYMBOLS_IMAGE, SYMBOLS_VALUE

VALUES_PER_INPUT = 7

def train_guess_number(batch=False, act_func_data=ActivationFunctions.EXP, learning_rate=0.05, epochs=2000):
    BETA = 1
    act_func = lambda x: act_func_data.value["act_func"](x, BETA)
    deriv_act_func = lambda x: act_func_data.value["deriv_act_func"](x, BETA)
    output_transform = act_func_data.value["output_transform"]    
    scaler = MinMaxScaler()

    network = MultilayerNetwork(hidden_layers_perceptron_qty=[VALUES_PER_INPUT, 2, VALUES_PER_INPUT],
                                           input_dim=VALUES_PER_INPUT,
                                           output_dim=VALUES_PER_INPUT, 
                                           learning_rate=learning_rate, epochs=epochs,
                                           act_func=act_func, deriv_act_func=deriv_act_func)

    X = scaler.fit_transform(SYMBOLS_IMAGE)
    y = SYMBOLS_IMAGE
    X_train, X_test, y_train, y_test = train_test_split(X, X, test_size=0.1)
    if batch:
        train_accuracies, test_accuracies, train_errors, test_errors = network.train_batch(X_train, y_train)
    else: train_accuracies, test_accuracies, train_errors, test_errors = network.train_online(X_train, y_train)
    
    classify_result = scaler.inverse_transform([network.forward_propagation(X_train[0])])[0]
    expected_result = scaler.inverse_transform([X_train[0]])[0]
    print("Classify result: ", classify_result)
    visualize_output(classify_result)
    print("Expected result: ", expected_result)
    visualize_output(expected_result)

    return train_accuracies, test_accuracies, train_errors, test_errors

def visualize_output(output):
    for num in output:
        for bit in bin(int(num)):
            if bit == '1': print('#', end='')
            else: print(' ', end='')
        print('')
        
if __name__ == "__main__":
    random.seed(123456789)
    train_guess_number()
    
