from dataclasses import dataclass

@dataclass
class Options:
    n:  int = 2             # dimension of the cube (nxn)
    scramble:   int = 5             # how many times to scramble the cube
    algorithm:  str = "bfs"         # algorithm to use to solve the cube
    heuristic:  str = "manhattan"   # heuristic to use to solve the cube