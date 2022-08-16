from operator import mod
from search_methods.node import Node
from enums.directions import Directions
import copy
import numpy as np


class DFS:
    def __init__(self, cube):
        self.visited = []
        self.border = []
        self.deepsOfStates = {}
        self.border.append(Node(cube, None, Directions.NULL))
        np.random.seed(123456)  # TODO: constante general

    def solve(self):
        i = 0
        node = self.border[0]
        while not node.state.is_solved() and len(self.border) > 0:
            stateKey = node.state.to_string()
            if (stateKey not in self.deepsOfStates or self.deepsOfStates[stateKey] > node.deep):
                # Solo expando cuando no he visitado el estado o si es menos profundo que cuando lo visite
                self.deepsOfStates[stateKey] = node.deep
                nextMovements = np.arange((-len(Directions) + 1) / 2, (len(Directions) - 1) / 2 + 1)
                nextMovements = np.delete(nextMovements, np.where(nextMovements == Directions.NULL.value) or np.where(
                    nextMovement == -1 * node.lastMovement.value))
                np.random.shuffle(nextMovements)
                for nextMovement in nextMovements:
                    direction = Directions(nextMovement)
                    newNode = Node(copy.deepcopy(node.state), node, direction, node.deep + 1)
                    newNode.state.move(direction)
                    self.border.insert(0, newNode)
                    node.add_children(newNode)

            self.visited.append(node)
            node = self.border.pop(0)
            i += 1
            if i % 100 == 0:
                print(i)

        if node.state.is_solved():
            return node
        else:
            raise ValueError('No solution found')
