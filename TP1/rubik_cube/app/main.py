from arguments.parser import parser
from enums.moves import Moves
from rubik import Rubik
from search_methods.manager import Manager
from search_methods.methods import BFS, DFS
import numpy as np

RANDOM_SEED = 123456789
MAX_RANDOM_MOVES = 20

def shuffleRubik(rubik):
    movesQty = np.random.randint(1, MAX_RANDOM_MOVES) 
    for i in range(movesQty):
        rubik.cube = rubik.move(Moves(np.random.randint(0, len(Moves))))

    return rubik


def main(n):
    np.random.seed(RANDOM_SEED) # TODO: revisar que esta seed se aplica a todos los random que se llaman luego?

    rubik = Rubik(n)
    print("to_string: " + rubik.to_string())
    rubik = shuffleRubik(rubik)
    bfs = Manager(BFS(), rubik)
    print(bfs.solve())


if __name__ == '__main__':
    args = parser.parse_args()

    main(args.options.n)
