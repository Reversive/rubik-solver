from arguments.parser import parser
from enums.directions import Directions
from rubik import Rubik
from enums.faces import Faces

if __name__ == '__main__':
    args = parser.parse_args()

    rubik = Rubik(args.options.n)
    print(rubik.cube)
    rubik.move(Directions.ROTATE_CLOCKWISE)
    rubik.move(Directions.TOP_LEFT)
    rubik.move(Directions.BOTTOM_RIGHT)
    rubik.move(Directions.ROTATE_ANTICLOCKWISE)
    rubik.move(Directions.LEFT_DOWN)
    rubik.move(Directions.RIGHT_UP)
    rubik.move(Directions.RIGHT_UP)
    rubik.move(Directions.ROTATE_ANTICLOCKWISE)
    rubik.move(Directions.TOP_RIGHT)


    rubik.move(Directions.TOP_LEFT)
    rubik.move(Directions.ROTATE_CLOCKWISE)
    rubik.move(Directions.RIGHT_DOWN)
    rubik.move(Directions.RIGHT_DOWN)
    rubik.move(Directions.LEFT_UP)
    rubik.move(Directions.ROTATE_CLOCKWISE)
    rubik.move(Directions.BOTTOM_LEFT)
    rubik.move(Directions.TOP_RIGHT)
    rubik.move(Directions.ROTATE_ANTICLOCKWISE)

    print(rubik.cube)
