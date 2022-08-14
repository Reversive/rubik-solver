from faces import Faces
from directions import Directions
from rotations import Rotations

class Rubik:
    def __init__(self, n = 2):
        #frente, arriba, izquierda, abajo, derecha, atras
        self.cube = [[],[],[],[],[],[]]
        self.n = n
        
        for i in range(6):
           for j in range(n*n):
              self.cube[i].append(i)

    
    def rotate(self, face, direction):
        destination = []
        for i in range(self.n):
            for j in range(self.n): 
                pos = self.n*(j) + self.n - i - 1 if direction == Rotations.CLOCKWISE else self.n*(self.n - j - 1) + i
                # clockwise: (i, j) -> (j, n-i-1)
                # anticlockwise: (i, j) -> (n-j-1, i)
                destination.insert(self.n*i + j, self.cube[face.value][pos])
        
        self.cube[face.value] = destination.copy()


    def spinCol(self, face, column, direction):
        SPIN_FACES_UP = [   [Faces.FRONT.value, Faces.BOTTOM.value, Faces.BACK.value, Faces.TOP.value], 
                            [Faces.TOP.value, Faces.FRONT.value, Faces.BOTTOM.value, Faces.BACK.value], 
                            [Faces.LEFT.value, Faces.BOTTOM.value, Faces.RIGHT.value, Faces.TOP.value]]
        SPIN_FACES_DOWN = [ [Faces.FRONT.value, Faces.TOP.value, Faces.BACK.value, Faces.BOTTOM.value], 
                            [Faces.TOP.value, Faces.BACK.value, Faces.BOTTOM.value, Faces.FRONT.value], 
                            [Faces.LEFT.value, Faces.TOP.value, Faces.RIGHT.value, Faces.BOTTOM.value]]
#       En la posicion que denota la cara en X va el valor de la que se encuentra en la cara que esta en X+1

        if(direction == Directions.DOWN):
            faces = SPIN_FACES_DOWN[face.value % 3]
        else: faces = SPIN_FACES_UP[face.value % 3]
       
        aux_face = self.cube[faces[Faces.FRONT.value]].copy()
        for i in range(len(faces)-1):
            for j in range(self.n):
                self.cube[faces[i]][j*self.n + column] = self.cube[faces[i+1]][j*self.n + column]
        
        for j in range(self.n):
            self.cube[faces[-1]][j*self.n + column] = aux_face[j*self.n + column]


    def move(self, direction):
        if direction == Directions.TOP_LEFT:
            self.spinTop(-1)
        elif direction == Directions.TOP_RIGHT:
            self.spinTop(1)
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
            self.rotate(Faces.FRONT,Rotations.ANTICLOCKWISE)
            self.spinCol(Faces.LEFT, self.n - 1, Directions.DOWN)
        elif direction == Directions.ROTATE_RIGHT:
            self.rotate(Faces.FRONT,Rotations.CLOCKWISE)
            self.spinCol(Faces.LEFT, self.n - 1, Directions.UP)
        else:
            print('Invalid direction')
        

    
    
