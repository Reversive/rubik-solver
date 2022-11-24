import requests
from PIL import Image
import os
BASE_URL = "https://pokeapi.co/api/v2/pokemon/"
IMAGES_PATH = "TP3/data/pokemon_images/"
GS_IMAGES_PATH = "TP3/data/GS_pokemon_images/"

def make_grayscale_pokemons():
    for image_file_name in os.listdir(IMAGES_PATH):
        image = Image.open(IMAGES_PATH + image_file_name)
        grayscale = image.convert('L')
        grayscale.save(GS_IMAGES_PATH + image_file_name)


# desde pipenv shell, justo fuera del repositorio
# python -m TP3.data.load_images
if __name__ == "__main__":
    for i in range(1, 151 +1, 1):
        url = BASE_URL + str(i)
        response = requests.get(url)
        data = response.json()
        image_url = data['sprites']['front_default']
        image = requests.get(image_url)
        with open("TP3/data/pokemon_images/" + str(i) + ".png", 'wb') as f:
            f.write(image.content)
    
