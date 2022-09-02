from arguments.parser import parser
import numpy as np

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
    print(*solver.current_palette, sep='\n')
    print("---------------------")
    sliced = elite_selection(solver.current_palette, 4, solver.palette_size)
    print(*sliced, sep='\n')
    print("---------------------")
    sliced = roulette_selection(solver.current_palette, 4)
    print(*sliced, sep='\n')
    print("---------------------")
    sliced = deterministic_tournament_selection(solver.current_palette, 4, 3)
    print(*sliced, sep='\n')
    print("---------------------")
    sliced = probabilistic_tournament_selection(solver.current_palette, 4)
    print(*sliced, sep='\n')
    print("---------------------")
    offspring = heuristic_crossover(sliced[0], sliced[1], target)
    print(*offspring, sep='\n')
    print("---------------------")
    offspring = geometric_average_crossover(sliced[0], sliced[1], target)
    print(*offspring, sep='\n')
    print("---------------------")
    offspring = uniform_crossover(sliced[0], sliced[1], target)
    print(*offspring, sep='\n')
    print("---------------------")


if __name__ == '__main__':
    args = parser.parse_args()
    avail_colors = np.array([[0.31, 0.02, 0.22], [0.01, 0.42, 0.02], [0.001, 0.92, 0.02], [0.021, 0.02, 0.02]])
    target_color = np.array([0.01, 0.02, 0.021])
    main(target_color, avail_colors)
