import requests, os
from dotenv import dotenv_values

class Weather:

    API_KEY = 'key=' + dotenv_values("credentials.env")['KEY']
    API_METHOD = '/forecast.json'
    BASE_URL = 'http://api.weatherapi.com/v1'
      
    @staticmethod
    def search(url):
        return requests.get(url, headers={'User-Agent': 'Mozilla'}).json()
    
    
    @classmethod
    def get_weather_info(cls, city):
        url = cls.BASE_URL + cls.API_METHOD + '?' + cls.API_KEY + '&q=' + city
        weather_info = cls.search(url)
        os.system('wget ' + weather_info['current']['condition']['icon'][2:] + ' -O ./images/weather_icon.png')
        return weather_info

