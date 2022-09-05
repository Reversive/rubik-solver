import math
import numpy as np


def fitness(target, percentage, colors):
    # prod = np.dot(percentage, colors)
    prod = [percentage[i] * colors[i] for i in range(len(colors))]
    dist = np.linalg.norm(target - sum(prod))
    return np.exp(-dist)
