from enums.faces import Faces
from enums.directions import Directions
from enums.rotations import Rotations


class Rubik:
    def __init__(self, n=2):
        # frente, arriba, izquierda, abajo, derecha, atras
        self.cube = [[], [], [], [], [], []]
        self.n = n

        for i in range(6):
            for j in range(n * n):
                self.cube[i].append(i)

    def rotate(self, face, direction):
        destination = []

        if direction == Rotations.CLOCKWISE:
            pos = lambda i,j: self.n*(j) + self.n - i - 1
                # clockwise: (i, j) -> (j, n-i-1)
        elif direction == Rotations.ANTICLOCKWISE:
            pos = lambda i,j: self.n*(self.n - j - 1) + i
                # anticlockwise: (i, j) -> (n-j-1, i)
        else:            
            raise ValueError('Invalid direction')

        for i in range(self.n):
            for j in range(self.n): 
                destination.insert(self.n*i + j, self.cube[face.value][pos])
        
        self.cube[face.value] = destination.copy()

    def spinCol(self, face, column, direction):
        SPIN_FACES_UP = [[Faces.FRONT.value, Faces.BOTTOM.value, Faces.BACK.value, Faces.TOP.value],
                         [Faces.TOP.value, Faces.FRONT.value, Faces.BOTTOM.value, Faces.BACK.value],
                         [Faces.LEFT.value, Faces.BOTTOM.value, Faces.RIGHT.value, Faces.TOP.value]]
        SPIN_FACES_DOWN = [[Faces.FRONT.value, Faces.TOP.value, Faces.BACK.value, Faces.BOTTOM.value],
                           [Faces.TOP.value, Faces.BACK.value, Faces.BOTTOM.value, Faces.FRONT.value],
                           [Faces.LEFT.value, Faces.TOP.value, Faces.RIGHT.value, Faces.BOTTOM.value]]
        #       En la posicion que denota la cara en X va el valor de la que se encuentra en la cara que esta en X+1

        if (direction == Directions.DOWN):
            faces = SPIN_FACES_DOWN[face.value % 3]
        else:
            faces = SPIN_FACES_UP[face.value % 3]

        aux_face = self.cube[faces[Faces.FRONT.value]].copy()
        for i in range(len(faces) - 1):
            for j in range(self.n):
                self.cube[faces[i]][j * self.n + column] = self.cube[faces[i + 1]][j * self.n + column]

        for j in range(self.n):
            self.cube[faces[-1]][j * self.n + column] = aux_face[j * self.n + column]

    def spinRow(self, face, row, direction):
        # En realidad solo existen dos ejes de rotacion, asi que deberia salir con 2 pero me ta costando pensar...
        # Piensen que aca no es que son los 0 1 2 como antes y puedo hacer modulo,
        # va no lo pude pensar como modulo si les sale joya

        SPIN_FACES_LEFT = [[Faces.FRONT.value, Faces.LEFT.value, Faces.BACK.value, Faces.RIGHT.value],
                           [Faces.TOP.value, Faces.LEFT.value, Faces.BOTTOM.value, Faces.RIGHT.value]]
        SPIN_FACES_RIGHT = [[Faces.FRONT.value, Faces.RIGHT.value, Faces.BACK.value, Faces.LEFT.value],
                            [Faces.TOP.value, Faces.RIGHT.value, Faces.BOTTOM.value, Faces.LEFT.value]]

        if face.value == 0 or face.value == 2 or face.value == 4 or face.value == 5:
            reduced_face = 0
        else:
            reduced_face = 1
        if direction == Directions.ROTATE_LEFT:
            faces = SPIN_FACES_LEFT[reduced_face]
        else:
            faces = SPIN_FACES_RIGHT[reduced_face]

        #aca no entiendo pq va FRONT pero bueno, funciona y eso que nunca piso front
        aux_face = self.cube[faces[Faces.FRONT.value]].copy()
        for i in range(len(faces) - 1):
            for j in range(self.n):
                self.cube[faces[i]][self.n * row + j] = self.cube[faces[i + 1]][self.n * row + j]
        for j in range(self.n):
            self.cube[faces[-1]][self.n * row + j] = aux_face[self.n * row + j]

    def move(self, direction):
        if direction == Directions.TOP_LEFT:
            self.spinRow(Faces.TOP, 0, Directions.ROTATE_LEFT)
        elif direction == Directions.TOP_RIGHT:
            self.spinRow(Faces.TOP, 0, Directions.ROTATE_RIGHT)
        elif direction == Directions.LEFT_UP:
            self.spinCol(Faces.FRONT, 0, Directions.UP)
            self.rotate(Faces.LEFT, Rotations.ANTICLOCKWISE)
        elif direction == Directions.LEFT_DOWN:
            self.spinCol(Faces.FRONT, 0, Directions.DOWN)
            self.rotate(Faces.LEFT, Rotations.CLOCKWISE)
        elif direction == Directions.RIGHT_UP:
            self.spinCol(Faces.FRONT, self.n - 1, Directions.UP)
            self.rotate(Faces.RIGHT, Rotations.CLOCKWISE)
        elif direction == Directions.RIGHT_DOWN:
            self.spinCol(Faces.FRONT, self.n - 1, Directions.DOWN)
            self.rotate(Faces.RIGHT, Rotations.ANTICLOCKWISE)
        elif direction == Directions.BOTTOM_LEFT:
            self.spinBottom(-1)
        elif direction == Directions.BOTTOM_RIGHT:
            self.spinBottom(1)
        elif direction == Directions.ROTATE_LEFT:
            self.rotate(Faces.FRONT, Rotations.ANTICLOCKWISE)
            self.spinCol(Faces.LEFT, self.n - 1, Directions.DOWN)
        elif direction == Directions.ROTATE_RIGHT:
            self.rotate(Faces.FRONT, Rotations.CLOCKWISE)
            self.spinCol(Faces.LEFT, self.n - 1, Directions.UP)
        else:
            print('Invalid direction')
        
