import numpy as np


def get_color_heursitic_weight(rubik):
    count = 0
    for i in range(6):
        for j in range(rubik.n * rubik.n):
            if rubik.cube[i][j] != i:
                count += 1
    return count / (rubik.n * 4)
