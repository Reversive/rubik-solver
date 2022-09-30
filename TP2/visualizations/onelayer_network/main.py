import pandas as pd

from ...visualizations.onelayer_network.graphs import read_results_csv, plot_epochs_error_evolution
from ...onelayer_network.classifiers.nolinear_classifier import NoLinearClassifier, NoLinearClassifierType


def epochs_error_evolution():
    classifier = NoLinearClassifier(dataset_df, learning_rate=0.01, epochs=500,
                        CLASSIFIER_TYPE=NoLinearClassifierType.RELU,
                        BETA=0.5)

    train_accuracies, test_accuracies = classifier.execute(test_data_ratio=0.2)
    plot_epochs_error_evolution(train_accuracies, test_accuracies, range(1, len(train_accuracies) + 1))

if __name__ == "__main__":
    dataset_df = pd.read_csv("./TP2/onelayer_network/TP2-ej2-conjunto.csv", header=0)
    epochs_error_evolution()
    