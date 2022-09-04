from dataclasses import dataclass
from socket import timeout


@dataclass
class Options:
    n: int = 2  # dimension of the cube (nxn)
    scramble: int = 5  # how many times to scramble the cube
    algorithm: str = "bfs"  # algorithm to use to solve the cube
    timeout: int = 90  # timeout for the algorithm to solve the cube
    seed: int = 12345 # seed for the random number generator
    csv: bool = False  # if true, the output will be in csv format
