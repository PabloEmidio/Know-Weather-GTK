import requests
from dotenv import dotenv_values
from shutil import copyfileobj


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

        # download hours and days's icon
        for i in range(0, 5):
            if i in (1, 2):
                response_day_icon = requests.get('https://' + weather_info['forecast']['forecastday'][i]['hour'][current_hour]['condition']['icon'][2:], stream=True)
                with open(f'./images/days_icon/{i}.png', 'wb') as file:
                    copyfileobj(response_day_icon.raw, file)
            if current_hour+i>23:
                with open(f'./images/hour_icon/unavailable.png', 'rb') as unavailable_image:
                    with open(f'./images/hour_icon/{i+1}.png', 'wb') as file:
                        copyfileobj(unavailable_image, file)
            else:
                response_hour_icon = requests.get('https://' + weather_info['forecast']['forecastday'][0]['hour'][current_hour+i]['condition']['icon'][2:], stream=True)
                with open(f'./images/hour_icon/{i+1}.png', 'wb') as file:
                    copyfileobj(response_hour_icon.raw, file)
        return weather_info
    

