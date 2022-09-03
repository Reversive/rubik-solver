from functions.fitness import fitness
from data_structure.Color import Color


def crossover(parents: Color, points: [], target: Color) -> list[Color]:
    offspring_rgb = [get_rgb(parents, points[0], points[1], points[2]),
                     get_rgb(parents, 1 - points[0], 1 - points[1], 1 - points[2])]
    return [Color(offspring_rgb[0], fitness(target, offspring_rgb[0])),
            Color(offspring_rgb[1], fitness(target, offspring_rgb[1]))]


def get_rgb(parents, r_idx, g_idx, b_idx):
    return [parents[r_idx].rgb[0], parents[g_idx].rgb[1], parents[b_idx].rgb[2]]
