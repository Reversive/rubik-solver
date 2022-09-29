from graphs import read_results_csv, plot_epochs_error_evolution


def main():
    train_accuracies, test_accuracies, iters  =read_results_csv("../../dump/perceptron_results.csv")
    plot_epochs_error_evolution(train_accuracies, test_accuracies, iters)

if __name__ == "__main__":
    main()
    