from utils.Perceptron import Perceptron
import numpy as np


class StepClassifier:
    def __init__(self):
        self.perceptron = Perceptron(np.sign, 2, 0.01)
        train_dataset = [[1, 1, 1], [0, 1, -1], [1, 0, -1], [0, 0, -1]]
        self.perceptron.train(train_dataset)
        print(self.perceptron.test([1, 1]) == 1)
        print(self.perceptron.test([0, 1]) == -1)
        print(self.perceptron.test([1, 0]) == -1)
        print(self.perceptron.test([0, 0]) == -1)

#Habria que ver una manera de definir la red, hacer algun metodo o algo para poder decir algo onda
#Tengo 3 capas, 2 nodos por capa, y que se encargue de entrenar la red pasandole el input y listo, no tener
#que ir nodo por nodo


#Para hacer el XOR, habria que usar algo asi, va es lo que se me ocurre pero como nadie explico que logica
#deberian llevar las redes

#  - e1 -> v1 ---
#              \v5 ---> O
#              /
#  - e2 -> v2 ---
#v1 hace OR, v2 hace !AND, y v5 hace AND de los dos outputs, tal vez el Not deberia ir aparte, npi...