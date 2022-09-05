from data_structure.Member import Member
from functions.fitness import fitness
import random
import numpy as np


def mutate(color: Member, target: Member, colors) -> Member:
    limit = 0.1
    functions = [mutate_single_gene(color, target, limit, colors), mutate_double_gene(color, target, limit, colors),
                 mutate_all_genes(color, target, limit, colors)]
    return np.random.choice(functions, p=[0.6, 0.3, 0.1])


def mutate_gene(color: Member, idx: int, limit: float):
    delta = random.uniform(-limit, limit)
    color.percentage[idx] = (color.percentage[idx] + delta) % 1
    return color.percentage


def mutate_single_gene(color: Member, target: Member, limit: float, colors) -> Member:
    idx = random.randint(0, 2)
    color.percentage = mutate_gene(color, idx, limit)
    return Member(color.percentage, fitness(target, color.percentage, colors))


def mutate_double_gene(color: Member, target: Member, limit: float, colors) -> Member:
    idx = random.sample(range(0, 2), 2)
    color.percentage = mutate_gene(color, idx[0], limit)
    color.percentage = mutate_gene(color, idx[1], limit)
    return Member(color.percentage, fitness(target, color.percentage, colors))


def mutate_all_genes(color: Member, target: Member, limit: float, colors) -> Member:
    percentage = [(color.percentage[0] + random.uniform(-limit, limit)) % 1,
                  (color.percentage[1] + random.uniform(-limit, limit)) % 1,
                  (color.percentage[2] + random.uniform(-limit, limit)) % 1]
    return Member(percentage, fitness(target, percentage, colors))
