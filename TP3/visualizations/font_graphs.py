from ..font_generator import latent_space_run
from .utils import plot_accuracy_of_epochs_curves_with_legend
from ..utils.activations_functions import ActivationFunctions



def plot_error_and_accuracy_changing_act_function():
    N = 5
    errors_by_experiment = []
    accuracies_by_experiment = []
    legends = ["Signo","Linear","TanH","Logistica","RElu"]
    activation_functions = [ActivationFunctions.SIGN, ActivationFunctions.TANH, ActivationFunctions.LOGISTICA]
    for i in activation_functions:
        for j in range(N):
            train_accuracies, test_accuracies, train_errors, test_errors = latent_space_run(act_func_data=i,momentum_alpha=0.3,with_adam=True)
            errors_by_experiment.append(train_errors)
            accuracies_by_experiment.append(train_accuracies)
    plot_accuracy_of_epochs_curves_with_legend(errors_by_experiment, N, legends=legends, y_axis_label="Error")
    plot_accuracy_of_epochs_curves_with_legend(accuracies_by_experiment, N, legends=legends, y_axis_label="Accuracy")

def plot_error_and_accuracy_changing_momentum():
    N = 5
    errors_by_experiment = []
    accuracies_by_experiment = []
    legends = []
    aux = [0.1,0.2,0.3,0.5,0.8]
    for i in aux:
        for j in range(N):
            train_accuracies, test_accuracies, train_errors, test_errors = latent_space_run(act_func_data=ActivationFunctions.LOGISTICA,momentum_alpha=i,with_adam=True)
            errors_by_experiment.append(train_errors)
            accuracies_by_experiment.append(train_accuracies)
        legends.append("Momentum:" + str(i))
    plot_accuracy_of_epochs_curves_with_legend(errors_by_experiment, N, legends=legends, y_axis_label="Error")
    plot_accuracy_of_epochs_curves_with_legend(accuracies_by_experiment, N, legends=legends, y_axis_label="Accuracy")

def plot_error_and_accuracy_changing_adam():
    N = 5
    errors_by_experiment = []
    accuracies_by_experiment = []
    legends=["Optimal Architecture"]
    for j in range(N):
        train_accuracies, test_accuracies, train_errors, test_errors = latent_space_run(act_func_data=ActivationFunctions.LOGISTICA,momentum_alpha=0.5,with_adam=False)            
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
            train_accuracies, test_accuracies, train_errors, test_errors = latent_space_run(act_func_data=ActivationFunctions.LOGISTICA,momentum_alpha=0.3,with_adam=False,adaptative_learning_rate=i)
            errors_by_experiment.append(train_errors)
            accuracies_by_experiment.append(train_accuracies)
    plot_accuracy_of_epochs_curves_with_legend(errors_by_experiment, N, legends=legends, y_axis_label="Error")
    plot_accuracy_of_epochs_curves_with_legend(accuracies_by_experiment, N, legends=legends, y_axis_label="Accuracy")

def plot_error_and_accuracy_changing_noise_factor():
    N = 5
    errors_by_experiment = []
    accuracies_by_experiment = []
    legends = []
    cases = [0.1,0.2,0.5,0.7,0.9]
    for i in cases:
        for j in range(N):
            train_accuracies, test_accuracies, train_errors, test_errors = latent_space_run(act_func_data=ActivationFunctions.LOGISTICA,epochs=1000,hidden_layers_dim=[56],momentum_alpha=0.3,with_adam=True,noise=True,adaptative_learning_rate=False,noise_factor=i)
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
        [   IMAGE_WIDTH*LATENT_SPACE_DIM # 16
        ],
        [   HALF_INPUT_SIZE],
        [   HALF_INPUT_SIZE, 
            IMAGE_WIDTH*LATENT_SPACE_DIM # 16
        ],
        [   HALF_INPUT_SIZE, 
            IMAGE_WIDTH*LATENT_SPACE_DIM, # 16
            IMAGE_WIDTH],
        [   HALF_INPUT_SIZE, 
            IMAGE_WIDTH*LATENT_SPACE_DIM, # 16
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

    

def plot_error_and_accuracy_changing_layers_denoising():
    IMAGE_WIDTH = 8
    IMAGE_HEIGHT = 7
    INPUT_SIZE = 7*IMAGE_WIDTH # 56
    HALF_INPUT_SIZE = int(INPUT_SIZE/2) # 28
    LATENT_SPACE_DIM = 2

    possible_hidden_layers_dim = [
        [   HALF_INPUT_SIZE, 
            LATENT_SPACE_DIM,
            HALF_INPUT_SIZE
        ],
        [   INPUT_SIZE, 
            HALF_INPUT_SIZE,
            INPUT_SIZE
        ],
        [   INPUT_SIZE  ],

        [   INPUT_SIZE + HALF_INPUT_SIZE  ],
        
        [   INPUT_SIZE *2  ],
    ]

    N = 5
    errors_by_experiment = []
    accuracies_by_experiment = []
    legends = []

    for hidden_layers_dim in possible_hidden_layers_dim:
        print("Experimenting with hidden layers: ", hidden_layers_dim)
        for _ in range(N):
            train_accuracies, test_accuracies, train_errors, test_errors = latent_space_run(
                noise=True, noise_factor=0.1,
                hidden_layers_dim=hidden_layers_dim, epochs=1000, with_adam=True, adaptative_learning_rate=True, momentum_alpha=0.5
            )

            errors_by_experiment.append(train_errors)
            accuracies_by_experiment.append(train_accuracies)

        legends.append("Hidden layers: " + str(hidden_layers_dim))


    plot_accuracy_of_epochs_curves_with_legend(errors_by_experiment, N, legends=legends, y_axis_label="Error")

    plot_accuracy_of_epochs_curves_with_legend(accuracies_by_experiment, N, legends=legends, y_axis_label="Accuracy")

