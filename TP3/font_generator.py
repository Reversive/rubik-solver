import math
import random
from .models.multilayer_network import MultilayerNetwork
from sklearn.model_selection import train_test_split
from .utils.activations_functions import ActivationFunctions
import numpy as np
import pandas as pd
from .data.font import SYMBOLS_IMAGE, SYMBOLS_VALUE
import configparser
import sys
from .visualizations.utils import generate_latent_space_matrix_plot
import matplotlib.pyplot as plt

IMAGE_WIDTH = 8
IMAGE_HEIGHT = 7
INPUT_SIZE = 7 * IMAGE_WIDTH


def create_network(act_func_data=ActivationFunctions.LOGISTICA, latent_space_dim=2,
                   hidden_layers_dim=[28,
                                      16,
                                      2,
                                      16,
                                      28],
                   learning_rate=0.05, epochs=1000, with_adam=False, momentum_alpha=0, adaptative_learning_rate=False,
                   noise=False, noise_factor=0):
    BETA = 1
    act_func = lambda x: act_func_data.value["act_func"](x, BETA)
    deriv_act_func = lambda x: act_func_data.value["deriv_act_func"](x, BETA)
    return MultilayerNetwork(
        input_dim=INPUT_SIZE,
        hidden_layers_perceptron_qty=hidden_layers_dim,
        output_dim=INPUT_SIZE,
        learning_rate=learning_rate, epochs=epochs,
        noise=noise, noise_factor=noise_factor,
        act_func=act_func, momentum_alpha=momentum_alpha, deriv_act_func=deriv_act_func, with_adam=with_adam,
        adaptative_learning_rate=adaptative_learning_rate)


def get_binary(output):
    binary = np.zeros(7 * 8)
    count = 0
    for num in output:
        if num > 0.5:
            binary[count] = 1
        else:
            binary[count] = 0
        count += 1
    return binary


def get_heatmap(network, X_train):
    AMOUNT_PER_ROW = 4
    IMG_AMOUNT = 32
    HEIGHT = 7
    WIDTH = 8
    matrix = np.zeros((int(IMG_AMOUNT / AMOUNT_PER_ROW) * HEIGHT, WIDTH * AMOUNT_PER_ROW))
    for idx, train_element in enumerate(X_train):
        # result = train_element # si queremos que sea con el set original
        result = network.forward_propagation(train_element) # si queremos que sea con la prediccion
        temp = get_binary(result)
        k = 0
        for j in range(HEIGHT * int(math.floor(idx / AMOUNT_PER_ROW)),
                       HEIGHT * int((math.floor(idx / AMOUNT_PER_ROW) + 1))):
            for i in range(idx % AMOUNT_PER_ROW * WIDTH, (idx % AMOUNT_PER_ROW + 1) * WIDTH):
                matrix[j][i] = temp[k]
                k += 1

    plt.axis('off')
    plt.imshow(matrix, cmap='hot_r', interpolation='nearest')
    plt.show()


def train_guess(network, X_train, X_test, y_train, y_test, noise=False, verbose=True):
    train_accuracies, test_accuracies, train_errors, test_errors = network.train(X_train, y_train, X_test, y_test)

    classify_result = network.forward_propagation(X_train[0])
    expected_result = y_train[0]
    noisy_result = X_train[0]
    if verbose:
        print("Latent space of this classification: ", network.V[int(np.floor(len(network.V) / 2))])
        # print("Network output: ")
        # visualize_output(classify_result)
        # print("Expected result: ")
        # visualize_output(expected_result)
        # if noise:
        #     print("Network input: ")
        #     visualize_output(noisy_result)
        get_heatmap(network, X_train)
    return train_accuracies, test_accuracies, train_errors, test_errors


def latent_space_exercise(network, latent_space):
    classify_result = network.forward_propagation_from_latent_space(latent_space)
    print("Classification result: ", classify_result)
    visualize_output(classify_result)


