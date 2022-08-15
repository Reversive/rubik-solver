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
                self.cube[i].append(self.n*self.n*i + j)

    def rotate(self, face, direction):
        destination = []

        if direction == Rotations.CLOCKWISE:
            pos = lambda i,j: self.n*(self.n - j - 1) + i
                # clockwise: (i, j) -> (n-j-1, i)
        elif direction == Rotations.ANTICLOCKWISE:
            pos = lambda i,j: self.n*(j) + self.n - i - 1
                # anticlockwise: (i, j) -> (j, n-i-1)
        else:            
            raise ValueError('Invalid direction')

        for i in range(self.n):
            for j in range(self.n): 
                destination.insert(self.n*i + j, self.cube[face.value][pos(i,j)])
        
        self.cube[face.value] = destination.copy()

    def spin(self, faces, posLambda):
        aux_face = self.cube[faces[0]].copy()
        for i in range(len(faces) - 1):
            for j in range(self.n):
                self.cube[faces[i]][posLambda(j)] = self.cube[faces[i + 1]][posLambda(j)]

        for j in range(self.n):
            self.cube[faces[-1]][posLambda(j)] = aux_face[posLambda(j)]

    def spinCol(self, face, column, direction):
        if(face == 2 or face == 4):
            raise ValueError('Invalid face, for sides use spinSide')

        SPIN_FACES_UP = [[Faces.FRONT.value, Faces.BOTTOM.value, Faces.BACK.value, Faces.TOP.value],
                         [Faces.TOP.value, Faces.FRONT.value, Faces.BOTTOM.value, Faces.BACK.value]]
        SPIN_FACES_DOWN = [[Faces.FRONT.value, Faces.TOP.value, Faces.BACK.value, Faces.BOTTOM.value],
                           [Faces.TOP.value, Faces.BACK.value, Faces.BOTTOM.value, Faces.FRONT.value]]
        #       En la posicion que denota la cara en X va el valor de la que se encuentra en la cara que esta en X+1

        if (direction == Directions.DOWN):
            faces = SPIN_FACES_DOWN[face.value % 3]
        elif (direction == Directions.UP):
            faces = SPIN_FACES_UP[face.value % 3]
        else: raise ValueError('Invalid direction')
        self.spin(faces, lambda j: j * self.n + column)
        
    def spinRow(self, face, row, direction):
        if(face == 2 or face == 4):
            raise ValueError('Invalid face, for sides use spinSide')

        SPIN_FACES_LEFT = [Faces.FRONT.value, Faces.RIGHT.value, Faces.BACK.value, Faces.LEFT.value]
        SPIN_FACES_RIGHT = [Faces.FRONT.value, Faces.LEFT.value, Faces.BACK.value, Faces.RIGHT.value]

        if (direction == Directions.LEFT):
            faces = SPIN_FACES_LEFT
        elif (direction == Directions.RIGHT):
            faces = SPIN_FACES_RIGHT
        else: raise ValueError('Invalid direction')

        self.spin(faces, lambda j: self.n * row + j)

    def spinSide(self, face, column, direction):
        SPIN_SIDE_UP = [Faces.LEFT.value, Faces.BOTTOM.value, Faces.RIGHT.value, Faces.TOP.value]
        SPIN_SIDE_DOWN = [Faces.LEFT.value, Faces.TOP.value, Faces.RIGHT.value, Faces.BOTTOM.value]
        SIDE_LAMBDAS_UP=[
            lambda j: (self.n-1 -j)*self.n + column,       #LEFT
            lambda j: self.n*(self.n-column) -j -1,        #BOTTOM
            lambda j: j*self.n + (self.n-1 -column),        #RIGHT
            lambda j: self.n * column + j                   #TOP
        ]
        SIDE_LAMBDAS_DOWN=[
            lambda j: j*self.n + column,                    #LEFT
            lambda j: self.n * column + self.n -1 - j,         #TOP
            lambda j: (self.n-1 -j)*self.n + self.n -1 -column, #RIGHT
            lambda j: self.n * (self.n -1 -column) + j      #BOTTOM
        ]
        if (direction == Directions.DOWN):
            faces = SPIN_SIDE_DOWN
            lambdas = SIDE_LAMBDAS_DOWN
        elif (direction == Directions.UP):
            faces = SPIN_SIDE_UP
            lambdas = SIDE_LAMBDAS_UP
        else: raise ValueError('Invalid direction')

        aux_face = self.cube[faces[0]].copy()
        for i in range(len(faces) -1):
            for j in range(self.n):
                self.cube[faces[i]][lambdas[i](j)] = self.cube[faces[i+1]][lambdas[i+1](j)]

        for j in range(self.n):
            self.cube[faces[3]][lambdas[3](j)] = aux_face[lambdas[0](j)]
    
    def move(self, direction):
        if direction == Directions.TOP_LEFT:
            self.spinRow(Faces.FRONT, 0, Directions.LEFT)
            self.rotate(Faces.BOTTOM, Rotations.CLOCKWISE)
        elif direction == Directions.TOP_RIGHT:
            self.spinRow(Faces.FRONT, 0, Directions.RIGHT)
            self.rotate(Faces.BOTTOM, Rotations.ANTICLOCKWISE)
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
            self.spinRow(Faces.FRONT, self.n-1, Directions.LEFT)
            self.rotate(Faces.BOTTOM, Rotations.ANTICLOCKWISE)
        elif direction == Directions.BOTTOM_RIGHT:
            self.spinRow(Faces.FRONT, self.n-1, Directions.RIGHT)
            self.rotate(Faces.BOTTOM, Rotations.CLOCKWISE)
        elif direction == Directions.ROTATE_ANTICLOCKWISE:
            self.rotate(Faces.FRONT, Rotations.ANTICLOCKWISE)
            self.spinSide(Faces.LEFT, self.n - 1, Directions.DOWN)
        elif direction == Directions.ROTATE_CLOCKWISE:
            self.rotate(Faces.FRONT, Rotations.CLOCKWISE)
            self.spinSide(Faces.LEFT, self.n - 1, Directions.UP)
        else:
            print('Invalid direction')
        
