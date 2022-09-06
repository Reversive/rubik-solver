import numpy as numpy
import matplotlib.pyplot as plt

def csv_population(palette_list, method):
    file = open('./plotter/' + method, 'w')

    for i in palette_list:
        file.write(str(numpy.mean(list(map(lambda x: x.fitness, i)))) + ' ')
        file.write(str(numpy.std(list(map(lambda x: x.fitness, i)))) + '\n')
    file.close()

def read_csv(method):
    file = open('./' + method, 'r')
    fitness_by_gen = []
    error_by_gen = []
    current_line = file.readline()
    while current_line != '':
        current_line = current_line.split(' ')
        current_line[-1] = current_line[-1].strip()
        fitness_by_gen.append(float(current_line[0]))
        error_by_gen.append(float(current_line[1]))
        current_line = file.readline()
    file.close()
    return fitness_by_gen, error_by_gen

if __name__ == '__main__':

    fitness_by_gen, error_by_gen = read_csv('elite_point')
    plt.errorbar(y=fitness_by_gen, x=range(len(fitness_by_gen)), yerr=error_by_gen, elinewidth=0.1, fmt='-')

    fitness_by_gen, error_by_gen = read_csv('prob_tournament_uniform')
    plt.errorbar(y=fitness_by_gen, x=range(len(fitness_by_gen)), yerr=error_by_gen, elinewidth=0.1, fmt='-')

    plt.xlabel('Generation')
    plt.ylabel('Fitness')
    plt.grid()
    plt.title('Fitness vs Generation')
    legend = plt.legend(['One-point','Uniform'])
    legend.set_title('Crossover')
    plt.show()