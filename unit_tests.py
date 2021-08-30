import unittest
from solver import Solver
import requests

class MyTestCase(unittest.TestCase):
    def __init__(self):
        self.URL = "https://sugoku.herokuapp.com/board"

    def easy(self):
        S = Solver()
        p = {'difficulty': 'easy'}
        r = requests.get(url=self.URL, params=p)
        data = r.json()
        print(data)
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
