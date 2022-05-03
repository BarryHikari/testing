import unittest
from name_function import get_formatted_name

class NameTestCase(unittest.TestCase):
    """Tests for name_function.py"""
    
    def test_first_last_name(self):
        """Is data like 'Will Smith' handled correctly?"""
        
        formatted_name = get_formatted_name('will', 'smith')
        self.assertEqual(formatted_name, 'Will Smith')
        
    def test_first_middle_last_name(self):
        formatted_name = get_formatted_name('Will', 'Smith', 'Carroll')
        self.assertEqual(formatted_name, 'Will Carroll Smith')

if __name__ == '__main__':
    unittest.main()