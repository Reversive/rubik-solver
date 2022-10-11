import pandas as pd

from ...onelayer_network.main import cross_validation

from .graphs import read_results_csv, plot_accuracy_of_epochs_curves_with_legend
from ...onelayer_network.classifiers.nolinear_classifier import NoLinearClassifier
from ...utils.activations_functions import ActivationFunctions


def epochs_accuracy_evolution_crossvalidation():
    k=3
    accuracies = False
    train_results_list, test_results_list = cross_validation(k = k, accuracies=accuracies)
    legends = [f"Conjunto {i}" for i in range(k)]

    plot_accuracy_of_epochs_curves_with_legend(test_results_list, 1, legends, y_axis_label="Accuracy" if accuracies else "Error")


def epochs_accuracy_evolution_test_division(dataset_df):
    classifier = NoLinearClassifier(dataset_df, learning_rate=0.05, epochs=250,
                        act_functions=ActivationFunctions.EXP,
                        BETA=0.5)

    curves = []
    legends = []
    division_list = [0.1, 0.3, 0.5, 0.7, 0.9]
    N = 10
    for division in division_list:
        for i in range(N):
            classifier = NoLinearClassifier(dataset_df, learning_rate=0.05, epochs=250,
                        act_functions=ActivationFunctions.TANH,
                        BETA=1.0)
            train_accuracies, test_accuracies, train_errors, test_errors = classifier.execute(train_data_ratio=division)
            # curves.append(train_accuracies)

            curves.append(test_errors)
        # legends.append(f"Train {division}")
        legends.append(f"Train rate: {division}")

    plot_accuracy_of_epochs_curves_with_legend(curves,N, legends,y_axis_label="Errors")

def accurracy_vs_epochs_over_beta_evolution(dataset_df):
    curves = []
    legends = []
    N = 10
    for i in [5,10,20]:
        for j in range(N):
            classifier = NoLinearClassifier(dataset_df, learning_rate=0.05, epochs=250,
                        act_functions=ActivationFunctions.RELU,
                        BETA=i/10)
            train_accuracies, test_accuracies, train_errors, test_errors = classifier.execute(train_data_ratio=0.7)
            # curves.append(train_accuracies)
            curves.append(train_accuracies)
            # legends.append(f"Test")
        legends.append(f"Beta:" + str(i/10))

    plot_accuracy_of_epochs_curves_with_legend(curves,N, legends)

def accurracy_vs_epochs_over_learning_rate(dataset_df):
    curves = []
    legends = []
    N = 10
    for i in [0.1,0.5,1,2]:
        for j in range(N):
            classifier = NoLinearClassifier(dataset_df, learning_rate=i/10, epochs=250,
                        act_functions=ActivationFunctions.TANH,
                        BETA=1.0)
            train_accuracies, test_accuracies, train_errors, test_errors = classifier.execute(train_data_ratio=0.7)
            curves.append(train_accuracies)
            # curves.append(test_accuracies)
            # legends.append(f"Test")
        legends.append(f"Learning rate:" + str(i / 10))
    plot_accuracy_of_epochs_curves_with_legend(curves,N, legends)


def linear_function(dataset_df):
    curves = []
    legends = []
    N = 10
    for j in range(N):
        classifier = NoLinearClassifier(dataset_df, learning_rate=0.05, epochs=250,
                        act_functions=ActivationFunctions.LINEAR,BETA=1.0)

        train_accuracies, test_accuracies, train_errors, test_errors = classifier.execute(train_data_ratio=0.7)
        curves.append(train_errors)
        curves.append(test_errors)
    
    legends.append(f"Train")
    legends.append(f"Test")
    plot_accuracy_of_epochs_curves_with_legend(curves, N, legends, y_axis_label="Error")

def act_function(dataset_df):
    curve_exp = []
    curve_tanh = []
    curve_relu = []
    legends = []
    N = 10
    for i in range(N):
        classifier = NoLinearClassifier(dataset_df, learning_rate=0.05, epochs=250,
                        act_functions=ActivationFunctions.EXP,
                        BETA=1.0)
        train_accuracies, test_accuracies, train_errors, test_errors = classifier.execute(train_data_ratio=0.7)
        curve_exp.append(test_errors)
        classifier = NoLinearClassifier(dataset_df, learning_rate=0.05, epochs=250,
                        act_functions=ActivationFunctions.TANH,
                        BETA=1.0)
        train_accuracies, test_accuracies, train_errors, test_errors = classifier.execute(train_data_ratio=0.7)
        curve_tanh.append(test_errors)
        classifier = NoLinearClassifier(dataset_df, learning_rate=0.05, epochs=250,
                        act_functions=ActivationFunctions.RELU,
                        BETA=1.0)
        train_accuracies, test_accuracies, train_errors, test_errors = classifier.execute(train_data_ratio=0.7)
        curve_relu.append(test_errors)
        # curves.append(train_accuracies)
    legends.append(f"Act: EXP")
    legends.append(f"Act: TANH")
    legends.append(f"Act: RELU")

    plot_accuracy_of_epochs_curves_with_legend(curve_exp + curve_tanh + curve_relu,N, legends,y_axis_label="Errors")

def train_vs_batch(dataset_df):
    legends = []
    N = 10
    batch_train = []
    batch_test = []
    online_train = []
    online_test = []
    for i in range(N):
        classifier = NoLinearClassifier(dataset_df, learning_rate=0.05, epochs=250,
                        act_functions=ActivationFunctions.EXP,
                        BETA=1.0)
        train_accuracies, test_accuracies, train_errors, test_errors = classifier.execute(train_data_ratio=0.7,batch_train=True)
        batch_train.append(train_accuracies)
        batch_test.append(test_accuracies)
        classifier = NoLinearClassifier(dataset_df, learning_rate=0.05, epochs=250,
                        act_functions=ActivationFunctions.EXP,
                        BETA=1.0)
        train_accuracies, test_accuracies, train_errors, test_errors = classifier.execute(train_data_ratio=0.7,batch_train=False)
        online_train.append(train_accuracies)
        online_test.append(test_accuracies)
    legends.append(f"Batch: Train")
    legends.append(f"Batch: Test")
    legends.append(f"Online: Train")
    legends.append(f"Online: Test")

    # legends.append(f"Test")
    plot_accuracy_of_epochs_curves_with_legend(batch_train + batch_test + online_train + online_test,N, legends)

def plot_accuracy_of_epochs_simple_perceptron():
    legends = []
    N = 10
    train = []
    test = []
    for i in range(N):
        classifier = NoLinearClassifier(dataset_df, learning_rate=0.05, epochs=250,
                        act_functions=ActivationFunctions.EXP,
                        BETA=1.0)
        train_accuracies, test_accuracies, train_errors, test_errors = classifier.execute(train_data_ratio=0.7)
        train.append(train_accuracies)
        test.append(test_accuracies)

    legends.append(f"Train")
    legends.append(f"Test")

    # legends.append(f"Test")
    plot_accuracy_of_epochs_curves_with_legend(train + test,N, legends)


if __name__ == "__main__":
    dataset_df = pd.read_csv("./TP2/onelayer_network/TP2-ej2-conjunto.csv", header=0)
    # epochs_error_evolution_test_division(dataset_df)
    # act_function(dataset_df)
    epochs_accuracy_evolution_crossvalidation()
    # plot_accuracy_of_epochs_simple_perceptron()
    # accurracy_vs_epochs_over_beta_evolution(dataset_df)
    # linear_function(dataset_df)