from arguments.parser import parser
from rubik import Rubik

if __name__ == '__main__':
    args = parser.parse_args()

    rubik = Rubik(args.options.n)
    print(rubik.cube)
    
    rubik.move('RIGHT_UP')
    print(rubik.cube)