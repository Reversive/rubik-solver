import bisect


class Method(object):
    def __init__(self):
        pass

    def insert_node(self, array, node):
        pass

    def calculate_weight(self, node, n):
        return 0


class BFS(Method):
    def insert_node(self, array, node):
        array.append(node)

        return array


class Greedy(Method):
    def __init__(self, heuristic):
        super().__init__()
        self.heuristic = heuristic

    def insert_node(self, array, node):
        bisect.insort(array, node)
        return array

    def calculate_weight(self, node, n):
        return self.heuristic(node.state, n)


class AStar(Method):
    def __init__(self, heuristic):
        super().__init__()
        self.heuristic = heuristic

    def insert_node(self, array, node):
        bisect.insort(array, node)
        return array

    def calculate_weight(self, node, n):
        return self.heuristic(node.state, n) + node.deep


class DFS(Method):
    def insert_node(self, array, node):
        array.appendleft(node)

        return array
