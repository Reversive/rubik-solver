import random
from data_structure.Member import Member
from functions.fitness import fitness

from methods.selection.elite_selection import elite_selection
from methods.selection.roulette_selection import roulette_selection
from methods.selection.tournament_selection import deterministic_tournament_selection
from methods.selection.tournament_selection import probabilistic_tournament_selection
from methods.crossover.uniform_crossover import uniform_crossover
from methods.crossover.heuristic_crossover import heuristic_crossover
from methods.crossover.geometric_average_crossover import geometric_average_crossover
from methods.crossover.point_crossover import point_crossover

from methods.mutations.mutate import mutate

selection_functions = {'elite': elite_selection, 'roulette': roulette_selection,
                       'prob_tournament': probabilistic_tournament_selection,
                       'det_tournament': deterministic_tournament_selection}
crossover_functions = {'geometric': geometric_average_crossover, 'heuristic': heuristic_crossover,
                       'point': point_crossover, 'uniform': uniform_crossover}


class Solver:

    def __init__(self, population, target, max_iterations, mutation_probability, selection_function,
                 selection_func_result_size, crossover_function, colors):
        self.population_size = len(population)
        self.colors = colors
        self.target_color = target
        self.current_population = self.generate_population(population, colors)
        self.population_number = 0
        self.max_iterations = max_iterations
        self.mutation_probability = mutation_probability
        self.solved = False
        self.selection_func_result_size = selection_func_result_size
        self.palette_list = []
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

        while self.population_number < self.max_iterations and not self.solved:
            self.palette_list.append(self.current_population)
            self.evolve_population()

        self.palette_list.append(self.current_population)

        if not self.solved:
            print("Did you create a new color?")
            raise RuntimeError
        else:
            print(self.population_number)

    def generate_population(self, population, colors) -> list[Member]:
        curr_population = []
        for i in range(self.population_size):
            curr_population.append(Member(population[i], fitness(self.target_color, population[i])))
        return curr_population

    def evolve_population(self):
        new_gen = []
        while len(new_gen) < self.population_size:
            sliced = self.selection_function(self.current_population, self.selection_func_result_size)
            offspring = self.crossover_function(sliced[random.randint(0, len(sliced) - 1)],
                                                sliced[random.randint(0, len(sliced) - 1)],
                                                self.target_color)
            if random.uniform(0, 1) < self.mutation_probability:
                new_gen.append(mutate(offspring[0], self.target_color))
            else:
                new_gen.append(offspring[0])
            if self.crossover_function != heuristic_crossover:  # since heuristic crossover gives only one child
                if random.uniform(0, 1) < self.mutation_probability:
                    new_gen.append(mutate(offspring[1], self.target_color))
                else:
                    new_gen.append(offspring[1])

        self.current_population = new_gen
        self.population_number += 1

        for color in new_gen:
            if color.fitness >= 0.99:
                print("found!")
                print(color.probabilities)
                self.solved = True
                break
