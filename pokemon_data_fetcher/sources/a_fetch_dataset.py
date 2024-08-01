import requests
import json

class PokemonDataFetcher:
    def __init__(self, start_id=1, end_id=500, output_file='data/pokemon_data.json'):
        self.start_id = start_id
        self.end_id = end_id
        self.output_file = output_file
        self.pokemon_data = []

    def fetch_data(self):
        for pokemon_id in range(self.start_id, self.end_id + 1):
            url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}/"
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()
                pokemon_info = {
                    'id': data['id'],
                    'name': data['name'],
                    'types': [t['type']['name'] for t in data['types']],
                    'height': data['height'],
                    'weight': data['weight'],
                    'moves': [move['move']['name'] for move in data['moves']]
                }
                self.pokemon_data.append(pokemon_info)
                self._save_data()
                print(f"Successfully retrieved data for Pokémon ID {pokemon_id}")
            else:
                print(f"Failed to retrieve data for Pokémon ID {pokemon_id}: {response.status_code}")

    def _save_data(self):
        with open(self.output_file, 'w') as f:
            json.dump(self.pokemon_data, f, indent=4)

    def get_data(self):
        return self.pokemon_data
