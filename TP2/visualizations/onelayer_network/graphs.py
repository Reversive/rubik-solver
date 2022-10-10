import numpy
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


def read_results_csv(file):
    df = pd.read_csv(file, header=0)
    train_accuracies = df["TRAIN_ACCURACY"].values
    test_accuracies = df["TEST_ACCURACY"].values
    iters = df["EPOCH"].values

    return train_accuracies, test_accuracies, iters


def plot_accuracy_of_epochs_curves_with_legend(curves, N, legends, y_axis_label="Accuracy", x_axis_label="Epochs"):
    iters = range(1, len(curves[0]) + 1)
    colors = sns.color_palette("hls", len(legends))
    for i in range(int(len(curves) / N) - 1):
        aux_avg, aux_std = get_average_and_std(curves[i * N:(i + 1) * N])
        plt.errorbar(iters, aux_avg, fmt='o-', yerr=aux_std)
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
        average.append(numpy.average(aux))
        std.append(numpy.std(aux))
        aux.clear()

    return average, std
