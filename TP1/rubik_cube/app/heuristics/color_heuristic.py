def get_color_heursitic_weight(cube, n):
    count = 0
    for i in range(6):
        for j in range(n * n):
            if cube[i][j] != i:
                count += 1

    return count / (n * 4) # n*4 es la maxima cantidad de colores que se pueden corregir en el cubo
