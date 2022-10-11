# TP2: [Perceptrón Simple](https://github.com/Reversive/sia-repo/tree/main/TP2/onelayer_network) y [Multicapa](https://github.com/Reversive/sia-repo/tree/main/TP2/multilayer_network)

## Como utilizar la red neuronal:
Desde el directorio `./TP2`, ejecutar `pipenv install`, luego `pipenv shell` para acceder al entorno virtual. Una vez dentro, salir fuera del directorio ejecutando `cd ..`y desde allí se pueden ejecutar los distintos programas.


### Perceptrón simple
En el archivo `./TP2/onelayer_network/config.yaml` se puede configurar el perceptrón con su tipo, su beta, su función de activación, cantidad de epocas, taza de aprendizaje y el directorio absoluto donde se encuentra el dataset a utilizar.

Una vez se encuentra configurado como se desea, para ejecutarlo se debe utilizar desde el entorno virtual:
`python -m TP2.onelayer_network.main`

### Perceptrón multicapa
Analogamente al simple, existe un archivo de configuración en `./TP2/multilayer_network/config.yaml` donde se puede decidir beta, la función de activación, la cantidad de epocas, la taza de aprendizaje y el ejercicio a resolver. 

Una vez se encuentra configurado como se desea, para ejecutarlo se debe utilizar desde el entorno virtual:
`python -m TP2.multilayer_network.main`
