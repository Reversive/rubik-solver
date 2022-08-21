from operator import mod
from rubik import Rubik
from search_methods.node import Node
from enums.moves import Moves
import numpy as np


class Manager:
    BORDER_DTYPE = [('heuristicValue', float), ('node', Node)]

    def __init__(self, method, rubik):
        self.method = method
        self.visited = np.array([], dtype=Node)
        self.border = np.array([], dtype=self.BORDER_DTYPE)
        self.border = np.append(self.border, np.array([(0, Node(rubik, None, None, 0))], dtype=self.BORDER_DTYPE))
        self.deepsOfStates = {}
        self.n = rubik.n  # TODO: cambiar esto?

    def solve(self):
        i = 0

        # para root
        node = self.border[0][1]
        self.border = np.delete(self.border, 0)

        while not node.state.is_solved() and (len(self.border) > 0 or len(self.visited) == 0):
            if node.state.to_string() not in self.deepsOfStates or self.deepsOfStates[
                node.state.to_string()] > node.deep:
                # Solo expando cuando no he visitado el estado o si es menos profundo que cuando lo visite
                self.deepsOfStates[node.state.to_string()] = node.deep
                nextMovements = np.arange(0, len(Moves))
                if node.lastMovement is not None:
                    # chequeo que no sea root node
                    nextMovements = np.delete(nextMovements,
                                              int((node.lastMovement.value + (len(Moves) / 2)) % len(Moves)))

                np.random.shuffle(nextMovements)
                newBorder = np.empty(len(nextMovements), dtype=self.BORDER_DTYPE)

                for index, nextMovement in enumerate(nextMovements):
                    direction = Moves(nextMovement)
                    newNode = Node(node.state.move(direction), node, direction, node.deep + 1)
                    newTuple = (self.method.calculate_weight(newNode), newNode)
                    node.add_children(newTuple)
                    newBorder[index] = newTuple

                self.border = self.method.insert_node(self.border,
                                                      newBorder)  # agrego todos los nuevos border de una
                self.visited = np.append(self.visited, node)

            node = self.border[0][1]
            self.border = np.delete(self.border, 0)

            i += 1
            if i % 1000 == 0:
                print(i)

        if node.state.is_solved():
            print("visited nodes: " + str(len(self.visited)))
            print("border nodes: " + str(len(self.border)))
            print("deeps of states: " + str(len(self.deepsOfStates)))
            return node
        else:
            raise ValueError('No solution found')
