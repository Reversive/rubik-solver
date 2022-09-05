import random
import numpy as np
from data_structure.Member import Member
from methods.crossover.helper import crossover


def uniform_crossover(first_parent: Member, second_parent: Member, target: Member, colors) -> list[Member]:
    parents = [first_parent, second_parent]
    points = np.random.randint(0, 2, size=len(first_parent.percentage))
    return crossover(parents, points, target, colors)
