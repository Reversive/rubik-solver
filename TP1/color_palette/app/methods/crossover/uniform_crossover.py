import random

from functions.fitness import fitness
from data_structure.Color import Color


def uniform_crossover(first_parent: Color, second_parent: Color, target: Color) -> list[Color]:
    parents = [first_parent, second_parent]
    r_idx = random.randint(0, 1)
    b_idx = random.randint(0, 1)
    g_idx = random.randint(0, 1)
    offspring_rgb = [get_rgb(parents, r_idx, g_idx, b_idx), get_rgb(parents, 1 - r_idx, 1 - g_idx, 1 - b_idx)]
    return [Color(offspring_rgb[0], fitness(target, offspring_rgb[0])),
            Color(offspring_rgb[1], fitness(target, offspring_rgb[1]))]


def get_rgb(parents, r_idx, g_idx, b_idx):
    red = parents[r_idx].rgb[0]
    green = parents[g_idx].rgb[1]
    blue = parents[b_idx].rgb[2]
    total = red + green + blue
    return [red / total, green / total, blue / total]
