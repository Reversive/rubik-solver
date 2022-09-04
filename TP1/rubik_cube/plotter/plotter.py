import matplotlib.pyplot as plt
import numpy as numpy


def read_csv(file):
    out = open(file, 'r')
    current_line = out.readline()
    visited_nodes = []
    depth = []
    border_nodes = []
    time = []
    while current_line is not None and current_line != '':
        aux = current_line.split(',')
        aux[-1] = aux[-1].strip('\n')
        visited_nodes.append(aux[1])
        depth.append(aux[2])
        border_nodes.append(aux[3])
        time.append(aux[4])
    return visited_nodes, depth, border_nodes, time


def analyze_parsed_data(visited_nodes, depth, border_nodes, time):
    visited_nodes_mean = numpy.mean(visited_nodes) + numpy.mean(border_nodes)
    visited_nodes_std = numpy.std(visited_nodes) + numpy.std(border_nodes)
    time_mean = numpy.mean(time)
    time_std = numpy.std(time)
    return visited_nodes_std, visited_nodes_mean, time_mean, time_std


def read_search_method(method_name):
    visited_nodes_points = []
    visited_nodes_error = []
    time_nodes_points = []
    time_nodes_errors = []
    aux = [2,6,9]
    for i in range(3):
        visited_nodes, depth, border_nodes, time = read_csv('./' + method_name + '/out_' + str(aux[i]) + '.csv')
        visited_node_point, visited_node_error, time_node_point, time_node_error = analyze_parsed_data(visited_nodes, depth, border_nodes, time)
        visited_nodes_points.append(visited_node_point)
        visited_nodes_error.append(visited_node_error)
        time_nodes_points.append(time_node_point)
        time_nodes_errors.append(time_node_error)
    return visited_nodes_points, visited_nodes_error, aux




if __name__ == '__main__':
    visited_nodes_BFS, visited_nodes_error_BFS, cases = read_search_method('BFS')
    plt.errorbar(visited_nodes_BFS, cases, yerr=visited_nodes_error_BFS, fmt='-o')
    visited_nodes_BFS, visited_nodes_error_BFS, cases = read_search_method('ASTAR_DIFFCOLORS')
    plt.errorbar(visited_nodes_BFS, cases, yerr=visited_nodes_error_BFS, fmt='-x')
    visited_nodes_BFS, visited_nodes_error_BFS, cases = read_search_method('ASTAR_SMANHATTAN')
    plt.errorbar(visited_nodes_BFS, cases, yerr=visited_nodes_error_BFS, fmt='-s')
    plt.xlabel('Cases')
    plt.ylabel('Expanded nodes')
    plt.grid()
    plt.title('Expanded nodes vs Cases')
    plt.legend(['BFS','ASTAR_DIFFCOLORS','ASTAR_SMANHATTAN'])