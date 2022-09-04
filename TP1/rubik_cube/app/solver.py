import time
import random
import func_timeout

from heuristics.color_heuristic import get_color_heursitic_weight
from heuristics.faces_colors import get_faces_colors_weight
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

def main(n, algorithm, scramble, timeout):
    rubikUtils = RubikUtils(n)
    manager_BFS = lambda r: Manager(BFS(), r, rubikUtils)
    manager_DFS = lambda r: Manager(DFS(), r, rubikUtils)
    manager_ASTAR = lambda r: Manager(AStar(get_color_heursitic_weight), r, rubikUtils)
    manager_ASTAR = lambda r: Manager(AStar(get_faces_colors_weight), r, rubikUtils)
    manager_LGREEDY = lambda r: Manager(LocalGreedy(get_color_heursitic_weight), r, rubikUtils)
    manager_LGREEDY = lambda r: Manager(LocalGreedy(get_faces_colors_weight), r, rubikUtils)
    manager_GGREEDY = lambda r: Manager(GlobalGreedy(get_color_heursitic_weight), r, rubikUtils)
    manager_GGREEDY = lambda r: Manager(GlobalGreedy(get_faces_colors_weight), r, rubikUtils)
    managers = [manager_BFS, manager_DFS, manager_LGREEDY, manager_LGREEDY, manager_ASTAR, manager_ASTAR, manager_GGREEDY, manager_GGREEDY]

    managers = {
        "BFS": manager_BFS,
        "DFS": manager_DFS,
        "ASTAR1": manager_ASTAR,
        "ASTAR2": manager_ASTAR,
        "LGREEDY1": manager_LGREEDY,
        "LGREEDY2": manager_LGREEDY,
        "GGREEDY1": manager_GGREEDY,
        "GGREEDY2": manager_GGREEDY
    }

    print("ALGORITHM " + algorithm)
    manager = managers[algorithm]
    print("MOVES QTY: " + str(scramble))
    random.seed(RANDOM_SEED)
    rubik = Rubik(n, rubikUtils)
    shuffled_rubik = shuffleRubik(rubik, scramble)
    print("input: " + shuffled_rubik.to_string())
    start_time = time.time()
    try:
        result = func_timeout.func_timeout(timeout, lambda: manager(shuffled_rubik).solve(), args=())
        print('Solucionado: SI')
        print("Rubik cube: \n" + str(result.state))
    except func_timeout.FunctionTimedOut:
        print('Solucionado: NO')
    print("--- %s seconds ---\n" % (time.time() - start_time))

    # rubikVisualizer = rubik_visualizer.Rubik_Visualizer(manager3)
    # rubikVisualizer.visualize()
    print("\n\n")

if __name__ == '__main__':
    args = parser.parse_args()

    main(args.options.n, args.options.algorithm, args.options.scramble, args.options.timeout)
