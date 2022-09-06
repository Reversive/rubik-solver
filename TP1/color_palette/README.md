# Sistemas de Inteligencia Artificial

# [TP1](https://github.com/Reversive/sia-repo/tree/main/TP1) - Parte B: Algoritmos Genéticos

Implementación mediante Algoritmos Genéticos de un sistema de mezcla de pigmentos.

## Ejecución

Ubicandose en el directorio app, ejecutar

```sh
python3 main.py <file.json>
```

En dónde el archivo .json debe contener:

* population_size: tamaño de la población
* colors_amount: cantidad de colores disponibles de la paleta
* target_color: color deseado. Debe ser un array de n elementos (n >= 1).
* selection_fun: función de selección a utilizar. Se puede elegir entre "elite", "roulette", "prob_tournament" y "
  det_tournament".
* crossover_fun: función de crossover a utilizar. Se puede elegir entre "point" y "uniforme".
* mutation_prob: probabilidad que un gen mute.
* mutation_range: rango en el cual un gen puede variar al mutar.
* k: número de elementos que se seleccionarán en las funciones de selección.
* max_generations: cantidad límite de generaciones.
* initial_population: array de colores iniciales.

En caso que no se espeficaran, se tomará por defecto:

```sh
{
  "population_size": 100,
  "colors_amount": 20,
  "target_color": [
    0.25,
    0.5,
    0.25
  ],
  "selection_fun": "elite",
  "crossover_fun": "uniform",
  "mutation_prob": 0.05,
  "mutation_range": 0.1,
  "k": 10,
  "max_generations": 2000
}
```

Opcionalmente, la poblacion inicial se inserta de la siguiente forma:

```
{
  "initial_population": [
    [
      0.1,
      0.1,
      0.01
    ],
    [
      0.05,
      0.15,
      0.25
    ],
    [
      0.3,
      0.02,
      0.2
    ],
    [
      0.05,
      0.2,
      0.03
    ],
    [
      0.25,
      0.14,
      0.12
    ],
    [
      0.25,
      0.25,
      0.25
    ]
  ]
}
```