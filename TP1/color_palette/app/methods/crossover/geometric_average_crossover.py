import random
from data_structure.Color import Color
from functions.fitness import fitness


def geometric_average_crossover(first_parent: Color, second_parent: Color, target: Color) -> list[Color]:
    offspring_rgb = [get_rgb(first_parent, second_parent, lambda gamma, x1, x2: (1 - gamma) * x1 + gamma * x2),
                     get_rgb(first_parent, second_parent, lambda gamma, x1, x2: (1 - gamma) * x2 + gamma * x1)]
    return [Color(offspring_rgb[0], fitness(target, offspring_rgb[0])),
            Color(offspring_rgb[1], fitness(target, offspring_rgb[1]))]


def get_rgb(first_parent: Color, second_parent: Color, function):
    gamma = random.uniform(0, 1)
    red = function(gamma, first_parent.rgb[0], second_parent.rgb[0])
    green = function(gamma, first_parent.rgb[1], second_parent.rgb[1])
    blue = function(gamma, first_parent.rgb[2], second_parent.rgb[2])
    return [red, green, blue]
