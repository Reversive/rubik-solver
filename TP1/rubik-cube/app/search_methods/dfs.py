from operator import mod
from search_methods.node import Node
from enums.directions import Directions
import copy
import numpy as np

class DFS:
    def __init__(self, cube):
        self.visited = []
        self.border = []
        self.deepsOfStates = {cube.toString(): 0} # TODO: IMPLEMENTAR
        self.border.append(Node(cube, None, Directions.NULL))
        np.random.seed(123456) # TODO: constante general
        
    def solve(self):
        node = self.border.pop(0)
        i=0
        while not node.state.isSolved() or not len(self.border) == 0:
            #a = list(range(len(Directions)))
            nextSteps = np.arange(1, len(Directions))
            nextSteps = np.delete(nextSteps, 5)
            nextSteps = nextSteps[nextSteps != len(Directions)-1-node.lastMovement.value] 
            np.random.shuffle(nextSteps)
            # sacar el anterior step
            for nextStep in nextSteps:
                direction = Directions(nextStep)
                newNode = Node(copy.deepcopy(node.state), node, direction)
                newNode.state.move(direction)
                self.border.insert(0, newNode)
            
            self.visited.append(node)
            node = self.border.pop(0)
            i+=1


        if node.state.isSolved():
            return node
        else: raise ValueError('No solution found')
        
