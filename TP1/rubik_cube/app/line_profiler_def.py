import line_profiler

import rubik_cube.app.solver as solver
import rubik
import search_methods

profiler = line_profiler.LineProfiler()
profiler.add_function(search_methods.manager.Manager.solve)
# profiler.add_function(rubik.Rubik.move_col)
# profiler.add_function(rubik.Rubik.move_row)
# profiler.add_function(rubik.Rubik.move_rotate)
# profiler.add_function(rubik.Rubik.spin_col)
# profiler.add_function(rubik.Rubik.spin_row)
# profiler.add_function(rubik.Rubik.spin_side)
# profiler.add_function(rubik.Rubik.spin)
# profiler.add_function(rubik.Rubik.rotate)

wrapper = profiler(solver.main)
wrapper(2)

profiler.print_stats(open("line_profiler_ans.txt", "w"), output_unit=1)
