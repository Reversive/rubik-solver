import bisect

import numpy as np

from rubik_cube.app.enums.moves import Moves


class Method(object):
    def __init__(self):
        pass

    def insert_nodes(self, array, nodes):
        pass

    def calculate_weight(self, node, n):
        return 0


class BFS(Method):
    def insert_nodes(self, array, nodes):
        for node in nodes:
            array.append(node)

        return array


class LocalGreedy(Method):
    def __init__(self, heuristic):
        super().__init__()
        self.heuristic = heuristic

    def insert_nodes(self, array, nodes):
        nodes.sort()
        for node in nodes:
            array.appendleft(node)
        return array

    def calculate_weight(self, node, n):
        return self.heuristic(node.state, n)



class GlobalGreedy(Method):
    def __init__(self, heuristic):
        super().__init__()
        self.heuristic = heuristic

    def insert_nodes(self, array, nodes):
        for node in nodes:
            bisect.insort(array, node)
        return array

    def calculate_weight(self, node, n):
        return self.heuristic(node.state, n)


class AStar(Method):
    def __init__(self, heuristic):
        super().__init__()
        self.heuristic = heuristic

    def insert_nodes(self, array, nodes):
        for node in nodes:
            bisect.insort(array, node)
        return array

    def calculate_weight(self, node, n):
        return self.heuristic(node.state, n) + node.deep


class DFS(Method):
    def insert_nodes(self, array, nodes):
        # recibe ordenados de mas viejos a mas nuevos, por eso el reverse
        for node in nodes[::-1]:
            array.appendleft(node)

        return array


class IDDFS(Method):
    def __init__(self):
        super().__init__()
        self.depth_step = 2
        self.sum_count = 0

    def insert_nodes(self, array, nodes):
        self.sum_count = 0
        for node in nodes[::-1]:
            if node.deep <= self.depth_step:
                array.appendleft(node)

        #Bueno lo pusheo pq lo unico que falta es aumentar el depth_step, pero no se puede meter recursivo pq no tengo los nodos de los arboles antiguos
        #Si a alguno se le ocurre algo :8
        return array

