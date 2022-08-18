import numpy as np


class Node:
    def __init__(self, rubikState, parent, lastMovement, deep=0):
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
