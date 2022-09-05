import random

from functions.fitness import fitness
from data_structure.Member import Member


def heuristic_crossover(first_parent: Member, second_parent: Member, target: Member, colors) -> list[Member]:
    # offspring_rgb = [get_rgb(first_parent, second_parent, lambda r, x1, x2: r * (x1 - x2) + x1),
    #                  get_rgb(first_parent, second_parent, lambda r, x1, x2: r * (x1 - x2) + x2)]
    # return [Member(offspring_rgb[0], fitness(target, offspring_rgb[0])),
    #         Member(offspring_rgb[1], fitness(target, offspring_rgb[1]))]
    offspring_rgb = get_rgb(first_parent, second_parent, lambda r, x1, x2: r * (x1 - x2) + x2);
    return [Member(offspring_rgb, fitness(target, offspring_rgb, colors))]


def get_rgb(first_parent: Member, second_parent: Member, function):
    r = random.uniform(0, 1)
    red = function(r, min(first_parent.percentage[0], second_parent.percentage[0]), max(first_parent.percentage[0], second_parent.percentage[0]))
    green = function(r, min(first_parent.percentage[1], second_parent.percentage[1]), max(first_parent.percentage[1], second_parent.percentage[1]))
    blue = function(r, min(first_parent.percentage[2], second_parent.percentage[2]), max(first_parent.percentage[2], second_parent.percentage[2]))
    return [red, green, blue]
