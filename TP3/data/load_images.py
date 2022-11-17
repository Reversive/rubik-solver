import requests
BASE_URL = "https://pokeapi.co/api/v2/pokemon/"

# desde pipenv shell, justo fuera del repositorio
# python -m TP3.data.load_images
if __name__ == "__main__":
    for i in range(1, 35, 3):
        url = BASE_URL + str(i)
        response = requests.get(url)
        data = response.json()
        image_url = data['sprites']['front_default']
        image = requests.get(image_url)
        with open("TP3/data/pokemon_images/" + str(i) + ".png", 'wb') as f:
            f.write(image.content)
    
