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
        self.depth_of_states[self.state_string(node.state)] = node.depth

        while not self.rubik_utils.is_solved(node.state) and (len(self.border) > 0 or self.visited == 1):
            if node.lastMovement is not None:
                # chequeo que no sea root node
                next_moves = [m for m in possible_moves
                            if m != int((node.lastMovement + (len(MovesN3) / 2)) % len(MovesN3))]
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
                        self.method.calculate_weight, self.n)
                    self.depth_of_states[new_state_str] = new_node.depth
                    new_borders.append(new_node)
                else: self.visited += 1 # no lo agrego a la frontera pero si lo cuento como visitado

            self.border = self.method.insert_nodes(self.border, new_borders)
            
            self.visited += 1
            node = self.border.popleft()
            rubik = Rubik(self.n, self.rubik_utils, node.state)
            if self.visited % 50000 == 0:
                print(self.visited, node.depth, len(self.border))

        if self.rubik_utils.is_solved(node.state):
            self.visited += 1
            print("Nodos expandidos: " + str(self.visited))
            print("Nodos borde: " + str(len(self.border)))
            print("Profundidad: " + str(node.depth))
            moves_to_solution = ""
            parent = node
            while parent.lastMovement is not None:
                if(self.n == 2):
                    prev_move = MovesN2(parent.lastMovement)
                else: prev_move = MovesN3(parent.lastMovement)
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
