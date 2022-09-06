# Sistemas de Inteligencia Artificial

# [TP1](https://github.com/Reversive/sia-repo/tree/main/TP1) - Parte A: Métodos de búsqueda
Implementación de un motor de búsqueda de soluciones para un Cubo Rubik. 

## Como utilizar el solucionador de rubiks
Ejecutar el siguiente comando:
```python3 -u solver.py -n=N --timeout=TIMEOUT --algorithm=ALGORITHM --scramble=SCRAMBLE --seed=SEED --csv=CSV```

Dónde los argumentos son:
- n: Dimensión del rubik (default 2)
- timeout: Timeout que tiene el solucionador (default 90)
- algorithm: Algoritmo de busqueda a utilizar (defaults a BFS, pero puede ser: DFS, ASTAR1, ASTAR2, LGREEDY1, LGREEDY2, GGREEDY1, GGREEDY2)
- scramble: Cantidad de movimientos que se realizan sobre el rubik al mezclarlo (default 5)
- seed: Semilla (integer) utilizada para los generadores de numeros aleatorios (default 12345)
- csv: Booleano que indica si el output debe ser en formato CSV o no (default False)

