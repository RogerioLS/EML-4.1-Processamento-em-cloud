import unittest
from sources.a_fetch_dataset import PokemonDataFetcher

class TestPokemonDataFetcher(unittest.TestCase):
    def test_fetch_data(self):
        fetcher = PokemonDataFetcher(start_id=1, end_id=2, output_file='data/test_pokemon_data.json')
        fetcher.fetch_data()
        data = fetcher.get_data()
        
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]['id'], 1)
        self.assertEqual(data[1]['id'], 2)
        self.assertIn('name', data[0])
        self.assertIn('types', data[0])
        self.assertIn('height', data[0])
        self.assertIn('weight', data[0])
        self.assertIn('moves', data[0])

if __name__ == '__main__':
    unittest.main()
