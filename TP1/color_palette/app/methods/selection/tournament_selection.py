import random
import numpy as np
from data_structure.Member import Member


def deterministic_tournament_selection(palette: list[Member], result_size: int) -> list[Member]:
    selected = []
    groups_size = 5
    while len(selected) < result_size:
        selected.append(max(np.random.choice(palette, size=groups_size), key=lambda color: color.fitness))
    return selected


def probabilistic_tournament_selection(palette: list[Member], result_size: int) -> list[Member]:
    threshold = random.uniform(0.5, 1)
    selected = []
    while len(selected) < result_size:
        r = random.uniform(0, 1)
        pair = np.random.choice(palette, 2)
        if r < threshold:
            selected.append(max(pair, key=lambda color: color.fitness))
        else:
            selected.append(min(pair, key=lambda color: color.fitness))
    return selected
