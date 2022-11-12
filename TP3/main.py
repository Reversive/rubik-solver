import random
from .models.multilayer_network import MultilayerNetwork
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.model_selection import train_test_split
from .utils.activations_functions import ActivationFunctions
import numpy as np
import pandas as pd
from .data.font import SYMBOLS_IMAGE, SYMBOLS_VALUE

VALUES_PER_INPUT = 7

def train_guess_number(batch=False, act_func_data=ActivationFunctions.EXP, 
                        learning_rate=0.05, epochs=1000, load_backup_weights=False):
    BETA = 1
    act_func = lambda x: act_func_data.value["act_func"](x, BETA)
    deriv_act_func = lambda x: act_func_data.value["deriv_act_func"](x, BETA)
    output_transform = act_func_data.value["output_transform"]    

    network = MultilayerNetwork(
                                                input_dim=      VALUES_PER_INPUT,
                                hidden_layers_perceptron_qty=[  VALUES_PER_INPUT, 
                                                                VALUES_PER_INPUT,
                                                                2,
                                                                VALUES_PER_INPUT, 
                                                                VALUES_PER_INPUT],
                                                output_dim=     VALUES_PER_INPUT, 
                                learning_rate=learning_rate, epochs=epochs,
                                act_func=act_func, deriv_act_func=deriv_act_func)

    X = output_transform.fit_transform(SYMBOLS_IMAGE) # input = expected output
    X_train, X_test, y_train, y_test = train_test_split(X, X, test_size=0.5)

    if load_backup_weights:
        # Para tomar pesos del ultimo entrenamiento
        network.load_backup_weights()
    else:
        # Para entrenar de cero:
        if batch:
            train_accuracies, test_accuracies, train_errors, test_errors = network.train_batch(X_train, y_train)
        else: train_accuracies, test_accuracies, train_errors, test_errors = network.train_online(X_train, y_train)
    
    classify_result = output_transform.inverse_transform([network.forward_propagation(X_train[0])])[0]
    expected_result = output_transform.inverse_transform([X_train[0]])[0]
    print("Latent space of this classification: ", network.V[2])
    print("Classification result: ", classify_result)
    visualize_output(classify_result)
    print("Expected result: ", expected_result)
    visualize_output(expected_result)

    return train_accuracies, test_accuracies, train_errors, test_errors, network

def latent_space_exercise(network, output_transform, latent_space):
    classify_result = output_transform.inverse_transform([network.forward_propagation_from_latent_space(latent_space)])[0]
    print("Classification result: ", classify_result)
    visualize_output(classify_result)
    
def visualize_output(output):
    for num in output:
        for bit in bin(int(num)):
            if bit == '1': print('#', end='')
            else: print(' ', end='')
        print('')
        
if __name__ == "__main__":
    random.seed(123456789)
    
    # TODO: Add config file and readme with instructions
    act_func_data=ActivationFunctions.EXP
    train_accuracies, test_accuracies, train_errors, test_errors, network = \
        train_guess_number(act_func_data=act_func_data, learning_rate=0.05, epochs=25000, 
                load_backup_weights=True)

    while(True):
        print("Insert latent space numbers [0,1]")
        a = float(input())
        b = float(input())
        latent_space_exercise(network, act_func_data.value["output_transform"], [a, b])
    
    
