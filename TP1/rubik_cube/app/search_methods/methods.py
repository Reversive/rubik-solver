import numpy as np

class Method(object):
    def __init__(self, insertIdx = None):
        self.insertIdx = insertIdx
    
    def insertNode(self, array, node):
        pass

    def popNode(self, array):
        pass


class BFS(Method):
    def insertNode(self, array, node):
        return np.append(array, node)


class DFS(Method):
    def insertNode(self, array, node):
        return np.insert(array, 0, node)
