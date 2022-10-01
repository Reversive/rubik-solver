import pandas as pd

from ...visualizations.onelayer_network.graphs import read_results_csv, plot_accuracy_of_epochs_curves_with_legend
from ...onelayer_network.classifiers.nolinear_classifier import NoLinearClassifier, NoLinearClassifierType


def epochs_error_evolution_test_division(dataset_df):
    classifier = NoLinearClassifier(dataset_df, learning_rate=0.01, epochs=10000,
                        CLASSIFIER_TYPE=NoLinearClassifierType.RELU,
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

def epochs_error_evolution(dataset_df):
    classifier = NoLinearClassifier(dataset_df, learning_rate=0.01, epochs=20000,
                        CLASSIFIER_TYPE=NoLinearClassifierType.RELU,
                        BETA=1)
    curves = []
    legends = []

    train_accuracies, test_accuracies = classifier.execute(test_data_ratio=0.3)
    curves.append(train_accuracies)
    legends.append(f"Train")
    curves.append(test_accuracies)
    legends.append(f"Test")
    plot_accuracy_of_epochs_curves_with_legend(curves, legends)


if __name__ == "__main__":
    dataset_df = pd.read_csv("./TP2/onelayer_network/TP2-ej2-conjunto.csv", header=0)
    # epochs_error_evolution_test_division(dataset_df)
    epochs_error_evolution(dataset_df)
    