import random
from .models.multilayer_network import MultilayerNetwork
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.model_selection import train_test_split
from .utils.activations_functions import ActivationFunctions
import numpy as np
import pandas as pd
from .data.font import SYMBOLS_IMAGE, SYMBOLS_VALUE, corrupt, get_corrupted_array
import configparser
import sys


VALUES_PER_INPUT = 56

def create_network(act_func_data=ActivationFunctions.EXP,latent_space_dim=70,
                        learning_rate=0.05, epochs=1000):
    BETA = 1
    act_func = lambda x: act_func_data.value["act_func"](x, BETA)
    deriv_act_func = lambda x: act_func_data.value["deriv_act_func"](x, BETA)
    return MultilayerNetwork(
                                                input_dim=      VALUES_PER_INPUT,
                                hidden_layers_perceptron_qty=[  VALUES_PER_INPUT, 
                                                                VALUES_PER_INPUT,
                                                                latent_space_dim,
                                                                VALUES_PER_INPUT, 
                                                                VALUES_PER_INPUT],
                                                output_dim=     VALUES_PER_INPUT, 
                                learning_rate=learning_rate, epochs=epochs,
                                act_func=act_func, deriv_act_func=deriv_act_func)

def train_guess_number(network, scaler,X_train, X_test, y_train, y_test, batch=False):
    if batch:
        train_accuracies, test_accuracies, train_errors, test_errors = network.train_batch(X_train, y_train)
    else: train_accuracies, test_accuracies, train_errors, test_errors = network.train_online(X_train, y_train)
    
    # classify_result = scaler.inverse_transform([network.forward_propagation(X_train[0])])[0]
    # expected_result = scaler.inverse_transform([X_train[0]])[0]
    classify_result = network.forward_propagation(X_train[0])
    expected_result = y_train[0]
    noisy_result = X_train[0]
    print("Latent space of this classification: ", network.V[3])
    print("Classification result: ")
    visualize_output(classify_result)
    print("Expected result: ")
    visualize_output(expected_result)
    print("Noisy result: ")
    visualize_output(noisy_result)

    return train_accuracies, test_accuracies, train_errors, test_errors

def latent_space_exercise(network, latent_space):
    classify_result = network.forward_propagation_from_latent_space(latent_space)
    print("Classification result: ", classify_result)
    visualize_output(classify_result)
    
def visualize_output(output):
    count = 0
    #TODO: imprimir con escala de grises
    for num in output:
        count +=1
        if(num > 0.5):
            sys.stdout.write('#')
        else:
            sys.stdout.write(' ')            
        if(count % 8 == 0):
            print('')
        
def get_bit_image(letter):
    bit_image = []
    for num in letter:
        for bit in format(num, '08b'):
            bit_image.append(int(bit))
    return bit_image

if __name__ == "__main__":
    random.seed(123456789)
    config = configparser.ConfigParser()
    config.read("./TP3/config.yaml")

    general_config = config["general_config"]
    program_to_exec = general_config["exercise"]

    learning_rate = float(general_config['learning_rate'])
    epochs = int(general_config['epochs'])
    act_func_data = ActivationFunctions[general_config['activation_function']]
    scaler = act_func_data.value["output_transform"]
    beta = float(general_config['beta'])
    noise = general_config['noise'] == 'True'
    noise_factor = float(general_config['noise_factor'])
    load_backup_weights = general_config['load_backup_weights'] == 'True'
    test_size = float(general_config['test_size'])
    latent_space_dim = int(general_config['latent_space_dim'])
    
    X = []
    for img in SYMBOLS_IMAGE:
        X.append(get_bit_image(img))
    y = []
    for img in SYMBOLS_IMAGE:
        y.append(get_bit_image(img))

    for i in range(len(X)):
        for j in range(len(X[i])):
            X[i][j] += noise_factor * np.random.normal(loc=0.0, scale=1.0)
        X[i] = np.clip(X[i], 0.0,1.0)


    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size)
    network = create_network(act_func_data=act_func_data, 
            learning_rate=learning_rate, latent_space_dim=latent_space_dim,
            epochs=epochs)

    if load_backup_weights:
        network.load_backup_weights()
    else:
        train_accuracies, test_accuracies, train_errors, test_errors = train_guess_number(
            network, scaler,  X_train, X_test, y_train, y_test,
            batch = program_to_exec == "batch")
    
    if program_to_exec == "latent_space_exercise":
        while(True):
            latent_space_array = []
            print("Insert latent space numbers [0,1]")
            for i in range(latent_space_dim):
                latent_space_array.append(float(input()))
            latent_space_exercise(network, latent_space_array)
    
    
