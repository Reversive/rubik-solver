from ..font_generator import latent_space_run
from .utils import plot_accuracy_of_epochs_curves_with_legend

IMAGE_WIDTH = 8
IMAGE_HEIGHT = 7
INPUT_SIZE = 7*IMAGE_WIDTH
LATENT_SPACE_DIM = 2

def plot_error_and_accuracy_changing_layers():
    possible_hidden_layers_dim = [
        [   LATENT_SPACE_DIM   ],
        [   INPUT_SIZE,
            LATENT_SPACE_DIM,
            INPUT_SIZE],
        [   INPUT_SIZE, 
            IMAGE_WIDTH*LATENT_SPACE_DIM,
            LATENT_SPACE_DIM,
            IMAGE_WIDTH*LATENT_SPACE_DIM, 
            INPUT_SIZE],
        [   INPUT_SIZE, 
            IMAGE_WIDTH*LATENT_SPACE_DIM,
            IMAGE_WIDTH,
            LATENT_SPACE_DIM,
            IMAGE_WIDTH,
            IMAGE_WIDTH*LATENT_SPACE_DIM, 
            INPUT_SIZE],
        [   INPUT_SIZE, 
            IMAGE_WIDTH*LATENT_SPACE_DIM,
            IMAGE_WIDTH,
            LATENT_SPACE_DIM*LATENT_SPACE_DIM,
            LATENT_SPACE_DIM,
            LATENT_SPACE_DIM*LATENT_SPACE_DIM,
            IMAGE_WIDTH,
            IMAGE_WIDTH*LATENT_SPACE_DIM, 
            INPUT_SIZE],
    ]

    N = 5
    errors_by_experiment = []
    accuracies_by_experiment = []
    legends = []

    for hidden_layers_dim in possible_hidden_layers_dim:
        print("Experimenting with hidden layers: ", hidden_layers_dim)
        for _ in range(N):
            train_accuracies, test_accuracies, train_errors, test_errors = latent_space_run(
                hidden_layers_dim=hidden_layers_dim,
            )

            errors_by_experiment.append(train_errors)
            accuracies_by_experiment.append(train_accuracies)

        legends.append("Hidden layers: " + str(hidden_layers_dim))


    plot_accuracy_of_epochs_curves_with_legend(errors_by_experiment, N, legends=legends, y_axis_label="Error")

    plot_accuracy_of_epochs_curves_with_legend(accuracies_by_experiment, N, legends=legends, y_axis_label="Accuracy")

