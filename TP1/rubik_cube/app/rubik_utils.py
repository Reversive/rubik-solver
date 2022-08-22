from enums.faces import Faces


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

