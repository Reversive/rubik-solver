import numpy as np


class Method(object):
    def __init__(self):
        pass

    def insert_node(self, array, node):
        pass

    def calculate_weight(self, node):
        return 0


class BFS(Method):
    def insert_node(self, array, node):
        return np.append(array, node)

class Greedy(Method):
    def __init__(self, heuristic):
        super().__init__()
        self.heuristic = heuristic

    def insert_node(self, array, node):
        array = np.append(array, node)
        return np.sort(array)

    def calculate_weight(self, node):
        return self.heuristic(node.state)


class DFS(Method):
    def insert_node(self, array, node):
        return np.insert(array, 0, node)
