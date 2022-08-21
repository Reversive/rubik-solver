from arguments.parser import parser
from enums.moves import Moves
from rubik import Rubik
from heuristics.color_heuristic import get_color_heursitic_weight
from search_methods.manager import Manager
from search_methods.methods import BFS, DFS, Greedy
import numpy as np

RANDOM_SEED = 111
RANDOM_MOVES = 15


def shuffleRubik(rubik):
    for i in range(RANDOM_MOVES):
        rubik = rubik.move(Moves(np.random.randint(0, len(Moves))))

    return rubik


def main(n):
    np.random.seed(RANDOM_SEED)  # TODO: revisar que esta seed se aplica a todos los random que se llaman luego?

    rubik = Rubik(n)
    rubik = shuffleRubik(rubik)
    print("to_string: " + rubik.to_string())
    #manager = Manager(Greedy(get_color_heursitic_weight), rubik)
    manager = Manager(BFS(), rubik)
    #manager = Manager(DFS(), rubik)

    result = manager.solve()
    print("to_string: " + result.state.to_string())


if __name__ == '__main__':
    args = parser.parse_args()

    main(args.options.n)
