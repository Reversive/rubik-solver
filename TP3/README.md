# TP3: [Autoencoder](https://github.com/Reversive/sia-repo/blob/main/TP3/font_generator.py) y [Variable Autoencoder](https://github.com/Reversive/sia-repo/blob/main/TP3/pokemon_generator.py)

## Instalación:
Desde el directorio `./TP3`, ejecutar `pipenv install`, luego `pipenv shell` para acceder al entorno virtual. Una vez dentro, salir fuera del directorio ejecutando `cd ..`y desde allí se pueden ejecutar los distintos programas.


### Como ejecutar el ejercicio de aprendizaje de font.h con autoencoders
En el archivo `./TP3/config.yaml` se puede configurar los parametros del ejercicio, las epocas, su beta, su función de activación, cantidad de epocas, taza de aprendizaje, mejoras entre otras cosas.

Una vez se encuentra configurado como se desea, para ejecutarlo se debe utilizar desde el entorno virtual:
`python -m TP3.font_generator`

### Como ejecutar el ejercicio de aprendizaje de pokemones con VAE
Una vez se encuentra configurado como se desea, para ejecutarlo se debe utilizar desde el entorno virtual:
`python -m TP3.pokemon_generator`
