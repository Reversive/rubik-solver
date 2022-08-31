from arguments.parser import parser
import numpy as np

from data_structure.Solver import Solver


def main(target, available_colors):
    solver = Solver(available_colors, target)
    print(solver.current_palette[0])


if __name__ == '__main__':
    args = parser.parse_args()
    avail_colors = np.array([[0.01, 0.02, 0.02], [0.001, 0.02, 0.02], [0.020, 0.02, 0.02]])
    target_color = np.array([0.01, 0.02, 0.021])
    main(target_color, avail_colors)
