import numpy as np



class Node:
    def __init__(self, state, parent, last_movement, depth, calculate_heuristic, n):
        self.parent = parent
        self.state = state
        self.last_movement = last_movement
        self.depth = depth
        self.heuristic = calculate_heuristic(self, n)
        self.weight = self.heuristic + depth

    def get_parent(self):
        return self.parent
