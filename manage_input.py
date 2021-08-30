import requests

class InputData:
    def __init__(self, difficulty="medium"):
        self.URL = self.URL = "https://sugoku.herokuapp.com/board"

        p = {'difficulty': difficulty}
        r = requests.get(url=self.URL, params=p)
        data = r.json()
        self.board = data['board']