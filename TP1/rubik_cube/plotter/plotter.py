import matplotlib.pyplot as plt
import numpy as numpy

CASES = [2,6,9]

def read_csv(file):
    out = open(file, 'r')
    current_line = out.readline()
    visited_nodes = []
    depth = []
    border_nodes = []
    time = []
    current_line = out.readline()
    solved_percentage = 0
    total = 0
    while current_line.startswith('S'):
        total += 1
        current_line = out.readline()
    while current_line is not None and current_line != '':
        aux = current_line.split(',')
        aux[-1] = aux[-1].strip('\n')
        visited_nodes.append(int(aux[1]))
        depth.append(int(aux[2]))
        border_nodes.append(int(aux[3]))
        time.append(float(aux[4]))
        current_line = out.readline()
        while current_line.startswith('S'):
            total += 1
            current_line = out.readline()
        total += 1
        solved_percentage += 1

    out.close()
    return visited_nodes, depth, border_nodes, time, round((solved_percentage*100)/total,2)

def analyze_parsed_data(visited_nodes, depth, border_nodes, time):
    visited_nodes_mean = numpy.mean(visited_nodes) + numpy.mean(border_nodes)
    visited_nodes_std = numpy.std(visited_nodes) + numpy.std(border_nodes)
    time_mean = numpy.mean(time)
    time_std = numpy.std(time)
    return visited_nodes_mean, visited_nodes_std, time_mean, time_std

def read_search_method(method_name):
    visited_nodes_points = []
    visited_nodes_error = []
    time_nodes_points = []
    time_nodes_errors = []
    for i in CASES:
        visited_nodes, depth, border_nodes, time,solved_percentage = read_csv('./' + method_name + '/out_' + str(i) + '.csv')
        visited_node_point, visited_node_error, time_node_point, time_node_error = analyze_parsed_data(visited_nodes, depth, border_nodes, time)
        visited_nodes_points.append(visited_node_point)
        visited_nodes_error.append(visited_node_error)
        time_nodes_points.append(time_node_point)
        time_nodes_errors.append(time_node_error)
    return visited_nodes_points, visited_nodes_error, time_nodes_points, time_nodes_errors, solved_percentage

if __name__ == '__main__':
    visited_nodes, visited_nodes_error, time_nodes, time_errors, bfs_solved_percentage = read_search_method('BFS')
    plt.errorbar(y=time_nodes, x=CASES, yerr=time_errors, fmt='-o')

    visited_nodes, visited_nodes_error, time_nodes, time_errors, astar_diff_solved_percentage = read_search_method('ASTAR_DIFFCOLORS')
    plt.errorbar(y=time_nodes, x=CASES, yerr=time_errors, fmt='-x')

    visited_nodes, visited_nodes_error, time_nodes, time_errors, astar_sman_solved_percentage = read_search_method('ASTAR_SMANHATTAN')
    plt.errorbar(y=time_nodes, x=CASES, yerr=time_errors, fmt='-s')

    visited_nodes, visited_nodes_error, time_nodes, time_errors,iddfs_solved_percentage = read_search_method('IDDFS')
    plt.errorbar(y=time_nodes, x=CASES,yerr=time_errors, fmt='-p')
    print(visited_nodes)
    plt.xlabel('Cases')
    plt.yscale('log')
    plt.ylabel('time(s)')
    plt.grid()
    plt.title('Time vs Cases')
    plt.legend(['BFS', 'ASTAR_DIFFCOLORS','ASTAR_SMANHATTAN', 'IDDFS(step = 3)'])
    plt.show()
