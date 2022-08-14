from arguments.parser import parser
from directions import Directions
from rubik import Rubik
from faces import Faces

if __name__ == '__main__':
    args = parser.parse_args()

    rubik = Rubik(args.options.n)
    print(rubik.cube)
    rubik.move(Directions.ROTATE_RIGHT)
    rubik.move(Directions.LEFT_UP)
    rubik.move(Directions.RIGHT_UP)
    rubik.move(Directions.RIGHT_DOWN)
    rubik.move(Directions.LEFT_DOWN)
    rubik.move(Directions.ROTATE_LEFT)
    print(rubik.cube)