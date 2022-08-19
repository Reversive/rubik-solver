from arguments.parser import parser
from enums.moves import Moves
from rubik import Rubik
from search_methods.manager import Manager
from search_methods.methods import BFS, DFS
import numpy as np


def main(n):
    rubik = Rubik(n)
    rubik.cube = rubik.move(Moves.TOP_LEFT)
    rubik.cube = rubik.move(Moves.FRONT_ROTATE_CLOCKWISE)
    rubik.cube = rubik.move(Moves.BOTTOM_RIGHT)
    rubik.cube = rubik.move(Moves.FRONT_ROTATE_ANTICLOCKWISE)
    # rubik.cube = rubik.move(Moves.LEFT_DOWN)
    # rubik.cube = rubik.move(Moves.RIGHT_UP)
    # rubik.cube = rubik.move(Moves.RIGHT_UP)
    # rubik.cube = rubik.move(Moves.FRONT_ROTATE_ANTICLOCKWISE)
    # rubik.cube = rubik.move(Moves.TOP_RIGHT)

    print("to_string: " + rubik.to_string())
    bfs = Manager(DFS(), rubik)
    print(bfs.solve())

    # rubik.move(Directions.TOP_LEFT)
    # rubik.move(Directions.FRONT_ROTATE_CLOCKWISE)
    # rubik.move(Directions.RIGHT_DOWN)
    # rubik.move(Directions.RIGHT_DOWN)
    # rubik.move(Directions.LEFT_UP)
    # rubik.move(Directions.FRONT_ROTATE_CLOCKWISE)
    # rubik.move(Directions.BOTTOM_LEFT)
    # rubik.move(Directions.TOP_RIGHT)
    # rubik.move(Directions.FRONT_ROTATE_ANTICLOCKWISE)


if __name__ == '__main__':
    args = parser.parse_args()

    main(args.options.n)
