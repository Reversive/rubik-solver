import math
import numpy as np


def fitness(target, percentage, colors):
    # prod = np.dot(percentage, colors)
    prod = [percentage[i] * colors[i] for i in range(len(percentage))]
    dist = np.linalg.norm(target - sum(prod))
    print(dist)
    if dist > 1:
        return 1
    return dist
