import random

from data_structure.Member import Member

from methods.crossover.helper import crossover


def point_crossover(first_parent: Member, second_parent: Member, target: Member) -> list[Member]:
    parents = [first_parent, second_parent]
    points = [0, 0, 0]
    p = random.randint(0, len(points) - 1)
    for i in range(p, len(points) - 1):
        points[i] = 1
    return crossover(parents, points, target)
