import numpy as np


class Node:
    def __init__(self, state, parent, lastMovement, deep, calculateWeight, n):
        self.parent = parent
        self.state = state
        self.lastMovement = lastMovement
        self.deep = deep
        self.weight = calculateWeight(self, n)
        self.children = []

    def add_children(self, newChildren):
        self.children.append(newChildren)

    def get_children(self, i=0):
        return self.children[i]

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
