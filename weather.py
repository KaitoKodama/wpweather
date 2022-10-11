import requests
import json


API_TOKEN = "3172d608ff6855d7ee988e8d57d1d1bc"


class WeatherSet:
    label: str = ""
    category: str = ""
    place: str = ""

    def __init__(self, label: str, category: str, place: str):
        self.label = label
        self.category = category
        self.place = place

    def request(self):
        response = requests.get(
            "https://api.openweathermap.org/data/2.5/weather",
            params={
                "q": self.place,
                "appid": API_TOKEN,
                "units": "metric",
                "lang": "ja",
            },
        )
        temp = json.loads(response.text)
        return temp
