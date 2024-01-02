from datetime import datetime, timedelta


def test_current_temperature(weather_api_client):
    zipcode = 20852
    country_code = 'US'
    response_data, status_code = weather_api_client.get_weather_by_zipcode(zipcode, country_code)
    assert status_code == 200, "API did not return a successful response"
    temperature = response_data['main']['temp']
    weather_main = response_data['weather'][0]['main']
    weather_description = response_data['weather'][0]['description']
    print("\n")
    print(f"Weather: {weather_main}, Description: {weather_description}]\n")
    print(f"Current temperature: {temperature}°F")


def test_current_temperature_negative_invalid_zip(weather_api_client):
    zipcode = 1111111  # Invalid zipcode
    country_code = 'US'
    response_data, status_code = weather_api_client.get_weather_by_zipcode(zipcode, country_code)
    assert status_code == 404, "API did not return the expected 404 response for an invalid request"


def test_current_temperature_negative_invalid_country_code(weather_api_client):
    zipcode = 20852
    country_code = 'bbbbb'  # Invalid country code
    response_data, status_code = weather_api_client.get_weather_by_zipcode(zipcode, country_code)
    assert status_code == 404, "API did not return the expected 404 response for an invalid request"


def test_temperature_within_range(weather_api_client, tolerance=10):
    zipcode = '20852'
    country_code = 'US'

    # Get current temperature
    current_weather, current_status = weather_api_client.get_weather_by_zipcode(zipcode, country_code)
    assert current_status == 200, "Failed to fetch current weather data"
    current_temp = current_weather['main']['temp']

    # Get tomorrow's forecast temperature
    forecast_data, forecast_status = weather_api_client.get_forecast_by_zipcode(zipcode, country_code)
    assert forecast_status == 200, "Failed to fetch forecast data"

    tomorrow = datetime.now() + timedelta(days=1)
    tomorrow_date = tomorrow.strftime('%Y-%m-%d')
    tomorrows_temp = None

    for entry in forecast_data['list']:
        if tomorrow_date in entry['dt_txt']:
            tomorrows_temp = entry['main']['temp']
            break

    # This is second solution to get tomorrows_temp
    # tomorrows_temperatures = [entry['main']['temp'] for entry in forecast_data['list'] if
    #                           tomorrow_date in entry['dt_txt']]
    #
    # # Get the first temperature from the list if it exists
    # tomorrows_temp = tomorrows_temperatures[0] if tomorrows_temperatures else None

    assert tomorrows_temp is not None, "Failed to fetch tomorrow's temperature"

    # Check if current temperature is within the tolerance range of tomorrow's temperature
    lower_bound = tomorrows_temp - (tomorrows_temp * tolerance / 100)
    upper_bound = tomorrows_temp + (tomorrows_temp * tolerance / 100)

    assert lower_bound <= current_temp <= upper_bound, "Current temperature is not within the 10% range" \
                                                       " of tomorrow's temperature"
