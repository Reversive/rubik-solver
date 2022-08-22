from arguments.parser import parser
from enums.moves import Moves
from rubik import Rubik
from heuristics.color_heuristic import get_color_heursitic_weight
from search_methods.manager import Manager
from search_methods.methods import BFS, DFS, Greedy
import numpy as np
import time

RANDOM_SEED = 111
RANDOM_MOVES = 4


def shuffleRubik(rubik):
    for i in range(RANDOM_MOVES):
        rubik = rubik.move(Moves(i))

    return rubik


def main(n):
    np.random.seed(RANDOM_SEED)

    rubik = Rubik(n)
    rubik = shuffleRubik(rubik)
    print("input: " + rubik.to_string())
    manager = Manager(Greedy(get_color_heursitic_weight), rubik)
    #manager = Manager(BFS(), rubik)
    #manager = Manager(DFS(), rubik)
    start_time = time.time()
    result = manager.solve()
    print('Solucionado: SI')
    print("Rubik cube: " + result.state.to_string())
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == '__main__':
    args = parser.parse_args()

    main(args.options.n)
