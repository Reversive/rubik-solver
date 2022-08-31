import numpy as np
from data_structure.Color import Color
from functions.fitness import fitness


class Solver:

    def __init__(self, palette, target):
        self.palette_size = len(palette)
        self.target_color = target
        self.current_palette = self.generate_palette(palette)

    def generate_palette(self, palette) -> list[Color]:
        curr_palette = []
        for i in range(self.palette_size):
            curr_palette.append(Color(palette[i], fitness(self.target_color, palette[i])))
        return curr_palette

