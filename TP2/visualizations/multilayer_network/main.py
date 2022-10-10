import pandas as pd

from ...multilayer_network.main import xor_exercise

from ..onelayer_network.graphs import read_results_csv, plot_accuracy_of_epochs_curves_with_legend
from ...utils.activations_functions import ActivationFunctions

def epochs_accuracy_evolution_xor_exercise_train_vs_batch():
    N = 10
    batch_errors = []
    online_errors = []
    legends = []

    for i in range(N):
        train_accuracies, test_accuracies, train_errors, test_errors = xor_exercise(batch=True)
        batch_errors.append(train_errors)
        
        train_accuracies, test_accuracies, train_errors, test_errors = xor_exercise(batch=False)
        online_errors.append(train_errors)

    legends.append(f"Batch")
    legends.append(f"Online")

    plot_accuracy_of_epochs_curves_with_legend(batch_errors + online_errors, N, legends=legends, y_axis_label="Error")


if __name__ == "__main__":
    epochs_accuracy_evolution_xor_exercise_train_vs_batch()
