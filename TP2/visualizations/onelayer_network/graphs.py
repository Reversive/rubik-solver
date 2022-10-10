import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

def read_results_csv(file):
    df = pd.read_csv(file, header=0)
    train_accuracies = df["TRAIN_ACCURACY"].values
    test_accuracies = df["TEST_ACCURACY"].values
    iters = df["EPOCH"].values
    
    return train_accuracies, test_accuracies, iters

def plot_accuracy_of_epochs_curves_with_legend(curves, legends, y_axis_label="Accuracy", x_axis_label="Epochs"):
    iters = range(1, len(curves[0]) + 1)
    colors = sns.color_palette("hls", len(legends))
    for i in range(len(curves)):
        plt.plot(iters, curves[i], label=legends[i], color=colors[i])

    plt.legend()
    plt.xlabel(x_axis_label)
    plt.ylabel(y_axis_label)
    plt.show()
