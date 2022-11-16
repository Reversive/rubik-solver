import requests
BASE_URL = "https://pokeapi.co/api/v2/pokemon/"

# desde /TP3 ejecutar python3 data/load_images.py

if __name__ == "__main__":
    for i in range(1, 25, 3):
        url = BASE_URL + str(i)
        response = requests.get(url)
        data = response.json()
        image_url = data['sprites']['front_default']
        image = requests.get(image_url)
        with open("data/pokemon_images/" + str(i) + ".png", 'wb') as f:
            f.write(image.content)
    
