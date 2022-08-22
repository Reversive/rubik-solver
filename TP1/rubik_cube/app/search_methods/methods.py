import numpy as np
import bisect


class Method(object):
    def __init__(self):
        pass

    def insert_nodes(self, array, nodes):
        pass

    def calculate_weight(self, nodes):
        return 0


class BFS(Method):
    def insert_nodes(self, array, nodes):
        for node in nodes:
            array.append(node)

        return array


class Greedy(Method):
    def __init__(self, heuristic):
        super().__init__()
        self.heuristic = heuristic

    def insert_nodes(self, array, nodes):
        for node in nodes:
            bisect.insort(array, node)
        return array

    def calculate_weight(self, nodes):
        return self.heuristic(nodes)


class DFS(Method):
    def insert_nodes(self, array, nodes):
        for node in nodes:
            array.appendleft(node)
            
        return array
