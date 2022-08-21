import numpy as np


def faces_colors(rubik):
    dif_colors = 0
    faces = 6
    for i in range(faces):
        colors = np.empty(6)
        for j in range(rubik.n * rubik.n):
            colors[rubik.cube[i][j]] = 1
        for color in colors:
            if color != 1:
                dif_colors += 1
    return (dif_colors/faces) - 1
