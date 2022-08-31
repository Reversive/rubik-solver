import math


def fitness(target, base):
    return math.sqrt(pow(base[0] - target[0], 2) + pow(base[1] - target[1], 2) + pow(base[2] - target[2], 2))
