class Node:
    def __init__(self, rubik, parent, lastMovement):
        self.parent = parent
        self.state = rubik # TODO: se podria guardar de una forma mas eficiente?
        self.children = [] # TODO: ver como hacemos esto con numpy pq hay que saber el tamaño
        self.lastMovement = lastMovement
        
    def add_children(self, children):
        self.children.append(children)
    
    def get_children(self, i=0):
        return self.children[i]
        
    def get_parent(self):
        return self.parent
