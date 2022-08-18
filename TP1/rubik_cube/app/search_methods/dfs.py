from operator import mod
from rubik import Rubik
from search_methods.node import Node
from enums.moves import Moves
import numpy as np


class DFS:
    def __init__(self, rubik):
        self.visited = []
        self.border = []
        self.deepsOfStates = {}
        self.n = rubik.n  # TODO: cambiar esto?
        self.border.append(Node(rubik.cube, None, Moves.NULL))
        np.random.seed(123456)  # TODO: constante general

    def solve(self):
        i = 0

        # para root
        node = self.border.pop(0)
        rubikNode = Rubik(self.n, node.state)

        while not rubikNode.is_solved() and (len(self.border) > 0 or len(self.visited) == 0):
            if (node.state.tostring() not in self.deepsOfStates or self.deepsOfStates[node.state.tostring()] > node.deep):
                # Solo expando cuando no he visitado el estado o si es menos profundo que cuando lo visite
                self.deepsOfStates[node.state.tostring()] = node.deep

                nextMovements = np.arange((-len(Moves) + 1) / 2, (len(Moves) - 1) / 2 + 1)
                nextMovements = np.delete(nextMovements, [int((len(Moves) - 1) / 2), 6 - node.lastMovement.value])
                np.random.shuffle(nextMovements)

                for nextMovement in nextMovements:
                    direction = Moves(nextMovement)
                    newNode = Node(rubikNode.move(direction), node, direction, node.deep + 1)
                    self.border.insert(0, newNode)
                    node.add_children(newNode)

            self.visited.append(node)
            node = self.border.pop(0)
            rubikNode = Rubik(self.n, node.state)
            i += 1
            if i % 1000 == 0:
                print(i)

        if rubikNode.is_solved():
            return node
        else:
            raise ValueError('No solution found')
