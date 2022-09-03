import time

import random

from heuristics.color_heuristic import get_color_heursitic_weight
from arguments.parser import parser
from enums.moves import MovesN2, MovesN3
from rubik import Rubik
from rubik_visualizer import rubik_visualizer
from rubik_utils import RubikUtils
from search_methods.manager import Manager
from search_methods.methods import BFS, DFS, IDDFS, AStar, LocalGreedy, GlobalGreedy

RANDOM_SEED = 12345
RANDOM_MOVES = 1



def shuffleRubik(rubik, moves_qty):
    possibleMoves = list(map(int, MovesN3 if rubik.n == 3 else MovesN2))
    nextMove = None
    for i in range(moves_qty):
        if nextMove is not None:
            nextMoves = [m for m in possibleMoves
                         if m != int((nextMove + (len(MovesN3) / 2)) % len(MovesN3))]
        else: nextMoves = possibleMoves

        nextMove = random.choice(nextMoves)
        rubik.cube = rubik.move(nextMove)

    return rubik


def main(n):
    for moves_qty in [8]:
        random.seed(RANDOM_SEED)
        rubikUtils = RubikUtils(n)
        rubik = Rubik(n, rubikUtils)
        rubik = shuffleRubik(rubik, moves_qty)
        print("input: " + rubik.to_string())
        manager1 = Manager(LocalGreedy(get_color_heursitic_weight), rubik, rubikUtils)
        manager2 = Manager(AStar(get_color_heursitic_weight), rubik, rubikUtils)
        manager3 = Manager(BFS(), rubik, rubikUtils)
        manager4 = Manager(DFS(), rubik, rubikUtils)
        manager5 = Manager(IDDFS(), rubik, rubikUtils)
        manager6 = Manager(GlobalGreedy(get_color_heursitic_weight), rubik, rubikUtils)
        start_time = time.time()
        result = manager3.solve()
        print('Solucionado: SI')
        print("Rubik cube: \n" + str(result.state))
        print("--- %s seconds ---" % (time.time() - start_time))
        # rubikVisualizer = rubik_visualizer.Rubik_Visualizer(manager3)
        # rubikVisualizer.visualize()


if __name__ == '__main__':
    args = parser.parse_args()

    main(args.options.n)
