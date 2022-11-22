from ..font_generator import latent_space_run
from .utils import plot_accuracy_of_epochs_curves_with_legend
from ..utils.activations_functions import ActivationFunctions



def plot_error_and_accuracy_changing_act_function():
    N = 5
    errors_by_experiment = []
    accuracies_by_experiment = []
    legends = ["Signo","TanH","Logistica"]
    activation_functions = [ActivationFunctions.SIGN, ActivationFunctions.TANH, ActivationFunctions.LOGISTICA]
    for i in activation_functions:
        for j in range(N):
            train_accuracies, test_accuracies, train_errors, test_errors = latent_space_run(act_func_data=i,momentum_alpha=0.8,with_adam=False)
            errors_by_experiment.append(train_errors)
            accuracies_by_experiment.append(train_accuracies)
    plot_accuracy_of_epochs_curves_with_legend(errors_by_experiment, N, legends=legends, y_axis_label="Error")
    plot_accuracy_of_epochs_curves_with_legend(accuracies_by_experiment, N, legends=legends, y_axis_label="Accuracy")

def plot_error_and_accuracy_changing_momentum():
    N = 5
    errors_by_experiment = []
    accuracies_by_experiment = []
    legends = []
    aux = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
    for i in aux:
        for j in range(N):
            train_accuracies, test_accuracies, train_errors, test_errors = latent_space_run(act_func_data=ActivationFunctions.LOGISTICA,momentum_alpha=i,with_adam=False)
            errors_by_experiment.append(train_errors)
            accuracies_by_experiment.append(train_accuracies)
        legends.append("Momentum:" + str(i))
    plot_accuracy_of_epochs_curves_with_legend(errors_by_experiment, N, legends=legends, y_axis_label="Error")
    plot_accuracy_of_epochs_curves_with_legend(accuracies_by_experiment, N, legends=legends, y_axis_label="Accuracy")

def plot_error_and_accuracy_changing_adam():
    N = 5
    errors_by_experiment = []
    accuracies_by_experiment = []
    legends = ["Adam: True", "Adam: False"]
    cases = [True, False]
    for i in cases:
        for j in range(N):
            train_accuracies, test_accuracies, train_errors, test_errors = latent_space_run(act_func_data=ActivationFunctions.LOGISTICA,momentum_alpha=0.8,with_adam=i)
            errors_by_experiment.append(train_errors)
            accuracies_by_experiment.append(train_accuracies)
    plot_accuracy_of_epochs_curves_with_legend(errors_by_experiment, N, legends=legends, y_axis_label="Error")
    plot_accuracy_of_epochs_curves_with_legend(accuracies_by_experiment, N, legends=legends, y_axis_label="Accuracy")


def plot_error_and_accuracy_changing_learning_rate():
    N = 5
    errors_by_experiment = []
    accuracies_by_experiment = []
    legends = ["Adaptative learning rate: True", "Adaptative learning rate: False"]
    cases = [True, False]
    for i in cases:
        for j in range(N):
            train_accuracies, test_accuracies, train_errors, test_errors = latent_space_run(act_func_data=ActivationFunctions.LOGISTICA,momentum_alpha=0.2,with_adam=False,adaptative_learning_rate=i)
            errors_by_experiment.append(train_errors)
            accuracies_by_experiment.append(train_accuracies)
    plot_accuracy_of_epochs_curves_with_legend(errors_by_experiment, N, legends=legends, y_axis_label="Error")
    plot_accuracy_of_epochs_curves_with_legend(accuracies_by_experiment, N, legends=legends, y_axis_label="Accuracy")

def plot_error_and_accuracy_changing_noise_factor():
    N = 5
    errors_by_experiment = []
    accuracies_by_experiment = []
    legends = []
    cases = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
    for i in cases:
        for j in range(N):
            train_accuracies, test_accuracies, train_errors, test_errors = latent_space_run(act_func_data=ActivationFunctions.LOGISTICA,momentum_alpha=0.8,with_adam=True,noise=True,noise_factor=i)
            errors_by_experiment.append(train_errors)
            accuracies_by_experiment.append(train_accuracies)
        legends.append("Noise Factor: " + str(i))
    plot_accuracy_of_epochs_curves_with_legend(errors_by_experiment, N, legends=legends, y_axis_label="Error")
    plot_accuracy_of_epochs_curves_with_legend(accuracies_by_experiment, N, legends=legends, y_axis_label="Accuracy")

def plot_error_and_accuracy_changing_layers():
    IMAGE_WIDTH = 8
    IMAGE_HEIGHT = 7
    INPUT_SIZE = 7*IMAGE_WIDTH # 56
    HALF_INPUT_SIZE = int(INPUT_SIZE/2) # 28
    LATENT_SPACE_DIM = 2

    possible_left_hidden_layers_dim = [
        [      ],
        [   IMAGE_WIDTH*LATENT_SPACE_DIM # 14
        ],
        [   HALF_INPUT_SIZE],
        [   HALF_INPUT_SIZE, 
            IMAGE_WIDTH*LATENT_SPACE_DIM # 14
        ],
        [   HALF_INPUT_SIZE, 
            IMAGE_WIDTH*LATENT_SPACE_DIM, # 14
            IMAGE_WIDTH],
        [   HALF_INPUT_SIZE, 
            IMAGE_WIDTH*LATENT_SPACE_DIM, # 14
            IMAGE_WIDTH,
            LATENT_SPACE_DIM*LATENT_SPACE_DIM],
    ]

    N = 5
    errors_by_experiment = []
    accuracies_by_experiment = []
    legends = []

    for left_hidden_layers_dim in possible_left_hidden_layers_dim:
        hidden_layers_dim = left_hidden_layers_dim + [LATENT_SPACE_DIM] + left_hidden_layers_dim[::-1]
        print("Experimenting with hidden layers: ", hidden_layers_dim)
        for _ in range(N):
            train_accuracies, test_accuracies, train_errors, test_errors = latent_space_run(
                hidden_layers_dim=hidden_layers_dim,
            )

            errors_by_experiment.append(train_errors)
            accuracies_by_experiment.append(train_accuracies)

        legends.append("Left hidden layers: " + str(left_hidden_layers_dim))


    plot_accuracy_of_epochs_curves_with_legend(errors_by_experiment, N, legends=legends, y_axis_label="Error")

    plot_accuracy_of_epochs_curves_with_legend(accuracies_by_experiment, N, legends=legends, y_axis_label="Accuracy")

