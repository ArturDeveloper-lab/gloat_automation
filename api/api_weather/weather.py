import requests


class WeatherApiClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.weather_url = "http://api.openweathermap.org/data/2.5/weather"
        self.forecast_url = "http://api.openweathermap.org/data/2.5/forecast"

    def get_weather_by_zipcode(self, zipcode, country_code):
        params = {
            'zip': f"{zipcode},{country_code}",
            'appid': self.api_key,
            'units': 'imperial'  # This will request the temperature in Fahrenheit
        }
        response = requests.get(self.weather_url, params=params)
        return response.json(), response.status_code

    def get_forecast_by_zipcode(self, zipcode, country_code):
        params = {
            'zip': f"{zipcode},{country_code}",
            'appid': self.api_key,
            'units': 'imperial'
        }
        response = requests.get(self.forecast_url, params=params)
        return response.json(), response.status_code


