
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
                pos = self.n*(j) + self.n - i - 1 if direction == 'CLOCKWISE' else self.n*(self.n - j - 1) + i
                # clockwise: (i, j) -> (j, n-i-1)
                # anticlockwise: (i, j) -> (n-j-1, i)
                destination.insert(self.n*i + j, self.cube[face][pos])
        
        self.cube[face] = destination.copy()


    def spinCol(self, face, column, direction):
        #rotate 1
        #spin 0,2,5,4
        #SPIN_FACES = [list(reversed([0, 1, 5, 3])), [1, 5, 3, 0], [2, 1, 4, 3]]
        SPIN_FACES = [[3, 5, 1, 0], [0, 3, 5, 1], [3, 4, 1, 2]]
        # 0 -> 0 1 5 3 
        # 1 -> 1 5 3 0
        # 2 -> 2 1 4 3
        # 3 -> 3 0 1 5 CONTRACARA DE 1
        # 4 -> 4 1 2 3 CONTRACARA DE 2
        # 5 -> 5 1 0 3 CONTRACARA DE 0
        aux_face = self.cube[3].copy()
        for i in range(len(SPIN_FACES[face])-1):
            for j in range(self.n):
                self.cube[SPIN_FACES[face][i]][j*self.n + column] = self.cube[SPIN_FACES[face][i+1]][j*self.n + column]
        
        print(SPIN_FACES[face][-1])
        for j in range(self.n):
            self.cube[SPIN_FACES[face][-1]][j*self.n + column] = aux_face[j*self.n+ column]



    def move(self, direction):
        if direction == 'TOP_LEFT':
            self.spinTop(-1)
        elif direction == 'TOP_RIGHT':
            self.spinTop(1)
        elif direction == 'LEFT_UP':
            self.spinLeft(1)
        elif direction == 'LEFT_DOWN':
            self.spinLeft(-1)
        elif direction == 'RIGHT_UP':
            self.spinCol(0, 1, 'UP')
        elif direction == 'RIGHT_DOWN':
            self.spinRight(-1)
        elif direction == 'BOTTOM_LEFT':
            self.spinBottom(-1)
        elif direction == 'BOTTOM_RIGHT':
            self.spinBottom(1)
        elif direction == 'ROTATE_LEFT':
            self.rotate(0,'ANTICLOCKWISE')
            #self.spin()
        elif direction == 'ROTATE_RIGHT':
            self.rotate(0,'CLOCKWISE')
            self.spin()
        else:
            print('Invalid direction')
        

    
    
