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


VALUES_PER_INPUT = 42
LATENT_SPACE_DIM = 42
def create_network(act_func_data=ActivationFunctions.EXP,
                        learning_rate=0.05, epochs=1000):
    BETA = 1
    act_func = lambda x: act_func_data.value["act_func"](x, BETA)
    deriv_act_func = lambda x: act_func_data.value["deriv_act_func"](x, BETA)
    return MultilayerNetwork(
                                                input_dim=      VALUES_PER_INPUT,
                                hidden_layers_perceptron_qty=[  VALUES_PER_INPUT, 
                                                                VALUES_PER_INPUT,
                                                                LATENT_SPACE_DIM,
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
    expected_result = X_train[0]
    print("Latent space of this classification: ", network.V[2])
    print("Classification result: ")
    visualize_output(classify_result)
    print("Expected result: ")
    visualize_output(expected_result)

    return train_accuracies, test_accuracies, train_errors, test_errors

def latent_space_exercise(network, output_transform, latent_space):
    classify_result = output_transform.inverse_transform([network.forward_propagation_from_latent_space(latent_space)])[0]
    print("Classification result: ", classify_result)
    visualize_output(classify_result)
    
def visualize_output(output):
    print('')
    count = 0
    for num in output:
        count +=1
        if(num > 0.5):
            sys.stdout.write('#')
        else:
            sys.stdout.write(' ')            
        if(count % 8 == 0):
            print('')
        # count = -1
        # for bit in bin(int(num)):
        #     count +=1
        #     if count == 0 or count == 1:
        #         continue
        #     if bit == '1': print('#', end='')
        #     else: print(' ', end='')
        # print('')
        
def get_bit_image(letter):
    bit_image = []
    #letter = [0x04, 0x04, 0x02, 0x00, 0x00, 0x00, 0x00]
    for num in letter:
        count = 0
        for bit in bin(int(num)):
            count +=1
            if count == 1 or count == 2:
                continue
            bit_image.append(int(bit))
        if(count < 8):
            for i in range(0,8 - count):
                bit_image.append(0)
    visualize_output(bit_image)
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
    
    X = []
    for img in SYMBOLS_IMAGE:
        X.append(get_bit_image(img))
    y = X
    print(X[0])
    # X = scaler.fit_transform(SYMBOLS_IMAGE) # input = expected output
    # y = scaler.fit_transform(SYMBOLS_IMAGE)
    # X = X + noise_factor * np.random.normal(loc=0.0, scale=1.0, size=X.shape)
    # X = np.clip(X, 0.0,1.0)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size)

    network = create_network(act_func_data=act_func_data, 
            learning_rate=learning_rate, 
            epochs=epochs)

    if load_backup_weights:
        network.load_backup_weights()
    else:
        train_accuracies, test_accuracies, train_errors, test_errors = train_guess_number(
            network, scaler,  X_train, X_test, y_train, y_test,
            batch = program_to_exec == "batch")
    
    if program_to_exec == "latent_space_exercise":
        while(True):
            print("Insert latent space numbers [0,1]")
            a = float(input())
            b = float(input())
            latent_space_exercise(network, scaler, [a, b])
    
    
