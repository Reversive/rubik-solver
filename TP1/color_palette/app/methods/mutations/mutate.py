from data_structure.Color import Color
from functions.fitness import fitness
import random
import numpy as np


def mutate(color: Color, target: Color) -> Color:
    functions = [mutate_single_gene(color, target), mutate_double_gene(color, target), mutate_all_genes(color, target)]
    return np.random.choice(functions, p=[0.6, 0.3, 0.1])


def mutate_gene(color: Color, idx: int):
    delta = random.uniform(-0.1, 0.1)
    color.rgb[idx] = abs(color.rgb[idx] + delta)
    return color.rgb


def mutate_single_gene(color: Color, target: Color) -> Color:
    idx = random.randint(0, 2)
    color.rgb = mutate_gene(color, idx)
    return Color(color.rgb, fitness(target, color.rgb))


def mutate_double_gene(color: Color, target: Color) -> Color:
    idx = random.sample(range(0, 2), 2)
    color.rgb = mutate_gene(color, idx[0])
    color.rgb = mutate_gene(color, idx[1])
    return Color(color.rgb, fitness(target, color.rgb))


def mutate_all_genes(color: Color, target: Color) -> Color:
    limit = 0.1
    rgb = [abs(color.rgb[0] + random.uniform(-limit, limit)), abs(color.rgb[1] + random.uniform(-limit, limit)),
           abs(color.rgb[2] + random.uniform(-limit, limit))]
    return Color(rgb, fitness(target, rgb))
