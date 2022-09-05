import math
import numpy as np


def fitness(target, percentage, colors):
    # prod = np.dot(percentage, colors)
    prod = [percentage[i] * colors[i] for i in range(len(percentage))]
    dist = np.linalg.norm(target - np.clip(sum(prod), 0, 1))

    print(percentage)
    return np.sqrt(len(target)) - dist
