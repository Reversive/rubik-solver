import configparser
import numpy as np
import pandas as pd

from ..utils.activations_functions import ActivationFunctions
from .classifiers.linear_classifier import LinearClassifier
from .classifiers.nolinear_classifier import NoLinearClassifier
from .classifiers.step_classifier import StepClassifier


def config_nolinear_classifier(dataset_df, general_config, nolinear_config):
    return NoLinearClassifier(dataset_df,
                            float(general_config['learning_rate']), 
                            int(general_config['epochs']),
                            ActivationFunctions[nolinear_config['activation_function']],
                            float(nolinear_config['beta']))

def config_linear_classifier(dataset_df, general_config, linear_config):
    return LinearClassifier(dataset_df,
                            float(general_config['learning_rate']), 
                            int(general_config['epochs']))


def config_step_classifier(dataset_df, general_config, step_config):
    return StepClassifier(dataset_df, 
                            float(general_config['learning_rate']), 
                            int(general_config['epochs']),
                            float(step_config['umbral']))

def get_classifier(config, dataset_df = None):
    general_config = config['general_config']
    if dataset_df is None:
        dataset_df = pd.read_csv(general_config['dataset'], header=0)
    if general_config['classifier'] == 'step':
        return config_step_classifier(dataset_df, general_config, config['step_classifier'])
    elif (general_config['classifier'] == 'linear'):
        return config_linear_classifier(dataset_df, general_config, config['linear_classifier'])
    elif general_config['classifier'] == 'nolinear':
        return config_nolinear_classifier(dataset_df, general_config, config['nolinear_classifier'])

def ej1():
    learning_rate = 0.01
    epochs = 5
    umbral = 0

    # print("AND exercise")
    # and_train_dataset = [[-1, 1, -1], [1, -1, -1], [-1, -1, -1], [1, 1, 1]]
    # classifier = StepClassifier(and_train_dataset, learning_rate, epochs, umbral)
    # classifier.execute()
    
    print("XOR exercise")
    xor_train_dataset = [[-1, 1, 1], [1, -1, 1], [-1, -1, -1], [1, 1, -1]]
    classifier = StepClassifier(xor_train_dataset, learning_rate, epochs, umbral)
    classifier.execute()

def cross_validation(accuracies = True, k = 5):
    config = configparser.ConfigParser()
    config.read("./TP2/onelayer_network/config.yaml")
    general_config = config['general_config']
    dataset_df = pd.read_csv(general_config['dataset'], header=0)
    dataset_df = dataset_df.sample(frac=1).reset_index(drop=True)
    dataset = dataset_df.values
    dataset = np.array_split(dataset, k)

    train_results = []
    test_results = []

    for i in range(k):
        test_dataset = dataset[i]
        train_dataset = np.concatenate(dataset[:i] + dataset[i+1:])
        train_dataset_df = pd.DataFrame(train_dataset)
        test_dataset_df = pd.DataFrame(test_dataset)

        classifier = get_classifier(config, train_dataset_df)
        train_result, test_result = classifier.execute()
        train_results.append(train_result)
        test_results.append(test_result)
            
    return train_results, test_results


if __name__ == "__main__":

    # ej1()

    config = configparser.ConfigParser()
    config.read("./TP2/onelayer_network/config.yaml")

    np.random.seed(12345)
    cross_validation()
    # classifier = get_classifier(config)
    # classifier.execute()

