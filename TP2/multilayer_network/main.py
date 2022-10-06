from .multilayer_network import MultilayerNetwork
from ..utils.activations_functions import ActivationFunctions

def and_exercise():
    BETA = 1
    act_func = lambda x: ActivationFunctions.SIGN.value["act_func"](x, BETA)
    deriv_act_func = lambda x: ActivationFunctions.SIGN.value["deriv_act_func"](x, BETA)

    multilayer_network = MultilayerNetwork(hidden_layers_perceptron_qty=[4], input_dim=2, 
                                            output_dim=1, learning_rate=0.01, epochs=1000,
                                            act_func=act_func, deriv_act_func=deriv_act_func)

    dataset = [[1, 1, [1]], [-1, 1, [-1]], [1, -1, [-1]], [-1, -1, [-1]]]

    # multilayer_network.train_batch(train_data=dataset, test_data=dataset)
    multilayer_network.train_online(train_data=dataset, test_data=dataset)

    for example in dataset:
        print("Input: ", example[:-1])
        print("OUTPUT: ", multilayer_network.forward_propagation(example[:-1]))


if __name__ == "__main__":
    and_exercise()
