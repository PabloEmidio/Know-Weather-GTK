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
    def get_weather_info(cls, city, /, current_hour=0):
        url = cls.BASE_URL + cls.API_METHOD + '?' + cls.API_KEY + '&q=' + city + '&days=3'
        weather_info = cls.search(url)
        os.system('wget ' + weather_info['current']['condition']['icon'][2:] + ' -O ./images/weather_icon.png')
        os.system('wget ' + weather_info['forecast']['forecastday'][0]['hour'][current_hour]['condition']['icon'][2:] + f' -O ./images/hour_icon/1.png')
        os.system('wget ' + weather_info['forecast']['forecastday'][0]['hour'][current_hour+1]['condition']['icon'][2:] + f' -O ./images/hour_icon/2.png')
        os.system('wget ' + weather_info['forecast']['forecastday'][0]['hour'][current_hour+2]['condition']['icon'][2:] + f' -O ./images/hour_icon/3.png')
        os.system('wget ' + weather_info['forecast']['forecastday'][0]['hour'][current_hour+3]['condition']['icon'][2:] + f' -O ./images/hour_icon/4.png')
        os.system('wget ' + weather_info['forecast']['forecastday'][0]['hour'][current_hour+4]['condition']['icon'][2:] + f' -O ./images/hour_icon/5.png')
        return weather_info

