import numpy as np


class Node:
    def __init__(self, state, parent, lastMovement, depth, calculateWeight, n):
        self.parent = parent
        self.state = state
        self.lastMovement = lastMovement
        self.depth = depth
        self.weight = calculateWeight(self, n)

    def get_parent(self):
        return self.parent

    def __cmp__(self, other):
        return self.weight.__cmp__(other.weight)

    def __eq__(self, other):
        return self.__hash__() == other.__hash__()

    def __ne__(self, other):
        return self != other

    def __lt__(self, other):
        return self.weight < other.weight

    def __hash__(self):
        return hash(str(self))
