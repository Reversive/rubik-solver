from enums.directions import Directions
import numpy as np


class Node:
    def __init__(self, rubik, parent, lastMovement, deep=0):
        self.parent = parent
        self.state = rubik  # TODO: se podria guardar de una forma mas eficiente?
        self.lastMovement = lastMovement
        self.deep = deep
        self.children = []

    def add_children(self, newChildren):
        self.children = np.append(self.children, newChildren)

    def get_children(self, i=0):
        return self.children[i]

    def get_parent(self):
        return self.parent
