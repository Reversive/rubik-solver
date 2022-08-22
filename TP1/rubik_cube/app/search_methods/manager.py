from operator import mod
from search_methods.node import Node
from enums.moves import Moves
import numpy as np
import collections
from rubik import Rubik

class Manager:
    BORDER_DTYPE = [('heuristicValue', float), ('node', Node)]

    def __init__(self, method, rubik):
        self.method = method
        self.visited = []
        self.border = collections.deque([Node(rubik.cube, None, None, 0, self.method.calculate_weight)])
        self.deepsOfStates = {}
        self.n = rubik.n

    def solve(self):
        i = 0

        # para root
        node = self.border.pop()
        rubik = Rubik(self.n, node.state)

        while not rubik.is_solved() and (len(self.border) > 0 or len(self.visited) == 0):
            if rubik.to_string() not in self.deepsOfStates or self.deepsOfStates[
                rubik.to_string()] > node.deep:
                # Solo expando cuando no he visitado el estado o si es menos profundo que cuando lo visite
                self.deepsOfStates[rubik.to_string()] = node.deep
                nextMovements = np.arange(0, len(Moves))
                if node.lastMovement is not None:
                    # chequeo que no sea root node
                    nextMovements = np.delete(nextMovements,
                                              int((node.lastMovement.value + (len(Moves) / 2)) % len(Moves)))

                np.random.shuffle(nextMovements)
                newBorder = []
                newChildren = []

                for nextMovement in nextMovements:
                    direction = Moves(nextMovement)
                    newNode = Node(
                                rubik.move(direction), 
                                node, direction, node.deep + 1,
                                   self.method.calculate_weight)
                    newBorder = [newNode] + newBorder
                    newChildren = [newNode] + newChildren

                node.add_children(newChildren)
                self.border = self.method.insert_nodes(self.border,
                                                      newBorder)  # agrego todos los nuevos border de una

            self.visited.append(node)
            node = self.border.popleft()
            rubik = Rubik(self.n, node.state)
            i += 1
            if i % 1000 == 0:
                print(i)

        if rubik.is_solved():
            print("Nodos expandidos: " + str(len(self.visited)))
            print("Nodos borde: " + str(len(self.border)))
            print("Profundidad: " + str(len(self.deepsOfStates)))
            return node
        else:
            raise ValueError('No solution found')
