import random
from data_structure.Color import Color
from functions.fitness import fitness

from methods.selection.elite_selection import elite_selection
from methods.selection.roulette_selection import roulette_selection
from methods.selection.tournament_selection import deterministic_tournament_selection
from methods.selection.tournament_selection import probabilistic_tournament_selection
from methods.crossover.uniform_crossover import uniform_crossover
from methods.crossover.heuristic_crossover import heuristic_crossover
from methods.crossover.geometric_average_crossover import geometric_average_crossover
from methods.crossover import point_crossover

from methods.mutations.mutate import mutate

selection_functions = {'elite': elite_selection, 'roulette': roulette_selection,
                       'prob_tournament': probabilistic_tournament_selection,
                       'det_tournament': deterministic_tournament_selection}
crossover_functions = {'geometric': geometric_average_crossover, 'heuristic': heuristic_crossover,
                       'point': point_crossover, 'uniform': uniform_crossover}


class Solver:

    def __init__(self, palette, target, max_iterations, mutation_probability, selection_function,
                 selection_func_result_size, crossover_function):
        self.palette_size = len(palette)
        self.target_color = target
        self.current_palette = self.generate_palette(palette)
        self.palette_number = 0
        self.max_iterations = max_iterations
        self.mutation_probability = mutation_probability
        self.solved = False
        self.selection_func_result_size = selection_func_result_size

        if selection_functions.__contains__(selection_function):
            self.selection_function = selection_functions[selection_function]
        else:
            print("Invalid selection function specified. Elite selection will be used.")
            self.selection_function = elite_selection

        if crossover_functions.__contains__(crossover_function):
            self.crossover_function = crossover_functions[crossover_function]
        else:
            print("Invalid crossover function specified. Uniform crossover will be used.")
            self.selection_function = uniform_crossover

        while self.palette_number < self.max_iterations and not self.solved:
            self.evolve_palette()

        if not self.solved:
            print("Did you create a new color?")
            raise RuntimeError
        else:
            print(self.palette_number)

    def generate_palette(self, palette) -> list[Color]:
        curr_palette = []
        for i in range(self.palette_size):
            curr_palette.append(Color(palette[i], fitness(self.target_color, palette[i])))
        return curr_palette

    def evolve_palette(self):
        new_gen = []
        while len(new_gen) < self.palette_size:
            sliced = self.selection_function(self.current_palette, self.selection_func_result_size)
            offspring = self.crossover_function(sliced[random.randint(0, len(sliced) - 1)],
                                                sliced[random.randint(0, len(sliced) - 1)],
                                                self.target_color)
            if random.uniform(0, 1) < self.mutation_probability:
                new_gen.append(mutate(offspring[0], self.target_color))
            else:
                new_gen.append(offspring[0])
            if random.uniform(0, 1) < self.mutation_probability:
                new_gen.append(mutate(offspring[1], self.target_color))
            else:
                new_gen.append(offspring[1])

        self.current_palette = new_gen
        self.palette_number += 1

        for color in new_gen:
            print(color.fitness)
            if color.fitness >= 0.99:
                print("found!")
                print(color.rgb)
                self.solved = True
                break
