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

def main(n, algorithm, scramble, seed, timeout, csv):
    rubikUtils = RubikUtils(n)
    managers = {
        "BFS": lambda r: Manager(BFS(), r, rubikUtils),
        "DFS": lambda r: Manager(DFS(), r, rubikUtils),
        "ASTAR1": lambda r: Manager(AStar(get_color_heursitic_weight), r, rubikUtils),
        "ASTAR2": lambda r: Manager(AStar(get_faces_colors_weight), r, rubikUtils),
        "LGREEDY1": lambda r: Manager(LocalGreedy(get_color_heursitic_weight), r, rubikUtils),
        "LGREEDY2": lambda r: Manager(LocalGreedy(get_faces_colors_weight), r, rubikUtils),
        "GGREEDY1": lambda r: Manager(GlobalGreedy(get_color_heursitic_weight), r, rubikUtils),
        "GGREEDY2": lambda r: Manager(GlobalGreedy(get_faces_colors_weight), r, rubikUtils)
    }

    manager = managers[algorithm]
    random.seed(seed)
    rubik = Rubik(n, rubikUtils)
    shuffled_rubik = shuffleRubik(rubik, scramble)
    start_time = time.time()
    try:
        if not csv:
            print("ALGORITHM " + algorithm)
            print("MOVES QTY: " + str(scramble))
            print("SEED: " + str(seed))
            print("input: " + shuffled_rubik.to_string())
            
        result = func_timeout.func_timeout(timeout, lambda: manager(shuffled_rubik).solve(True), args=())
        execution_time = time.time() - start_time
        if csv:
            print(f"{result},{execution_time}")
        else:
            print("--- %s seconds ---\n" % execution_time)
    except func_timeout.FunctionTimedOut:
        print('Solucionado: NO')

    # rubikVisualizer = rubik_visualizer.Rubik_Visualizer(manager3)
    # rubikVisualizer.visualize()

if __name__ == '__main__':
    args = parser.parse_args()

    main(args.options.n, args.options.algorithm, args.options.scramble, args.options.seed, args.options.timeout, args.options.csv)
