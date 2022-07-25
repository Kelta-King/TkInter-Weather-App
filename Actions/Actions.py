import requests
import json
from Database import History as h

class Actions:

    def __init__(self, apiId) -> None:
        self.apiId = apiId

    def getWeather(self, city):
        try:
            url = "http://api.openweathermap.org/data/2.5/weather?appid=" + self.apiId + "&q=" + city        
            res = requests.get(url)
            if(res.status_code != 200):
                return "Incorrect", "-", "-"
            
            res.close()
            res = json.loads(res.content)
            temp_h = h.History(res["name"], str(str(int(res["main"]["temp"])-273)+" C"))
            temp_h.save()

            return res["name"], str(int(res["main"]["temp"])-273)+" °C", res["weather"][0]["main"]
            
        except Exception as ex:
            print(ex)
            return "Incorrect", "-", "-"
        