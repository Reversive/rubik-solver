import sys

import numpy as np
import random
import json

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

    available_colors = []
    for i in range(data['population_size']):
        available_colors.append([random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)])
    target = np.array(data['target_color'])

    solver = Solver(palette=available_colors, target=target, max_iterations=data['max_generations'],
                    mutation_probability=data['mutation_prob'], selection_function=data['selection_fun'],
                    selection_func_result_size=data['k'])


if __name__ == '__main__':
    main()
