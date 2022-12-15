import unittest
from rk1 import *

class rk1_test(unittest.TestCase):
    
    def test_example_A1(self):
        expected_result = [
            ('Преступление и наказание', 70, 'Библиотека имени Достоевского'),
            ('Отцы и дети', 100, 'Библиотека имени Некрасова'), 
            ('Горе от ума', 150, 'Российская государственная библиотека'), 
            ('Евгений Онегин', 50, 'Российская государственная библиотека'), 
            ('Ревизор', 40, 'Российская национальная библиотека')
        ]
        result = example_A1(libraries, books)
        self.assertEqual(result, expected_result)
    
    def test_example_A2(self):
        expected_result = [
            ('Российская государственная библиотека', 200), 
            ('Библиотека имени Некрасова', 100), 
            ('Библиотека имени Достоевского', 70), 
            ('Российская национальная библиотека', 40)
        ]
        result = example_A2(libraries, books)
        self.assertEqual(result, expected_result)
    
    def test_example_A3(self):
        expected_result = {
            'Библиотека имени Достоевского': ['Преступление и наказание'], 
            'Библиотека имени Некрасова': ['Преступление и наказание'], 
            'Библиотека-читальня имени И.С. Тургенева': ['Отцы и дети'], 
            'Центральная библиотека имени Добролюбова': ['Евгений Онегин']
        }
        result = example_A3(libraries, books)
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()