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

    # Setting target
    try:
        target = np.array(data['target_color'])
    except KeyError:
        print("No target specified. Please check your json file.")
        return

    pigments_amount = len(target)

    try:
        colors_amount = data['colors_amount']
    except KeyError:
        print("No colors amount specified. Using default.")
        colors_amount = 20

    try:
        population_size = data['population_size']
    except KeyError:
        print("No population size specified. Using default.")
        population_size = 100

    # Creating population
    try:
        curr_population = data['initial_population']
        population_size = len(curr_population)
        colors_amount = len(curr_population[0])
    except KeyError:
        curr_population = np.random.uniform(0.1, 0.3, size=(population_size, colors_amount))

    # Creating colors
    available_colors = np.random.uniform(0, 1, size=(colors_amount, pigments_amount))

    solver = Solver(population=curr_population, colors=available_colors, target=target,
                    max_iterations=data['max_generations'],
                    mutation_probability=data['mutation_prob'], selection_function=data['selection_fun'],
                    selection_func_result_size=data['k'], crossover_function=data['crossover_fun'],
                    mutation_range=data['mutation_range'])


#    plotter.plot_population(solver.palette_list)


if __name__ == '__main__':
    main()
