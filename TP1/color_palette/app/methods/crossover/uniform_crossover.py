import random

from data_structure.Color import Color
from methods.crossover.helper import crossover


def uniform_crossover(first_parent: Color, second_parent: Color, target: Color) -> list[Color]:
    parents = [first_parent, second_parent]
    idx = [random.randint(0, 1), random.randint(0, 1), random.randint(0, 1)]
    return crossover(parents, idx, target)
