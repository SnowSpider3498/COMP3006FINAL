import unittest
from refactor_data import *
import get_data
from data_manipulation import *
from main import *

class TestMain(unittest.TestCase):
    def test_print(self):
        
  
class TestSeaTemps(unittest.TestCase):
    def test_iterable(self):
        iter(get_data.SeaTemps())

    def test_get_data(self):
        # make sure the website returns a status code
        self.assertTrue(get_data.SeaTemps().response == 200)


class TestDataManipulation(unittest.TestCase):
    def test_data_manipulation(self):
        pass


if __name__ == '__main__':
    unittest.main()
