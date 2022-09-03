def get_faces_colors_weight(cube, n):
    dif_colors = 0
    for i in range(6):
        colors = [0,0,0,0,0,0]
        for j in range(n * n):
            colors[int(cube[i][j])] = 1
        for color in colors:
            if color != 1:
                dif_colors += 1

    return (dif_colors / 6) - 1
