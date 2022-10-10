import pandas as pd

from ...onelayer_network.main import cross_validation

from .graphs import read_results_csv, plot_accuracy_of_epochs_curves_with_legend
from ...onelayer_network.classifiers.nolinear_classifier import NoLinearClassifier
from ...utils.activations_functions import ActivationFunctions


def epochs_accuracy_evolution_crossvalidation():
    k=5
    train_curves, test_curves = cross_validation(k)
    legends = [f"Conjunto {i}" for i in range(k)]

    plot_accuracy_of_epochs_curves_with_legend(test_curves, legends)


def epochs_accuracy_evolution_test_division(dataset_df):
    classifier = NoLinearClassifier(dataset_df, learning_rate=0.01, epochs=200,
                        act_functions=ActivationFunctions.TANH,
                        BETA=0.5)

    curves = []
    legends = []
    division_list = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7]
    for division in division_list:
        train_accuracies, test_accuracies = classifier.execute(test_data_ratio=division)
        # curves.append(train_accuracies)
        # legends.append(f"Train {division}")
        curves.append(test_accuracies)
        legends.append(f"Test {division}")

    plot_accuracy_of_epochs_curves_with_legend(curves, legends)

def accurracy_vs_epochs_over_beta_evolution(dataset_df):
    curves = []
    legends = []
    for i in [5,10,15,20,25]:
        classifier = NoLinearClassifier(dataset_df, learning_rate=0.01, epochs=200,
                        act_functions=ActivationFunctions.TANH,
                        BETA=i/10)
        train_accuracies, test_accuracies = classifier.execute(test_data_ratio=0.3)
        curves.append(train_accuracies)
        legends.append(f"Beta:" + str(i/10))
        # curves.append(test_accuracies)
        # legends.append(f"Test")
    plot_accuracy_of_epochs_curves_with_legend(curves, legends)

def accurracy_vs_epochs_over_learning_rate(dataset_df):
    curves = []
    legends = []
    for i in [0.1,0.5,1,1.5,2]:
        classifier = NoLinearClassifier(dataset_df, learning_rate=i/10, epochs=200,
                        act_functions=ActivationFunctions.TANH,
                        BETA=1.0)
        train_accuracies, test_accuracies = classifier.execute(test_data_ratio=0.3)
        # curves.append(train_accuracies)
        legends.append(f"Learning rate:" + str(i/10))
        curves.append(test_accuracies)
        # legends.append(f"Test")
    plot_accuracy_of_epochs_curves_with_legend(curves, legends)

def act_function(dataset_df):
    curves = []
    legends = []
    classifier = NoLinearClassifier(dataset_df, learning_rate=0.05, epochs=200,
                        act_functions=ActivationFunctions.EXP,
                        BETA=1.0)
    train_accuracies, test_accuracies = classifier.execute(test_data_ratio=0.3,batch_train=True)
    curves.append(test_accuracies)
    classifier = NoLinearClassifier(dataset_df, learning_rate=0.05, epochs=200,
                        act_functions=ActivationFunctions.TANH,
                        BETA=1.0)
    train_accuracies, test_accuracies = classifier.execute(test_data_ratio=0.3,batch_train=True)
    curves.append(test_accuracies)
    classifier = NoLinearClassifier(dataset_df, learning_rate=0.05, epochs=200,
                        act_functions=ActivationFunctions.RELU,
                        BETA=1.0)
    train_accuracies, test_accuracies = classifier.execute(test_data_ratio=0.3,batch_train=True)
    # curves.append(train_accuracies)
    legends.append(f"Act: EXP")
    legends.append(f"Act: TANH")
    legends.append(f"Act: RELU")
    curves.append(test_accuracies)
    plot_accuracy_of_epochs_curves_with_legend(curves, legends)

def train_vs_batch(dataset_df):
    curves = []
    legends = []
    classifier = NoLinearClassifier(dataset_df, learning_rate=0.01, epochs=200,
                        act_functions=ActivationFunctions.TANH,
                        BETA=1.0)
    train_accuracies, test_accuracies = classifier.execute(test_data_ratio=0.3,batch_train=True)
    curves.append(train_accuracies)
    legends.append(f"Batch: Train")
    legends.append(f"Batch: Test")
    curves.append(test_accuracies)
    classifier = NoLinearClassifier(dataset_df, learning_rate=0.01, epochs=200,
                        act_functions=ActivationFunctions.TANH,
                        BETA=1.0)
    train_accuracies, test_accuracies = classifier.execute(test_data_ratio=0.3,batch_train=False)
    curves.append(train_accuracies)
    legends.append(f"Online: Train")
    legends.append(f"Online: Test")
    curves.append(test_accuracies)
    # legends.append(f"Test")
    plot_accuracy_of_epochs_curves_with_legend(curves, legends)

if __name__ == "__main__":
    dataset_df = pd.read_csv("./TP2/onelayer_network/TP2-ej2-conjunto.csv", header=0)
    # epochs_error_evolution_test_division(dataset_df)
    #accurracy_vs_epochs_over_learning_rate(dataset_df)
    epochs_accuracy_evolution_crossvalidation()
