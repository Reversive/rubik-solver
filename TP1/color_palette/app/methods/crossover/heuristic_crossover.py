import random

from functions.fitness import fitness
from data_structure.Color import Color


def heuristic_crossover(first_parent: Color, second_parent: Color, target: Color) -> list[Color]:
    # offspring_rgb = [get_rgb(first_parent, second_parent, lambda r, x1, x2: r * (x1 - x2) + x1),
    #                  get_rgb(first_parent, second_parent, lambda r, x1, x2: r * (x1 - x2) + x2)]
    # return [Color(offspring_rgb[0], fitness(target, offspring_rgb[0])),
    #         Color(offspring_rgb[1], fitness(target, offspring_rgb[1]))]
    offspring_rgb = get_rgb(first_parent, second_parent, lambda r, x1, x2: r * (x1 - x2) + x2);
    return [Color(offspring_rgb, fitness(target, offspring_rgb))]


def get_rgb(first_parent: Color, second_parent: Color, function):
    r = random.uniform(0, 1)
    red = function(r, min(first_parent.rgb[0], second_parent.rgb[0]), max(first_parent.rgb[0], second_parent.rgb[0]))
    green = function(r, min(first_parent.rgb[1], second_parent.rgb[1]), max(first_parent.rgb[1], second_parent.rgb[1]))
    blue = function(r, min(first_parent.rgb[2], second_parent.rgb[2]), max(first_parent.rgb[2], second_parent.rgb[2]))
    return [red, green, blue]
