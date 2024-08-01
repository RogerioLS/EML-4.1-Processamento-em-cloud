import unittest
from sources.a_fetch_dataset import PokemonDataFetcher
from sources.g_unit_test import TestPokemonDataFetcher

def run_tests():
    test_loader = unittest.TestLoader()
    test_suite = test_loader.loadTestsFromTestCase(TestPokemonDataFetcher)
    test_runner = unittest.TextTestRunner()
    result = test_runner.run(test_suite)
    return result.wasSuccessful()

def main():
    fetcher = PokemonDataFetcher(start_id=1, end_id=100, output_file='data/pokemon_data.json')
    fetcher.fetch_data()

if __name__ == '__main__':
    # Executa os testes unitários
    if run_tests():
        print("All tests passed. Proceeding to fetch data.")
        main()
    else:
        print("Some tests failed. Fix the issues before fetching data.")
