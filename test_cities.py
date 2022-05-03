import imp
import unittest
from city_functions import city_country

class FullInfoTestCase(unittest.TestCase):
    def correct_info_test(self):
        
        place_info = city_country('Wroclaw', 'Poland')
        self.assertEqual(place_info, 'Wroclaw, Poland')

    def correct_whole_info_test(self):
        place_info = city_country('Wroclaw', 'Poland', 2_000_000)
        self.assertEqual(place_info, 'Wroclaw, Poland - populacja 2000000')

if __name__ == '__main__':
    unittest.main()