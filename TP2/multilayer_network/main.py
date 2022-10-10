from ..utils.files import read_numbers_from_file
from ..utils.dataset_utils import DivideDatasetToTrainAndTest
from .multilayer_network import MultilayerNetwork
from sklearn.preprocessing import StandardScaler
from ..utils.activations_functions import ActivationFunctions
import numpy as np
import pandas as pd

ROWS_PER_NUMBER = 7
COLUMNS_PER_NUMBER = 5
def xor_exercise():
    BETA = 1
    act_func_data = ActivationFunctions.SIGN
    act_func = lambda x: act_func_data.value["act_func"](x, BETA)
    deriv_act_func = lambda x: act_func_data.value["deriv_act_func"](x, BETA)
    output_transform = act_func_data.value["output_transform"]

    multilayer_network = MultilayerNetwork(hidden_layers_perceptron_qty=[2], input_dim=2, 
                                            output_dim=1, learning_rate=0.01, epochs=1000,
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

    # scalarize eor standarize xpected outputs according to function
    output_dataset_df[output_dataset_df.columns] = output_transform.fit_transform(output_dataset_df)

    train_data = []
    test_data = []
    for i in range(len(input_dataset_df)):
        train_data.append([input_dataset_df.iloc[i].tolist(), output_dataset_df.iloc[i].tolist()])
        test_data.append([input_dataset_df.iloc[i].tolist(), output_dataset_df.iloc[i].tolist()])

    # multilayer_network.train_batch(train_data, test_data)
    multilayer_network.train_online(train_data, test_data)

    for example in test_data:
        print("Input: ", example[:-1])
        print("OUTPUT: ", multilayer_network.forward_propagation(example[:-1]), "EXPECTED: ", example[-1])


def even_numbers_exercise():
    BETA = 1
    ROWS_PER_NUMBER = 7
    COLUMNS_PER_NUMBER = 5
    act_func_data = ActivationFunctions.EXP # TODO: RELU NOT WORKING
    act_func = lambda x: act_func_data.value["act_func"](x, BETA)
    deriv_act_func = lambda x: act_func_data.value["deriv_act_func"](x, BETA)
    output_transform = act_func_data.value["output_transform"]

    multilayer_network = MultilayerNetwork(hidden_layers_perceptron_qty=[COLUMNS_PER_NUMBER*ROWS_PER_NUMBER,
                                                                        COLUMNS_PER_NUMBER*ROWS_PER_NUMBER], 
                                            input_dim=COLUMNS_PER_NUMBER*ROWS_PER_NUMBER, 
                                            output_dim=2, learning_rate=0.01, epochs=100,
                                            act_func=act_func, deriv_act_func=deriv_act_func)

    expected_output = []
    for i in range(10):
        expected_output.append([i%2, (i+1)%2])    
        # for even numbers output is: [0,1], for odd: [1,0]

    dataset = get_numbers_dataset(expected_output, output_transform)

    train_dataset, test_dataset = DivideDatasetToTrainAndTest(dataset, 1)

    # multilayer_network.train_batch(train_data=dataset, test_data=dataset)
    multilayer_network.train_online(train_data=train_dataset, test_data=train_dataset)

    print_results(multilayer_network, train_dataset)

def guess_numbers_exercise():
    BETA = 1
    act_func_data = ActivationFunctions.EXP # TODO: RELU NOT WORKING
    act_func = lambda x: act_func_data.value["act_func"](x, BETA)
    deriv_act_func = lambda x: act_func_data.value["deriv_act_func"](x, BETA)
    output_transform = act_func_data.value["output_transform"]

    multilayer_network = MultilayerNetwork(hidden_layers_perceptron_qty=[COLUMNS_PER_NUMBER*ROWS_PER_NUMBER,
                                                                        COLUMNS_PER_NUMBER*ROWS_PER_NUMBER], 
                                            input_dim=COLUMNS_PER_NUMBER*ROWS_PER_NUMBER, 
                                            output_dim=10, learning_rate=0.01, epochs=10000,
                                            act_func=act_func, deriv_act_func=deriv_act_func)

    expected_output = [
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 0
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0], # 1
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0], # 8
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]  # 9
        ]

    dataset = get_numbers_dataset(expected_output, output_transform)

    train_dataset, test_dataset = DivideDatasetToTrainAndTest(dataset, 1)

    # multilayer_network.train_batch(train_data=dataset, test_data=dataset)
    multilayer_network.train_online(train_data=train_dataset, test_data=train_dataset)

    print_results(multilayer_network, train_dataset)

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

    print("accuracy: ", corrects/len(dataset))

if __name__ == "__main__":
    #xor_exercise()
    even_numbers_exercise()
    #guess_numbers_exercise()
