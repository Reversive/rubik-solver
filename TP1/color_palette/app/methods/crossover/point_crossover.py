import random
import numpy as np
from data_structure.Member import Member
from methods.crossover.helper import crossover


def point_crossover(first_parent: Member, second_parent: Member, target: Member, colors) -> list[Member]:
    parents = [first_parent, second_parent]
    points = np.zeros(len(first_parent.percentage), dtype=int)
    p = random.randint(0, len(points) - 1)
    for i in range(p, len(points) - 1):
        points[i] = 1
    return crossover(parents, points, target, colors)
