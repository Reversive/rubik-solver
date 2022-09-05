from functions.fitness import fitness
from data_structure.Member import Member


def crossover(parents: Member, points: [], target: Member) -> list[Member]:
    offspring_rgb = [get_rgb(parents, points[0], points[1], points[2]),
                     get_rgb(parents, 1 - points[0], 1 - points[1], 1 - points[2])]
    return [Member(offspring_rgb[0], fitness(target, offspring_rgb[0])),
            Member(offspring_rgb[1], fitness(target, offspring_rgb[1]))]


def get_rgb(parents, r_idx, g_idx, b_idx):
    return [parents[r_idx].probabilities[0], parents[g_idx].probabilities[1], parents[b_idx].probabilities[2]]
