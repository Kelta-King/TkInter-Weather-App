import json
import os
from traceback import print_tb

class History:

    def __init__(self, city, weather) -> None:
        self.city = city
        self.weather = weather
    
    def save(self):
        obj = {
            "city" : self.city,
            "weather" : self.weather
        }

        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__), "history.json"))
        history = str()

        file = open(__location__, "r+")

        history = json.loads(file.read())
        history.append(obj)
        history = json.dumps(history)

        # Changes pointer to 0
        file.seek(0)
        file.write(history)
        file.close()
