import line_profiler
import rubik
import search_methods
import main

profiler = line_profiler.LineProfiler()
profiler.add_function(search_methods.manager.Manager.solve)
profiler.add_function(rubik.Rubik.move)
profiler.add_function(rubik.Rubik.move_col)
profiler.add_function(rubik.Rubik.move_row)
profiler.add_function(rubik.Rubik.move_rotate)
profiler.add_function(rubik.Rubik.spin_col)
profiler.add_function(rubik.Rubik.spin_row)
profiler.add_function(rubik.Rubik.spin_side)
profiler.add_function(rubik.Rubik.spin)

wrapper = profiler(main.main)
wrapper(2)

profiler.print_stats(open("line_profiler_res.txt", "w"))
