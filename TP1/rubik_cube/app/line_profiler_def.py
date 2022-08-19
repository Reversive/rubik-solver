import line_profiler
import rubik
import search_methods
import main

profiler = line_profiler.LineProfiler()
profiler.add_function(search_methods.manager.Manager.solve)
profiler.add_function(rubik.Rubik.move)

wrapper = profiler(main.main)
wrapper(2)

profiler.print_stats(open("line_profiler_res.txt", "w"))
