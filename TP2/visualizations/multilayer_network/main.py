import pandas as pd

from ...multilayer_network.main import xor_exercise, even_numbers_exercise, train_guess_number

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

def error_graph_even_numbers_train_vs_test():
    N = 10
    traineroo_errors = []
    testeroo_errors = []
    legends = []

    for i in range(N):
        train_accuracies, test_accuracies, train_errors, test_errors = even_numbers_exercise()
        traineroo_errors.append(train_accuracies)
        testeroo_errors.append(test_accuracies)


    legends.append(f"Train")
    legends.append(f"Test")

    plot_accuracy_of_epochs_curves_with_legend(traineroo_errors + testeroo_errors, N, legends=legends)

def error_over_momentum():
    N = 10
    curves = []
    legends = []
    for i in [0.1,0.2,0.4,0.6,0.8]:
        for j in range(N):
            train_accuracies, test_accuracies, train_errors, test_errors = even_numbers_exercise(momentum=i)
            curves.append(test_errors)
        legends.append(f"Momentum:" + str(i))
    plot_accuracy_of_epochs_curves_with_legend(curves, N, legends,y_axis_label='Errors')

def even_with_noise():
    N = 10
    traineroo_errors = []
    testeroo_errors = []
    legends = []

    for i in range(N):
        train_accuracies, test_accuracies, train_errors, test_errors = even_numbers_exercise(noisy_test=True)
        traineroo_errors.append(train_errors)
        testeroo_errors.append(test_errors)


    legends.append(f"Train")
    legends.append(f"Test")

    plot_accuracy_of_epochs_curves_with_legend(traineroo_errors + testeroo_errors, N, legends=legends,y_axis_label="Error")

def guess_variating_noise():
    N = 10
    curve_exp = []
    curve_tanh = []

    legends = []

    for i in range(N):
        train_accuracies, test_accuracies, train_errors, test_errors = train_guess_number(act_func_data=ActivationFunctions.LOGISTICA,noisy_test=True)
        curve_exp.append(test_accuracies)
        train_accuracies, test_accuracies, train_errors, test_errors = train_guess_number(act_func_data=ActivationFunctions.TANH, noisy_test=True)
        curve_tanh.append(test_accuracies)
        # testeroo_errors.append(test_accuracies)


    legends.append(f"Act: LOGISTICA")
    legends.append(f"Act: TANH")

    plot_accuracy_of_epochs_curves_with_legend(curve_exp + curve_tanh, N, legends=legends,y_axis_label="Accuracy")

if __name__ == "__main__":
    guess_variating_noise()
