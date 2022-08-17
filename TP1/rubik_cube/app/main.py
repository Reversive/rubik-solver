from arguments.parser import parser
from enums.directions import Directions
from rubik import Rubik
from search_methods.dfs import DFS

def main(n):

    rubik = Rubik(n)
    print(rubik.cube)
    rubik.move(Directions.FRONT_ROTATE_CLOCKWISE)
    # rubik.move(Directions.TOP_LEFT)
    # rubik.move(Directions.BOTTOM_RIGHT)
    # rubik.move(Directions.FRONT_ROTATE_ANTICLOCKWISE)
    # rubik.move(Directions.LEFT_DOWN)
    # rubik.move(Directions.RIGHT_UP)
    # rubik.move(Directions.RIGHT_UP)
    # rubik.move(Directions.FRONT_ROTATE_ANTICLOCKWISE)
    # rubik.move(Directions.TOP_RIGHT)

    dfs = DFS(rubik)
    print(dfs.solve())

    # rubik.move(Directions.TOP_LEFT)
    # rubik.move(Directions.FRONT_ROTATE_CLOCKWISE)
    # rubik.move(Directions.RIGHT_DOWN)
    # rubik.move(Directions.RIGHT_DOWN)
    # rubik.move(Directions.LEFT_UP)
    # rubik.move(Directions.FRONT_ROTATE_CLOCKWISE)
    # rubik.move(Directions.BOTTOM_LEFT)
    # rubik.move(Directions.TOP_RIGHT)
    # rubik.move(Directions.FRONT_ROTATE_ANTICLOCKWISE)

    print(rubik.cube)

if __name__ == '__main__':
    args = parser.parse_args()

    main(args.options.n)
