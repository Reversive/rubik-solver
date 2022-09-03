from arguments.parser import parser
import numpy as np
import random

from methods.crossover.uniform_crossover import uniform_crossover
from methods.crossover.geometric_average_crossover import geometric_average_crossover
from methods.crossover.heuristic_crossover import heuristic_crossover
from methods.selection.tournament_selection import deterministic_tournament_selection
from methods.selection.tournament_selection import probabilistic_tournament_selection
from methods.selection.elite_selection import elite_selection
from methods.selection.roulette_selection import roulette_selection
from data_structure.Solver import Solver


def main(target, available_colors):
    solver = Solver(available_colors, target)


if __name__ == '__main__':
    args = parser.parse_args()
    avail_colors = []
    for i in range(500):
        avail_colors.append([random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)])
    target_color = np.array([0.1, 0.2, 0.21])
    main(target_color, avail_colors)
