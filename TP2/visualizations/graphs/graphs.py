import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

def read_results_csv(file):
    df = pd.read_csv(file, header=0)
    train_accuracies = df["TRAIN_ACCURACY"].values
    test_accuracies = df["TEST_ACCURACY"].values
    iters = df["EPOCH"].values
    
    return train_accuracies, test_accuracies, iters

def plot_epochs_error_evolution(train_accuracies, test_accuracies, iters):
    plt.plot(iters, train_accuracies, label="Train", color='r')
    plt.plot(iters, test_accuracies, label="Test", color='b')
    plt.legend()
    plt.xlabel("Epochs")
    plt.ylabel("Accuracy")
    plt.show()

