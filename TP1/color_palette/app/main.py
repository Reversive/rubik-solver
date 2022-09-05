import sys

import numpy as np
import random
import json
# from color_palette.plotter import plotter
from data_structure.Solver import Solver


# usage: $ main.py <args.json>
def main():
    file = open('../app/arguments/args.json')
    if len(sys.argv) < 2:
        print("Using default parameters, set your own by adding a config.json file.")
    else:
        file = open(sys.argv[1])
    data = json.load(file)
    file.close()

    # Creating colors
    available_colors = np.random.uniform(0, 1, size=(data['colors_amount'], data['pigments_amount']))

    # Creating population
    curr_population = np.random.uniform(0, 1, size=(data['population_size'], data['colors_amount']))

    # Setting target
    target = np.array(data['target_color'])

    solver = Solver(population=curr_population, colors=available_colors, target=target,
                    max_iterations=data['max_generations'],
                    mutation_probability=data['mutation_prob'], selection_function=data['selection_fun'],
                    selection_func_result_size=data['k'], crossover_function=data['crossover_fun'],
                    mutation_range=data['mutation_range'])


#    plotter.plot_population(solver.palette_list)


if __name__ == '__main__':
    main()
