import numpy as np


class Node:
    def __init__(self, rubikState, parent, lastMovement, deep):
        self.parent = parent
        self.state = rubikState
        self.lastMovement = lastMovement
        self.deep = deep
        self.children = []

    def add_children(self, newChildren):
        self.children = np.append(self.children, newChildren)

    def get_children(self, i=0):
        return self.children[i]

    def get_parent(self):
        return self.parent

    def __cmp__(self, other):
        return self.deep < other.deep

    def __eq__(self, other):
        return self.__cmp__(other)

    def __ne__(self, other):
        return not self.__cmp__(other)

    def __lt__(self, other):
        return False

    def __hash__(self):
        return hash(str(self))
