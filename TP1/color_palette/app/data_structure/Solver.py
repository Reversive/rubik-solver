import numpy as np
import random
from data_structure.Color import Color
from functions.fitness import fitness

from methods.selection.elite_selection import elite_selection
from methods.crossover.uniform_crossover import uniform_crossover

from methods.selection.roulette_selection import roulette_selection

from methods.crossover.heuristic_crossover import heuristic_crossover

from methods.crossover.geometric_average_crossover import geometric_average_crossover

from methods.mutations.mutate import mutate


class Solver:

    def __init__(self, palette, target, max_iterations, mutation_probability, selection_function,
                 selection_func_result_size):
        self.palette_size = len(palette)
        self.target_color = target
        self.current_palette = self.generate_palette(palette)
        self.palette_number = 0
        self.max_iterations = max_iterations
        self.mutation_probability = mutation_probability
        self.solved = False
        self.selection_function = selection_function
        self.selection_func_result_size = selection_func_result_size
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
            # sliced = elite_selection(self.current_palette, 5, self.palette_size)
            sliced = elite_selection(self.current_palette, self.selection_func_result_size)
            offspring = geometric_average_crossover(sliced[random.randint(0, len(sliced) - 1)],
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
