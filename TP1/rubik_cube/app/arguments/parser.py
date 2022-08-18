from simple_parsing import ArgumentParser
from .options import Options

parser = ArgumentParser(
    prog='Rubik Cube Solver',
    description='Project with the goal of making an AI to solve a rubiks cube.\nThe AI algorithms used are BFS, DFS, Greedy and A*\nThere are x heuristics implemented: ...')

parser.add_arguments(Options, dest='options')
