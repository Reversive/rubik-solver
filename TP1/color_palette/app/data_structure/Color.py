import numpy as np


class Color:
    def __init__(self, rgb: np.array, fitness):
        self.rgb = rgb
        self.fitness = fitness

    def __str__(self):
        return "{} {} {} - fitness {}".format(self.rgb[0], self.rgb[1], self.rgb[2], self.fitness)
