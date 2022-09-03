import numpy as np
import random
import json

from data_structure.Solver import Solver


def main(target, available_colors):
    solver = Solver(available_colors, target)


if __name__ == '__main__':
    file = open('../app/arguments/args.json')
    data = json.load(file)
    file.close()
    avail_colors = []
    for i in range(1000):
        avail_colors.append([random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)])
    target_color = np.array([0.1, 0.2, 0.21])
    main(target_color, avail_colors)
