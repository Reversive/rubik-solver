import time

import numpy as np

from arguments.parser import parser
from enums.moves import Moves
from rubik import Rubik
from rubik_utils import RubikUtils
from search_methods.manager import Manager
from search_methods.methods import BFS

RANDOM_SEED = 111
RANDOM_MOVES = 7


def shuffleRubik(rubik):
    for i in range(RANDOM_MOVES):
        rubik.cube = rubik.move(Moves(i))

    return rubik


def main(n):
    np.random.seed(RANDOM_SEED)
    rubikUtils = RubikUtils(n)
    rubik = Rubik(n, rubikUtils)
    rubik = shuffleRubik(rubik)
    print("input: " + rubik.to_string())
    # manager = Manager(Greedy(get_color_heursitic_weight), rubik)
    manager = Manager(BFS(), rubik, rubikUtils)
    # manager = Manager(DFS(), rubik)
    start_time = time.time()
    result = manager.solve()
    print('Solucionado: SI')
    print("Rubik cube: \n" + str(result.state))
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == '__main__':
    args = parser.parse_args()

    main(args.options.n)
