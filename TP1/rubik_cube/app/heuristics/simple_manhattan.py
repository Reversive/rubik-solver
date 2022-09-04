from enums.faces import Faces

opposite_faces = [Faces.BACK, Faces.BOTTOM, Faces.RIGHT, Faces.TOP, Faces.LEFT, Faces.FRONT]
def get_simple_manhattan_weight(cube, n):
    distance_sum = 0
    for i in range(6):
        for j in range(n * n):
            if cube[i][j] != str(i):
                if Faces(i) == opposite_faces[int(cube[i][j])]:
                    distance_sum += 2
                else:
                    distance_sum += 1
                
    return distance_sum / (4 * (n-1))
