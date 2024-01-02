import pytest

# Adjust the import according to your project structure
from api.api_weather.weather import WeatherApiClient


@pytest.fixture(scope="session")
def weather_api_client():
    api_key = '8458b89402fdbe4a52ca303ec8676115'
    return WeatherApiClient(api_key)