def visualize_output(output):
    count = 0
    # TODO: imprimir con escala de grises
    for num in output:
        count += 1
        if (num > 0.5):
            sys.stdout.write('#')
        else:
            sys.stdout.write(' ')
        if (count % 8 == 0):
            print('')


def get_bit_image(letter):
    bit_image = []
    for num in letter:
        for bit in format(num, '08b'):
            bit_image.append(int(bit))
    return bit_image


def get_config():
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
    with_adam = general_config['with_adam'] == 'True'
    momentum_alpha = float(general_config['momentum_alpha'])
    adaptative_learning_rate = general_config['adaptative_learning_rate'] == 'True'
    return program_to_exec, learning_rate, epochs, act_func_data, scaler, beta, noise, noise_factor, load_backup_weights, test_size, latent_space_dim, with_adam, adaptative_learning_rate, momentum_alpha

def latent_space_run(learning_rate=0.05, epochs=2500, act_func_data=ActivationFunctions.LOGISTICA, 
                noise=False, noise_factor=0.0, test_size=0, with_adam=True, momentum_alpha=0.3,adaptative_learning_rate=False,
                hidden_layers_dim=[ 28,16,
                                    2,
                                    16,28]):
    X = []
    for img in SYMBOLS_IMAGE:
        X.append(get_bit_image(img))
    y = []
    for img in SYMBOLS_IMAGE:
        y.append(get_bit_image(img))

    if test_size == 0:
        X_train = X
        X_test = X
        y_train = y
        y_test = y
    else:
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size)
        
    network = create_network(act_func_data=act_func_data, learning_rate=learning_rate, 
            hidden_layers_dim=hidden_layers_dim, momentum_alpha=momentum_alpha,noise_factor=noise_factor,noise=noise,
            epochs=epochs, adaptative_learning_rate=adaptative_learning_rate,with_adam=with_adam)

    train_accuracies, test_accuracies, train_errors, test_errors = train_guess(
            network=network, X_train=X_train, X_test=X_test, y_train=y_train, 
            y_test=y_test, noise = noise, verbose=False)
    return train_accuracies, test_accuracies, train_errors, test_errors


if __name__ == "__main__":
    random.seed(123456789)
    program_to_exec, learning_rate, epochs, act_func_data, scaler, beta, noise, noise_factor, \
    load_backup_weights, test_size, latent_space_dim, with_adam, adaptative_learning_rate, momentum_alpha \
        = get_config()

    X = []
    for img in SYMBOLS_IMAGE:
        visualize_output(get_bit_image(img))
        X.append(get_bit_image(img))
    y = []
    for img in SYMBOLS_IMAGE:
        y.append(get_bit_image(img))

    if noise:
        hidden_layers_dim = [56]
    else:
        hidden_layers_dim = [28, 16,2,16, 28]
    
    if test_size == 0:
        X_train = X
        X_test = X
        y_train = y
        y_test = y
    else:
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size)

    network = create_network(act_func_data=act_func_data, learning_rate=learning_rate,
                             hidden_layers_dim=hidden_layers_dim, momentum_alpha=momentum_alpha,
                             epochs=epochs, adaptative_learning_rate=adaptative_learning_rate, with_adam=with_adam,
                             noise=noise, noise_factor=noise_factor)

    if load_backup_weights:
        network.load_backup_weights()
    else:
        train_accuracies, test_accuracies, train_errors, test_errors = train_guess(
            network=network, X_train=X_train, X_test=X_test, y_train=y_train,
            y_test=y_test)

    if program_to_exec == "latent_space_exercise":
        while (True):
            latent_space_array = []
            print("Insert latent space numbers [0,1]")
            for i in range(latent_space_dim):
                latent_space_array.append(float(input()))
            latent_space_exercise(network, latent_space_array)
    elif program_to_exec == "latent_plot":
        generate_latent_space_matrix_plot(network.forward_propagation_from_latent_space, IMAGE_WIDTH, IMAGE_HEIGHT,
                                          1,
                                          10)
