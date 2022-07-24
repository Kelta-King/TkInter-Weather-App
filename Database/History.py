from datetime import date
import os
from traceback import print_tb

class History:

    def __init__(self, city, weather) -> None:
        self.city = city
        self.weather = weather
    
    def save(self):

        try:
            obj = str(date.today()) + "," + self.city + "," + self.weather
            __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__), "history.csv"))
            history = str()

            file = open(__location__, "a")
            file.write("\n")
            file.write(obj)
            file.close()

            return True

        except Exception as ex:
            print(ex)
            return False

    def getHistory(self):
        try:
            __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__), "history.csv"))
            history = str()

            file = open(__location__, "r")
            return file.read()
            
        except Exception as ex:
            print(ex)
            return False