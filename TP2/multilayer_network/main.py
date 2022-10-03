from .multilayer_network import MultilayerNetwork


if __name__ == "__main__":
    # create and test multilayer network
    multilayer_network = MultilayerNetwork(1)
    # train data
    train_data = [[1, 1, [1]], [-1, 1, [-1]], [1, -1, [-1]], [-1, -1, [-1]]]

    for i in range(1000):
        multilayer_network.train(train_data)

    for example in train_data:
        print(multilayer_network.classify(example[:-1]))


    # for layer in multilayer_network.layers:
    #     print(layer.perceptrons_weights)