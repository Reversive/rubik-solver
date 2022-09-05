import random

from data_structure.Member import Member
from methods.crossover.helper import crossover


def uniform_crossover(first_parent: Member, second_parent: Member, target: Member) -> list[Member]:
    parents = [first_parent, second_parent]
    idx = [random.randint(0, 1), random.randint(0, 1), random.randint(0, 1)]
    return crossover(parents, idx, target)
