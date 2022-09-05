import random
from data_structure.Member import Member
from functions.fitness import fitness


def geometric_average_crossover(first_parent: Member, second_parent: Member, target: Member, colors) -> list[Member]:
    offspring_rgb = [get_rgb(first_parent, second_parent, lambda gamma, x1, x2: (1 - gamma) * x1 + gamma * x2),
                     get_rgb(first_parent, second_parent, lambda gamma, x1, x2: (1 - gamma) * x2 + gamma * x1)]
    return [Member(offspring_rgb[0], fitness(target, offspring_rgb[0], colors)),
            Member(offspring_rgb[1], fitness(target, offspring_rgb[1], colors))]


def get_rgb(first_parent: Member, second_parent: Member, function):
    gamma = random.uniform(0, 1)
    red = function(gamma, first_parent.percentage[0], second_parent.percentage[0])
    green = function(gamma, first_parent.percentage[1], second_parent.percentage[1])
    blue = function(gamma, first_parent.percentage[2], second_parent.percentage[2])
    return [red, green, blue]
