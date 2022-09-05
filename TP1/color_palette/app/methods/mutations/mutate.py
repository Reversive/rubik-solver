from data_structure.Member import Member
from functions.fitness import fitness
import random
import numpy as np


def mutate(color: Member, target: Member) -> Member:
    limit = 0.1
    functions = [mutate_single_gene(color, target, limit), mutate_double_gene(color, target, limit),
                 mutate_all_genes(color, target, limit)]
    return np.random.choice(functions, p=[0.6, 0.3, 0.1])


def mutate_gene(color: Member, idx: int, limit: float):
    delta = random.uniform(-limit, limit)
    color.probabilities[idx] = (color.probabilities[idx] + delta) % 1
    return color.probabilities


def mutate_single_gene(color: Member, target: Member, limit: float) -> Member:
    idx = random.randint(0, 2)
    color.probabilities = mutate_gene(color, idx, limit)
    return Member(color.probabilities, fitness(target, color.probabilities))


def mutate_double_gene(color: Member, target: Member, limit: float) -> Member:
    idx = random.sample(range(0, 2), 2)
    color.probabilities = mutate_gene(color, idx[0], limit)
    color.probabilities = mutate_gene(color, idx[1], limit)
    return Member(color.probabilities, fitness(target, color.probabilities))


def mutate_all_genes(color: Member, target: Member, limit: float) -> Member:
    probabilities = [(color.probabilities[0] + random.uniform(-limit, limit)) % 1, (color.probabilities[1] + random.uniform(-limit, limit)) % 1,
           (color.probabilities[2] + random.uniform(-limit, limit)) % 1]
    return Member(probabilities, fitness(target, probabilities))
