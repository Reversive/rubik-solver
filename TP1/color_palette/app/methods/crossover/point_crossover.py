import random

from data_structure.Color import Color

from methods.crossover.helper import crossover


def point_crossover(first_parent: Color, second_parent: Color, target: Color) -> list[Color]:
    parents = [first_parent, second_parent]
    points = [0, 0, 0]
    p = random.randint(0, len(points) - 1)
    for i in range(p, len(points) - 1):
        points[i] = 1
    return crossover(parents, points, target)
