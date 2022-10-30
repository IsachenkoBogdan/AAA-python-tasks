from src.one_hot_encoder import fit_transform
from typing import List
import unittest


class TestOneHotEncoder(unittest.TestCase):
    def test_cities_str_eq(self):
        cities = ['Moscow', 'New York', 'Moscow', 'Tomsk']
        exp_transformed_cities = [('Moscow', [0, 0, 1]),
                                  ('New York', [0, 1, 0]),
                                  ('Moscow', [0, 0, 1]),
                                  ('Tomsk', [1, 0, 0])]
        self.assertEqual(fit_transform(cities), exp_transformed_cities)

    def test_numbers_eq(self):
        numbers = [1, 2, 4, 35, 2313, 1, 35, 2313]
        exp_transformed_numbers = [(1, [0, 0, 0, 0, 1]),
                                   (2, [0, 0, 0, 1, 0]),
                                   (4, [0, 0, 1, 0, 0]),
                                   (35, [0, 1, 0, 0, 0]),
                                   (2313, [1, 0, 0, 0, 0]),
                                   (1, [0, 0, 0, 0, 1]),
                                   (35, [0, 1, 0, 0, 0]),
                                   (2313, [1, 0, 0, 0, 0])]
        self.assertEqual(fit_transform(numbers), exp_transformed_numbers)

    def test_joke_not_in(self):
        joke = ['1', 1]
        wrong_result = (1, [0, 1])
        self.assertNotIn(wrong_result, fit_transform(joke))

    def test_is_list(self):
        self.assertIsInstance(fit_transform(['Moscow']), List)

    def test_exceptions(self):
        with self.assertRaises(TypeError):
            fit_transform()
