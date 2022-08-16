from enums.faces import Faces
from enums.directions import Directions
from enums.rotations import Rotations
import numpy as np


class Rubik:
    SPIN_FACES_LEFT = [Faces.FRONT.value, Faces.RIGHT.value, Faces.BACK.value, Faces.LEFT.value]
    SPIN_FACES_RIGHT = [Faces.FRONT.value, Faces.LEFT.value, Faces.BACK.value, Faces.RIGHT.value]

    SPIN_SIDE_UP = [Faces.LEFT.value, Faces.BOTTOM.value, Faces.RIGHT.value, Faces.TOP.value]
    SPIN_SIDE_DOWN = [Faces.LEFT.value, Faces.TOP.value, Faces.RIGHT.value, Faces.BOTTOM.value]

    SPIN_FACES_UP = [[Faces.FRONT.value, Faces.BOTTOM.value, Faces.BACK.value, Faces.TOP.value],
                     [Faces.TOP.value, Faces.FRONT.value, Faces.BOTTOM.value, Faces.BACK.value]]
    SPIN_FACES_DOWN = [[Faces.FRONT.value, Faces.TOP.value, Faces.BACK.value, Faces.BOTTOM.value],
                       [Faces.TOP.value, Faces.BACK.value, Faces.BOTTOM.value, Faces.FRONT.value]]

    def __init__(self, n=2):
        # frente, arriba, izquierda, abajo, derecha, atras
        self.cube = np.empty((6, n * n), dtype=int)
        self.n = n

        for i in range(6):
            for j in range(n * n):
                self.cube[i][j] = i

    def rotate(self, face, direction):
        destination = np.empty(shape=(self.n * self.n))
        if direction == Rotations.CLOCKWISE:
            pos = lambda i, j: self.n * (self.n - j - 1) + i
            # clockwise: (i, j) -> (n-j-1, i)
        elif direction == Rotations.ANTICLOCKWISE:
            pos = lambda i, j: self.n * (j) + self.n - i - 1
            # anticlockwise: (i, j) -> (j, n-i-1)
        else:
            raise ValueError('Invalid direction rotating')

        for i in range(self.n):
            for j in range(self.n):
                destination[self.n * i + j] = self.cube[face.value][pos(i, j)]

        self.cube[face.value] = np.copy(destination)

    def spin(self, faces, posLambda):
        aux_face = np.copy(self.cube[faces[0]])
        for i in range(len(faces) - 1):
            for j in range(self.n):
                self.cube[faces[i]][posLambda(j)] = self.cube[faces[i + 1]][posLambda(j)]

        for j in range(self.n):
            self.cube[faces[-1]][posLambda(j)] = aux_face[posLambda(j)]

    def spin_col(self, face, column, direction):
        if face == 2 or face == 4:
            raise ValueError('Invalid face, for sides use spin_side')

        #       En la posicion que denota la cara en X va el valor de la que se encuentra en la cara que esta en X+1

        if (direction == Rotations.DOWN):
            faces = self.SPIN_FACES_DOWN[face.value % 3]
        elif (direction == Rotations.UP):
            faces = self.SPIN_FACES_UP[face.value % 3]
        else:
            raise ValueError('Invalid direction spinning column')
        self.spin(faces, lambda j: j * self.n + column)

    def spin_row(self, face, row, direction):
        if (face == 2 or face == 4):
            raise ValueError('Invalid face, for sides use spin_side')

        if (direction == Rotations.LEFT):
            faces = self.SPIN_FACES_LEFT
        elif (direction == Rotations.RIGHT):
            faces = self.SPIN_FACES_RIGHT
        else:
            raise ValueError('Invalid direction spinning row')

        self.spin(faces, lambda j: self.n * row + j)

    def spin_side(self, face, column, direction):

        SIDE_LAMBDAS_UP = [
            lambda j: (self.n - 1 - j) * self.n + column,  # LEFT
            lambda j: self.n * (self.n - column) - j - 1,  # BOTTOM
            lambda j: j * self.n + (self.n - 1 - column),  # RIGHT
            lambda j: self.n * column + j  # TOP
        ]
        SIDE_LAMBDAS_DOWN = [
            lambda j: j * self.n + column,  # LEFT
            lambda j: self.n * column + self.n - 1 - j,  # TOP
            lambda j: (self.n - 1 - j) * self.n + self.n - 1 - column,  # RIGHT
            lambda j: self.n * (self.n - 1 - column) + j  # BOTTOM
        ]
        if (direction == Rotations.DOWN):
            faces = self.SPIN_SIDE_DOWN
            lambdas = SIDE_LAMBDAS_DOWN
        elif (direction == Rotations.UP):
            faces = self.SPIN_SIDE_UP
            lambdas = SIDE_LAMBDAS_UP
        else:
            raise ValueError('Invalid direction spinning side')

        aux_face = np.copy(self.cube[faces[0]])
        for i in range(len(faces) - 1):
            for j in range(self.n):
                self.cube[faces[i]][lambdas[i](j)] = self.cube[faces[i + 1]][lambdas[i + 1](j)]

        for j in range(self.n):
            self.cube[faces[3]][lambdas[3](j)] = aux_face[lambdas[0](j)]

    def is_solved(self):
        for i in range(6):
            for j in range(self.n * self.n):
                if self.cube[i][j] != i:
                    return False

        return True

    def to_string(self):
        answer = ''
        for i in range(6):
            for j in range(self.n * self.n):
                answer += str(self.cube[i][j])

        return answer

    def move(self, direction):
        if direction == Directions.TOP_LEFT:
            self.spin_row(Faces.FRONT, 0, Rotations.LEFT)
            self.rotate(Faces.BOTTOM, Rotations.CLOCKWISE)
        elif direction == Directions.TOP_RIGHT:
            self.spin_row(Faces.FRONT, 0, Rotations.RIGHT)
            self.rotate(Faces.BOTTOM, Rotations.ANTICLOCKWISE)
        elif direction == Directions.LEFT_UP:
            self.spin_col(Faces.FRONT, 0, Rotations.UP)
            self.rotate(Faces.LEFT, Rotations.ANTICLOCKWISE)
        elif direction == Directions.LEFT_DOWN:
            self.spin_col(Faces.FRONT, 0, Rotations.DOWN)
            self.rotate(Faces.LEFT, Rotations.CLOCKWISE)
        elif direction == Directions.RIGHT_UP:
            self.spin_col(Faces.FRONT, self.n - 1, Rotations.UP)
            self.rotate(Faces.RIGHT, Rotations.CLOCKWISE)
        elif direction == Directions.RIGHT_DOWN:
            self.spin_col(Faces.FRONT, self.n - 1, Rotations.DOWN)
            self.rotate(Faces.RIGHT, Rotations.ANTICLOCKWISE)
        elif direction == Directions.BOTTOM_LEFT:
            self.spin_row(Faces.FRONT, self.n - 1, Rotations.LEFT)
            self.rotate(Faces.BOTTOM, Rotations.ANTICLOCKWISE)
        elif direction == Directions.BOTTOM_RIGHT:
            self.spin_row(Faces.FRONT, self.n - 1, Rotations.RIGHT)
            self.rotate(Faces.BOTTOM, Rotations.CLOCKWISE)
        elif direction == Directions.FRONT_ROTATE_ANTICLOCKWISE:
            self.rotate(Faces.FRONT, Rotations.ANTICLOCKWISE)
            self.spin_side(Faces.LEFT, self.n - 1, Rotations.DOWN)
        elif direction == Directions.FRONT_ROTATE_CLOCKWISE:
            self.rotate(Faces.FRONT, Rotations.CLOCKWISE)
            self.spin_side(Faces.LEFT, self.n - 1, Rotations.UP)
        elif direction == Directions.BACK_ROTATE_ANTICLOCKWISE:
            self.rotate(Faces.BACK, Rotations.ANTICLOCKWISE)
            self.spin_side(Faces.LEFT, 0, Rotations.UP)
        elif direction == Directions.BACK_ROTATE_CLOCKWISE:
            self.rotate(Faces.BACK, Rotations.CLOCKWISE)
            self.spin_side(Faces.LEFT, 0, Rotations.DOWN)
        else:
            print('Invalid direction on move')
