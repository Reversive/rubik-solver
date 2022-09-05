from data_structure.Member import Member
import numpy as np


def roulette_selection(palette: list[Member], result_size: int) -> list[Member]:
    total_fit = sum(color.fitness for color in palette)
    # accumulated_fit = [palette[0].fitness / total_fit]
    # for i in range(1, len(palette)):
    #     accumulated_fit.append(accumulated_fit[i-1] + palette[i].fitness/total_fit)
    # norm = [fit/total_fit for fit in accumulated_fit]
    # return [np.random.choice(palette, p=accumulated_fit) for i in range(result_size)]
    relative_fit = []
    for i in range(len(palette)):
        relative_fit.append(palette[i].fitness / total_fit)
    return np.random.choice(palette, p=relative_fit, size=result_size, replace=True)




