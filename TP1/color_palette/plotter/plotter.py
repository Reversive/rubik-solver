import numpy as numpy
import matplotlib.pyplot as plt

def plot_population(palette_list):
    plt.axes(projection ='3d')
    x, y, z = zip(*palette_list)
    print(x)



    plt.xlabel('Cases')
    plt.yscale('log')
    plt.ylabel('Expanded nodes')
    plt.grid()
    plt.title('Expanded nodes vs Cases')
    plt.legend(['BFS','ASTAR_DIFFCOLORS','ASTAR_SMANHATTAN'])
    plt.show()