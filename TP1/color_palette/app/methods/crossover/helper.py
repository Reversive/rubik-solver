from functions.fitness import fitness
from data_structure.Member import Member
import numpy as np


def crossover(parents: Member, points: [], target: Member, colors) -> list[Member]:
    offspring_percentage = [get_percentage(parents, points),
                            get_percentage(parents, np.subtract(np.ones(len(points), dtype=int), points))]
    return [Member(offspring_percentage[0], fitness(target, offspring_percentage[0], colors)),
            Member(offspring_percentage[1], fitness(target, offspring_percentage[1], colors))]


def get_percentage(parents, points):
    return [parents[points[i]].percentage[i] for i in range(len(points))]
