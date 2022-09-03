from enums.faces import Faces
from enums.moves import MovesN3
from enums.rotations import Rotations
from enums.directions import Directions


class RubikUtils:
    FACES_SPIN_UP = [[Faces.FRONT.value, Faces.BOTTOM.value, Faces.BACK.value, Faces.TOP.value],
                     [Faces.TOP.value, Faces.FRONT.value, Faces.BOTTOM.value, Faces.BACK.value]]
    FACES_SPIN_DOWN = [[Faces.FRONT.value, Faces.TOP.value, Faces.BACK.value, Faces.BOTTOM.value],
                       [Faces.TOP.value, Faces.BACK.value, Faces.BOTTOM.value, Faces.FRONT.value]]

    FACES_SPIN_LEFT = [Faces.FRONT.value, Faces.RIGHT.value, Faces.BACK.value, Faces.LEFT.value]
    FACES_SPIN_RIGHT = [Faces.FRONT.value, Faces.LEFT.value, Faces.BACK.value, Faces.RIGHT.value]

    SIDE_SPIN_UP = [Faces.LEFT.value, Faces.BOTTOM.value, Faces.RIGHT.value, Faces.TOP.value]
    SIDE_SPIN_DOWN = [Faces.LEFT.value, Faces.TOP.value, Faces.RIGHT.value, Faces.BOTTOM.value]

    # En la posicion que denota la cara en X va el valor de la que se encuentra en la cara que esta en X+1
    FACES_SPIN_BY_DIRECTION = [FACES_SPIN_UP, FACES_SPIN_DOWN, FACES_SPIN_LEFT, FACES_SPIN_RIGHT]

    def __init__(self, n):
        self.n = n
        self.solution= [[],[],[],[],[],[]]

        for i in range(6):
            for j in range(self.n * self.n):
                self.solution[i].append(str(i))
        SIDE_LAMBDAS_UP_FUNCTIONS = [
            lambda j, column: (self.n - 1 - j) * self.n + column,  # LEFT
            lambda j, column: self.n * (self.n - column) - j - 1,  # BOTTOM
            lambda j, column: j * self.n + (self.n - 1 - column),  # RIGHT
            lambda j, column: self.n * column + j  # TOP
        ]
        SIDE_LAMBDAS_DOWN_FUNCTIONS = [
            lambda j, column: j * self.n + column,  # LEFT
            lambda j, column: self.n * column + self.n - 1 - j,  # TOP
            lambda j, column: (self.n - 1 - j) * self.n + self.n - 1 - column,  # RIGHT
            lambda j, column: self.n * (self.n - 1 - column) + j  # BOTTOM
        ]  # el orden es acorde a SPIN_SIDE_DOWN

        self.POSITIONS_ROTATE_ORIGIN = []
        aux = []
        for i in range(self.n): #CLOCKWISE
            aux += [[self.n * (self.n - j - 1) + i for j in range(self.n)]]
        self.POSITIONS_ROTATE_ORIGIN += [aux]
        aux = []
        self.POSITIONS_ROTATE_DESTINY = []
        for i in range(self.n): #ANTICLOCKWISE
            aux += [[self.n * (j) + self.n - i - 1 for j in range(self.n)]]
            self.POSITIONS_ROTATE_DESTINY += [[self.n * i + j for j in range(self.n)]]
        self.POSITIONS_ROTATE_ORIGIN += [aux]

        self.POSITIONS_SPIN_COL_BY_COL = []
        for column in range(self.n):
            self.POSITIONS_SPIN_COL_BY_COL += [[j * self.n + column for j in range(self.n)]]

        self.POSITIONS_SPIN_ROW_BY_ROW = []
        for row in range(self.n):
            self.POSITIONS_SPIN_ROW_BY_ROW += [[self.n * row + j for j in range(self.n)]]

        self.POSITIONS_SPIN_SIDE_UP_BY_FACE_BY_COL = []
        self.POSITIONS_SPIN_SIDE_DOWN_BY_FACE_BY_COL = []
        for face in range(4):
            self.POSITIONS_SPIN_SIDE_UP_BY_FACE_BY_COL += [[]]
            self.POSITIONS_SPIN_SIDE_DOWN_BY_FACE_BY_COL += [[]]
            for column in range(self.n):
                self.POSITIONS_SPIN_SIDE_UP_BY_FACE_BY_COL[face] += [[SIDE_LAMBDAS_UP_FUNCTIONS[face](j, column) for j in range(self.n)]]
                self.POSITIONS_SPIN_SIDE_DOWN_BY_FACE_BY_COL[face] += [[SIDE_LAMBDAS_DOWN_FUNCTIONS[face](j, column) for j in range(self.n)]]


        self.moveCubeFunctions = {
            MovesN3.LEFT_UP.value: lambda endCube, self: self.move_col(endCube, 0, Directions.UP, Faces.LEFT,
                                                         Rotations.ANTICLOCKWISE),
            MovesN3.LEFT_DOWN.value: lambda endCube, self: self.move_col(endCube, 0, Directions.DOWN, Faces.LEFT,
                                                           Rotations.CLOCKWISE),
            MovesN3.RIGHT_UP.value: lambda endCube, self: self.move_col(endCube, self.n - 1, Directions.UP, Faces.RIGHT,
                                                          Rotations.CLOCKWISE),
            MovesN3.RIGHT_DOWN.value: lambda endCube, self: self.move_col(endCube, self.n - 1, Directions.DOWN, Faces.RIGHT,
                                                            Rotations.ANTICLOCKWISE),
            MovesN3.TOP_LEFT.value: lambda endCube, self: self.move_row(endCube, 0, Directions.LEFT, Rotations.CLOCKWISE),
            MovesN3.TOP_RIGHT.value: lambda endCube, self: self.move_row(endCube, 0, Directions.RIGHT, Rotations.ANTICLOCKWISE),
            MovesN3.BOTTOM_LEFT.value: lambda endCube, self: self.move_row(endCube, self.n - 1, Directions.LEFT, Rotations.CLOCKWISE),
            MovesN3.BOTTOM_RIGHT.value: lambda endCube, self: self.move_row(endCube, self.n - 1, Directions.RIGHT,
                                                              Rotations.ANTICLOCKWISE),
            MovesN3.FRONT_ROTATE_CLOCKWISE.value: lambda endCube, self: self.move_rotate(endCube, Faces.FRONT, Rotations.CLOCKWISE,
                                                                           self.n - 1,
                                                                           Directions.UP),
            MovesN3.FRONT_ROTATE_ANTICLOCKWISE.value: lambda endCube, self: self.move_rotate(endCube, Faces.FRONT,
                                                                               Rotations.ANTICLOCKWISE,
                                                                               self.n - 1, Directions.DOWN),
            MovesN3.BACK_ROTATE_CLOCKWISE.value: lambda endCube, self: self.move_rotate(endCube, Faces.BACK, Rotations.CLOCKWISE, 0,
                                                                          Directions.DOWN),
            MovesN3.BACK_ROTATE_ANTICLOCKWISE.value: lambda endCube, self: self.move_rotate(endCube, Faces.BACK,
                                                                              Rotations.ANTICLOCKWISE, 0,
                                                                              Directions.UP)
        }

    
    def is_solved(self, cube):
        return self.solution == cube