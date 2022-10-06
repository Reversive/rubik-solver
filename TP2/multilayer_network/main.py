from .multilayer_network import MultilayerNetwork


if __name__ == "__main__":
    multilayer_network = MultilayerNetwork(hidden_layers_perceptron_qty=[4], input_dim=2, output_dim=1, learning_rate=0.01)
    train_data = [[1, 1, [1]], [-1, 1, [-1]], [1, -1, [-1]], [-1, -1, [-1]]]
    # TODO: ESTANDARIZAR DATOS
    multilayer_network.feed_forward(train_data[0][:-1])

    multilayer_network.train(examples=train_data, epochs=1000)

    for example in train_data:
        print("Input: ", example[:-1])
        print("OUTPUT: ", multilayer_network.feed_forward(example[:-1]))
