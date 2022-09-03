from enums.directions import Directions
from enums.faces import Faces


class Rubik:
    def __init__(self, n, rubikUtils, state=None):
        # frente, arriba, izquierda, abajo, derecha, atras
        self.n = n
        self.rubikUtils = rubikUtils
        if state is not None:
            self.cube = state
        else:
            self.cube = [[],[],[],[],[],[]]
            for i in range(6):
                for j in range(self.n * self.n):
                    self.cube[i].append(str(i))


    def rotate(self, endCube, face, direction):
        # if direction == Rotations.CLOCKWISE:
        #     pos = lambda i, j: self.n * (self.n - j - 1) + i
        #     # clockwise: (i, j) -> (n-j-1, i)
        # elif direction == Rotations.ANTICLOCKWISE:
        #     pos = lambda i, j: self.n * (j) + self.n - i - 1
        #     # anticlockwise: (i, j) -> (j, n-i-1)
        # else:
        #     raise ValueError('Invalid direction rotating')

        for i in range(self.n):
            for j in range(self.n):
                endCube[face.value][self.rubikUtils.POSITIONS_ROTATE_DESTINY[i][j]] = \
                    self.cube[face.value][self.rubikUtils.POSITIONS_ROTATE_ORIGIN[direction.value][i][j]]

        return endCube

    def spin(self, endCube, faces, positions):
        for i in range(len(faces) - 1):
            for j in range(self.n):
                endCube[faces[i]][positions[j]] = self.cube[faces[i + 1]][positions[j]]

        for j in range(self.n):
            endCube[faces[-1]][positions[j]] = self.cube[faces[0]][positions[j]]
        return endCube

    def spin_side(self, endCube, column, direction):
        if (direction == Directions.DOWN):
            faces = self.rubikUtils.SIDE_SPIN_DOWN
            positions = self.rubikUtils.POSITIONS_SPIN_SIDE_DOWN_BY_FACE_BY_COL
        elif (direction == Directions.UP):
            faces = self.rubikUtils.SIDE_SPIN_UP
            positions = self.rubikUtils.POSITIONS_SPIN_SIDE_UP_BY_FACE_BY_COL
        else:
            raise ValueError('Invalid direction spinning side')

        for i in range(len(faces) - 1):
            for j in range(self.n):
                endCube[faces[i]][positions[i][column][j]] = self.cube[faces[(i + 1)]][
                    positions[(i + 1)][column][j]]

        for j in range(self.n):
            endCube[faces[-1]][positions[-1][column][j]] = self.cube[faces[0]][
                positions[0][column][j]]

        return endCube

    def spin_col(self, cube, face, column, direction):
        # COMENTADO POR EFICIENCIA
        # if face == Faces.LEFT.value or face == Faces.RIGHT.value:
        #     raise ValueError('Invalid face, for sides use spin_side')
        return self.spin(cube,
                         self.rubikUtils.FACES_SPIN_BY_DIRECTION[direction.value][face.value % 3],
                         self.rubikUtils.POSITIONS_SPIN_COL_BY_COL[column])

    def spin_row(self, cube, face, row, direction):
        # COMENTADO POR EFICIENCIA
        # if face == Faces.LEFT.value or face == Faces.RIGHT.value:
        # raise ValueError('Invalid face, for sides use spin_side')

        return self.spin(cube,
                         self.rubikUtils.FACES_SPIN_BY_DIRECTION[direction.value],
                         self.rubikUtils.POSITIONS_SPIN_ROW_BY_ROW[row])

    def to_string(self):
        return ''.join([
            ''.join(self.cube[0]),
            ''.join(self.cube[1]),
            ''.join(self.cube[2]),
            ''.join(self.cube[3]),
            ''.join(self.cube[4]),
            ''.join(self.cube[5])])

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
        endCube = list(map(list, self.cube))
        moveFunc = self.rubikUtils.moveCubeFunctions.get(move, 'Invalid move')
        return moveFunc(endCube, self)
