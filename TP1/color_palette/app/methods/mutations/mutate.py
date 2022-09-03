from data_structure.Color import Color
from functions.fitness import fitness
import random
import numpy as np


def mutate(color: Color, target: Color) -> Color:
    limit = 0.1
    functions = [mutate_single_gene(color, target, limit), mutate_double_gene(color, target, limit),
                 mutate_all_genes(color, target, limit)]
    return np.random.choice(functions, p=[0.6, 0.3, 0.1])


def mutate_gene(color: Color, idx: int, limit: float):
    delta = random.uniform(-limit, limit)
    color.rgb[idx] = (color.rgb[idx] + delta) % 1
    return color.rgb


def mutate_single_gene(color: Color, target: Color, limit: float) -> Color:
    idx = random.randint(0, 2)
    color.rgb = mutate_gene(color, idx, limit)
    return Color(color.rgb, fitness(target, color.rgb))


def mutate_double_gene(color: Color, target: Color, limit: float) -> Color:
    idx = random.sample(range(0, 2), 2)
    color.rgb = mutate_gene(color, idx[0], limit)
    color.rgb = mutate_gene(color, idx[1], limit)
    return Color(color.rgb, fitness(target, color.rgb))


def mutate_all_genes(color: Color, target: Color, limit: float) -> Color:
    rgb = [(color.rgb[0] + random.uniform(-limit, limit)) % 1, (color.rgb[1] + random.uniform(-limit, limit)) % 1,
           (color.rgb[2] + random.uniform(-limit, limit)) % 1]
    return Color(rgb, fitness(target, rgb))
