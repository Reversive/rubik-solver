import numpy as np


class Member:
    def __init__(self, percentage: np.array, fitness):
        self.percentage = percentage
        self.fitness = fitness

    def __str__(self):
        return "fitness {}".format(self.fitness)
