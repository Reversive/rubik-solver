import numpy as np


class Member:
    def __init__(self, probabilities: np.array, fitness):
        self.probabilities = probabilities
        self.fitness = fitness

    def __str__(self):
        return "fitness {}".format(self.fitness)
