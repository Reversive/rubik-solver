import numpy as np
import random
from data_structure.Color import Color
from functions.fitness import fitness

from methods.selection.elite_selection import elite_selection
from methods.crossover.uniform_crossover import uniform_crossover

from methods.selection.roulette_selection import roulette_selection

from methods.crossover.heuristic_crossover import heuristic_crossover

from methods.crossover.geometric_average_crossover import geometric_average_crossover


class Solver:

    def __init__(self, palette, target):
        self.palette_size = len(palette)
        self.target_color = target
        self.current_palette = self.generate_palette(palette)
        self.palette_number = 0
        while True:
            self.evolve_palette()

    def generate_palette(self, palette) -> list[Color]:
        curr_palette = []
        for i in range(self.palette_size):
            curr_palette.append(Color(palette[i], fitness(self.target_color, palette[i])))
        return curr_palette

    def evolve_palette(self):
        if self.palette_number > 100000:
            raise RuntimeError
        new_gen = []
        while len(new_gen) < self.palette_size:
            sliced = elite_selection(self.current_palette, 5, self.palette_size)
            # sliced = roulette_selection(self.current_palette, int(self.palette_size/2))
            offspring = geometric_average_crossover(sliced[random.randint(0, len(sliced) - 1)],
                                                    sliced[random.randint(0, len(sliced) - 1)],
                                                    self.target_color)
            new_gen.append(offspring[0])
            new_gen.append(offspring[1])
        self.current_palette = new_gen
        self.palette_number += 1
        for color in new_gen:
            print(color.fitness)
            if color.fitness >= 0.98:
                print("found!")
                print(color.rgb)
                exit(1)
