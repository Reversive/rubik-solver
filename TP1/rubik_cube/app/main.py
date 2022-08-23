import time

import numpy as np

from heuristics.color_heuristic import get_color_heursitic_weight
from arguments.parser import parser
from enums.moves import Moves
from rubik import Rubik
from rubik_utils import RubikUtils
from search_methods.manager import Manager
from search_methods.methods import BFS, DFS, AStar, LocalGreedy, GlobalGreedy

RANDOM_SEED = 111
RANDOM_MOVES = 8


def shuffleRubik(rubik):
    for i in range(RANDOM_MOVES):
        rubik.cube = rubik.move(i % (len(Moves)-1))

    return rubik


def main(n):
    np.random.seed(RANDOM_SEED)
    rubikUtils = RubikUtils(n)
    rubik = Rubik(n, rubikUtils)
    rubik = shuffleRubik(rubik)
    print("input: " + rubik.to_string())
    manager1 = Manager(LocalGreedy(get_color_heursitic_weight), rubik, rubikUtils)
    manager2 = Manager(AStar(get_color_heursitic_weight), rubik, rubikUtils)
    manager3 = Manager(BFS(), rubik, rubikUtils)
    manager4 = Manager(DFS(), rubik, rubikUtils)
    manager5 = Manager(GlobalGreedy(get_color_heursitic_weight), rubik, rubikUtils)
    start_time = time.time()
    result = manager2.solve()
    print('Solucionado: SI')
    print("Rubik cube: \n" + str(result.state))
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == '__main__':
    args = parser.parse_args()

    main(args.options.n)
