import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


def plot_accuracy_of_epochs_curves_with_legend(curves, N, legends, y_axis_label="Accuracy", x_axis_label="Epochs"):
    iters = range(1, len(curves[0]) + 1)
    colors = sns.color_palette("hls", len(legends))
    for i in range(int(len(curves) / N)):
        aux_avg, aux_std = get_average_and_std(curves[i * N:(i + 1) * N])
        plt.errorbar(iters, aux_avg, fmt='-', elinewidth=0.3, yerr=aux_std)
    # for i in range(len(curves)):
    #     plt.plot(iters, curves[i], label=legends[i], color=colors[i])

    plt.legend(legends)
    plt.xlabel(x_axis_label)
    plt.ylabel(y_axis_label)
    plt.show()


def get_average_and_std(curves):
    average = []
    std = []

    for i in range(len(curves[0])):
        aux = []
        for j in range(len(curves)):
            aux.append(curves[j][i])
        average.append(np.average(aux))
        std.append(np.std(aux))
        aux.clear()

    return average, std


def generate_latent_space_matrix_plot(predict, input_width, input_height, num_channels, n):
    # generate nxn samples
    figure = np.zeros((input_width * n, input_height * n, num_channels))

    # Create a Grid of latent variables, to be provided as inputs to decoder.predict
    # Creating vectors within range -5 to 5 as that seems to be the range in latent space
    min_range = 0.05
    max_range = 0.95
    # min_range = -5
    # max_range = 5

    grid_x = np.linspace(min_range, max_range, n)
    grid_y = np.linspace(min_range, max_range, n)[::-1]

    # decoder for each square in the grid
    for i, yi in enumerate(grid_y):
        for j, xi in enumerate(grid_x):
            z_sample = np.array([[xi, yi]])
            x_decoded = predict(z_sample)
            image = x_decoded.reshape(input_width, input_height, num_channels)
            figure[i * input_width: (i + 1) * input_width,
            j * input_height: (j + 1) * input_height] = image

    plt.figure(figsize=(10, 10))
    fig_shape = np.shape(figure)
    figure = figure.reshape((fig_shape[0], fig_shape[1], fig_shape[2]))

    if num_channels == 1:
        plt.imshow(figure, cmap='Greys_r')
    else:
        plt.imshow(figure)

    plt.axis('off')
    plt.savefig('TP3/ui/utils/pokemon.png', bbox_inches='tight', pad_inches=0)
    plt.axis('on')
    # plt.show()
