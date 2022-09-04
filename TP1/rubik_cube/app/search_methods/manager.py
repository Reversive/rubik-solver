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
        self.method.insert_nodes([Node(rubik.cube, None, None, 0, self.method.calculate_heuristic, self.n)])
        # self.border = collections.deque([Node(rubik.cube, None, None, 0, self.method.calculate_weight, self.n)])
        self.depth_of_states = {}
        self.rubik_utils = rubik_utils

    def solve(self, csv = False):
        i = 0
        possible_moves = list(map(int, MovesN3 if self.n == 3 else MovesN2))
        # para root
        node = self.method.pop()
        self.visited += 1
        rubik = Rubik(self.n, self.rubik_utils, node.state)
        self.depth_of_states[self.state_string(node.state)] = node.depth

        while not self.rubik_utils.is_solved(node.state) and (len(self.method.border) > 0 or self.visited == 1):
            if node.last_movement is not None:
                # chequeo que no sea root node
                next_moves = [m for m in possible_moves
                            if m != int((node.last_movement + (len(MovesN3) / 2)) % len(MovesN3))]
            else: next_moves = possible_moves

            random.shuffle(next_moves)
            new_borders = []
            for next_move in next_moves:
                new_state = rubik.move(next_move)
                new_state_str = self.state_string(new_state)
                new_depth = node.depth + 1
                if(new_state_str not in self.depth_of_states or self.depth_of_states[new_state_str] > new_depth):
                    # Solo expando cuando no he visitado el estado o si es menos profundo que cuando lo visite
                    new_node = Node(new_state,
                        node, next_move, new_depth,
                        self.method.calculate_heuristic, self.n)
                    self.depth_of_states[new_state_str] = new_node.depth
                    new_borders.append(new_node)
                else: self.visited += 1 # no lo agrego a la frontera pero si lo cuento como visitado

            self.method.insert_nodes(new_borders)
            
            self.visited += 1        
            node = self.method.pop()

            rubik = Rubik(self.n, self.rubik_utils, node.state)
            if not csv and self.visited % 250000 == 0:
                print(self.visited, node.depth, len(self.method.border))

        if self.rubik_utils.is_solved(node.state):
            if(csv):
                return f"{self.visited},{node.depth},{len(self.method.border)}"
            else:
                print("Nodos visitados: " + str(self.visited))
                print("Estados encontrados: " + str(len(self.depth_of_states)))
                print("Nodos borde: " + str(len(self.method.border)))
                print("Profundidad: " + str(node.depth))
                moves_to_solution = ""
                parent = node
                while parent.last_movement is not None:
                    if(self.n == 2):
                        prev_move = MovesN2(parent.last_movement)
                    else: prev_move = MovesN3(parent.last_movement)
                    moves_to_solution = str(prev_move) + " " + moves_to_solution
                    parent = parent.parent
                print("Moves to solution: " + moves_to_solution)
            return node
        else:
            raise ValueError('No solution found')

    def state_string(self, state):
        return ''.join([
            ''.join(state[0]),
            ''.join(state[1]),
            ''.join(state[2]),
            ''.join(state[3]),
            ''.join(state[4]),
            ''.join(state[5])])
