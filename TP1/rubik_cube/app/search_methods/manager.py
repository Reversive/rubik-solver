from operator import mod
from rubik import Rubik
from search_methods.node import Node
from enums.moves import Moves
import numpy as np


class Manager:
    def __init__(self, method, rubik):
        self.method = method
        self.visited = np.array([], dtype=Node)
        self.border = np.array([], dtype=Node)
        self.border = np.append(self.border, Node(rubik.cube, None, Moves.NULL))
        self.deepsOfStates = {}
        self.n = rubik.n  # TODO: cambiar esto?
        np.random.seed(123456)  # TODO: constante general

    def solve(self):
        i = 0

        # para root
        node = self.border[0]
        self.border = np.delete(self.border, 0)

        rubikNode = Rubik(self.n, node.state)

        while not rubikNode.is_solved() and (len(self.border) > 0 or len(self.visited) == 0):
            if (node.state.tostring() not in self.deepsOfStates or self.deepsOfStates[node.state.tostring()] > node.deep):
                # Solo expando cuando no he visitado el estado o si es menos profundo que cuando lo visite
                self.deepsOfStates[node.state.tostring()] = node.deep

                nextMovements = np.arange((-len(Moves) + 1) / 2, (len(Moves) - 1) / 2 + 1)
                nextMovements = np.delete(nextMovements, [int((len(Moves) - 1) / 2), 6 - node.lastMovement.value])
                np.random.shuffle(nextMovements)
                newBorder = np.empty(len(nextMovements), dtype=Node)

                for index, nextMovement in enumerate(nextMovements):
                    direction = Moves(nextMovement)
                    newNode = Node(rubikNode.move(direction), node, direction, node.deep + 1)
                    node.add_children(newNode)
                    newBorder[index] = newNode

            self.border = self.method.insertNode(self.border, newBorder) # agrego todos los nuevos border de una
            self.visited = np.append(self.visited, newNode)

            node = self.border[0]
            self.border = np.delete(self.border, 0)

            rubikNode = Rubik(self.n, node.state)
            i += 1
            if i % 1000 == 0:
                print(i)

        if rubikNode.is_solved():
            print("visited nodes: " + str(len(self.visited)))
            print("result: " + str(rubikNode.to_string()))
            print("deeps of states: " + str(len(self.deepsOfStates)))
            return node
        else:
            raise ValueError('No solution found')
