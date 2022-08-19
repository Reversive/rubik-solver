from enums.directions import Directions
from enums.faces import Faces
from enums.moves import Moves
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

    # En la posicion que denota la cara en X va el valor de la que se encuentra en la cara que esta en X+1

    def __init__(self, n=2, state=None):
        # frente, arriba, izquierda, abajo, derecha, atras
        self.n = n
        self.cube = np.empty((6, self.n * self.n), dtype=int)
        if state is not None:
            self.cube = np.array(state, copy=True)
        else:
            for i in range(6):
                for j in range(self.n * self.n):
                    self.cube[i][j] = i

    def rotate(self, endCube, face, direction):
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
                endCube[face.value][self.n * i + j] = self.cube[face.value][pos(i, j)]

        return endCube

    def spin(self, endCube, faces, posLambda):
        for i in range(len(faces)):
            for j in range(self.n):
                endCube[faces[i]][posLambda(j)] = self.cube[faces[(i + 1) % len(faces)]][posLambda(j)]

        return endCube

    def spin_col(self, cube, face, column, direction):
        if face == 2 or face == 4:
            raise ValueError('Invalid face, for sides use spin_side')

        if (direction == Directions.DOWN):
            faces = self.SPIN_FACES_DOWN[face.value % 3]
        elif (direction == Directions.UP):
            faces = self.SPIN_FACES_UP[face.value % 3]
        else:
            raise ValueError('Invalid direction spinning column')

        return self.spin(cube, faces, lambda j: j * self.n + column)

    def spin_row(self, cube, face, row, direction):
        if (face == 2 or face == 4):
            raise ValueError('Invalid face, for sides use spin_side')

        if (direction == Directions.LEFT):
            faces = self.SPIN_FACES_LEFT
        elif (direction == Directions.RIGHT):
            faces = self.SPIN_FACES_RIGHT
        else:
            raise ValueError('Invalid direction spinning row')

        return self.spin(cube, faces, lambda j: self.n * row + j)

    def spin_side(self, endCube, column, direction):
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
        if (direction == Directions.DOWN):
            faces = self.SPIN_SIDE_DOWN
            lambdas = SIDE_LAMBDAS_DOWN
        elif (direction == Directions.UP):
            faces = self.SPIN_SIDE_UP
            lambdas = SIDE_LAMBDAS_UP
        else:
            raise ValueError('Invalid direction spinning side')

        for i in range(len(faces)):
            for j in range(self.n):
                endCube[faces[i]][lambdas[i](j)] = self.cube[faces[(i + 1) % len(faces)]][
                    lambdas[(i + 1) % len(faces)](j)]

        return endCube

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

    def move_row(self, cube, row, direction, rotation):
        cube = self.spin_row(cube, Faces.FRONT, row, direction)
        cube = self.rotate(cube, Faces.BOTTOM, rotation)
        return cube

    def move_col(self, cube, column, direction, sideFace, rotation):
        cube = self.spin_col(cube, Faces.FRONT, column, direction)
        cube = self.rotate(cube, sideFace, rotation)
        return cube

    def move_rotate(self, cube, face, rotation, column, spinDir):
        cube = self.rotate(cube, face, rotation)
        cube = self.spin_side(cube, column, spinDir)
        return cube
    
    def move(self, move):
        endCube = np.array(self.cube, copy=True)
        endCube = {
            Moves.LEFT_UP: lambda: self.move_col(endCube, 0, Directions.UP, Faces.LEFT, Rotations.ANTICLOCKWISE),
            Moves.LEFT_DOWN: lambda: self.move_col(endCube, 0, Directions.DOWN, Faces.LEFT, Rotations.CLOCKWISE),
            Moves.RIGHT_UP: lambda: self.move_col(endCube, self.n - 1, Directions.UP, Faces.RIGHT, Rotations.CLOCKWISE),
            Moves.RIGHT_DOWN: lambda: self.move_col(endCube, self.n - 1, Directions.DOWN, Faces.RIGHT, Rotations.ANTICLOCKWISE),
            Moves.TOP_LEFT: lambda: self.move_row(endCube, 0, Directions.LEFT, Rotations.CLOCKWISE),
            Moves.TOP_RIGHT: lambda: self.move_row(endCube, 0, Directions.RIGHT, Rotations.ANTICLOCKWISE),
            Moves.BOTTOM_LEFT: lambda: self.move_row(endCube, self.n - 1, Directions.LEFT, Rotations.CLOCKWISE),
            Moves.BOTTOM_RIGHT: lambda: self.move_row(endCube, self.n - 1, Directions.RIGHT, Rotations.ANTICLOCKWISE),
            Moves.FRONT_ROTATE_CLOCKWISE: lambda: self.move_rotate(endCube, Faces.FRONT, Rotations.CLOCKWISE, self.n - 1,
                                                           Directions.UP),
            Moves.FRONT_ROTATE_ANTICLOCKWISE: lambda: self.move_rotate(endCube, Faces.FRONT, Rotations.ANTICLOCKWISE,
                                                               self.n - 1, Directions.DOWN),
            Moves.BACK_ROTATE_CLOCKWISE: lambda: self.move_rotate(endCube, Faces.BACK, Rotations.CLOCKWISE, 0, Directions.DOWN),
            Moves.BACK_ROTATE_ANTICLOCKWISE: lambda: self.move_rotate(endCube, Faces.BACK, Rotations.ANTICLOCKWISE, 0,
                                                              Directions.UP)
        }.get(move, 'Invalid move')()

        return endCube
