import line_profiler
import rubik
import search_methods
import main


profiler = line_profiler.LineProfiler()
profiler.add_function(search_methods.dfs.DFS.solve)

wrapper = profiler(main.main)
wrapper(2)

profiler.print_stats(open("line_profiler_res.txt", "w"))
