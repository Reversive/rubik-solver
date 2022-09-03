import collections

import random
from enums.moves import MovesN2, MovesN3
from rubik import Rubik
from search_methods.node import Node


class Manager:
    BORDER_DTYPE = [('heuristicValue', float), ('node', Node)]

    def __init__(self, method, rubik, rubik_utils):
        self.method = method
        self.visited = 0
        self.n = rubik.n
        self.border = collections.deque([Node(rubik.cube, None, None, 0, self.method.calculate_weight, self.n)])
        self.depth_of_states = {}
        self.rubik_utils = rubik_utils

    def solve(self):
        i = 0
        possible_moves = list(map(int, MovesN3 if self.n == 3 else MovesN2))
        # para root
        node = self.border.pop()
        self.visited += 1
        rubik = Rubik(self.n, self.rubik_utils, node.state)

        while not rubik.is_solved() and (len(self.border) > 0 or self.visited == 1):
            if rubik.to_string() not in self.depth_of_states or self.depth_of_states[
                rubik.to_string()] > node.depth:
                # Solo expando cuando no he visitado el estado o si es menos profundo que cuando lo visite
                self.depth_of_states[rubik.to_string()] = node.depth
                if node.lastMovement is not None:
                    # chequeo que no sea root node
                    next_moves = [m for m in possible_moves
                             if m != int((node.lastMovement + (len(MovesN3) / 2)) % len(MovesN3))]
                else: next_moves = possible_moves

                random.shuffle(next_moves)
                new_borders = []
                for nextMove in next_moves:
                    new_node = Node(
                        rubik.move(nextMove),
                        node, nextMove, node.depth + 1,
                        self.method.calculate_weight, self.n)
                    new_borders.append(new_node)
                self.border = self.method.insert_nodes(self.border, new_borders)
            
            self.visited += 1
            node = self.border.popleft()
            rubik = Rubik(self.n, self.rubik_utils, node.state)
            if self.visited % 50000 == 0:
                print(self.visited, node.depth, len(self.border))

        if rubik.is_solved():
            self.visited += 1
            print("Nodos expandidos: " + str(self.visited))
            print("Nodos borde: " + str(len(self.border)))
            print("Profundidad: " + str(node.depth))
            moves_to_solution = ""
            parent = node.parent
            while parent is not None:
                moves_to_solution = str(node.lastMovement) + " " + moves_to_solution
                parent = parent.parent
            print("Moves to solution: " +moves_to_solution)
            return node
        else:
            raise ValueError('No solution found')
