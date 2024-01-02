import allure
import pytest
from selenium.common.exceptions import TimeoutException
from ui_automation.pages.units_convert import UnitsPage

load_timeout = 5


@allure.description("The tests check the conversion from celsius to fahrenheit")
@pytest.mark.parametrize("celsius_input, expected_fahrenheit", [
    (30, "86.00000°F"), (0, "32.00000°F"), (-1, "30.20000°F")],
                         ids=["30C to Fahrenheit", "0C to Fahrenheit", "-1C to Fahrenheit"])
def test_celsius_to_fahrenheit_conversion(setup, celsius_input, expected_fahrenheit):
    driver = setup
    # This is a workaround because the webpage has an issue where it is continuously loading.
    driver.set_page_load_timeout(load_timeout)
    try:
        # Try to open the page
        driver.get("https://www.metric-conversions.org/temperature/celsius-to-fahrenheit.htm")
    except TimeoutException:
        # If the page load times out, stop the loading of the page
        driver.execute_script("window.stop();")
    temperature_page = UnitsPage(driver)
    temperature_page.convert_celsius_to_fahrenheit(celsius_input)
    result_f = temperature_page.get_convert_result()
    assert result_f.split('=')[1].strip() == expected_fahrenheit


@allure.description("The tests check the conversion from meters to feet")
@pytest.mark.parametrize("meter_input, expected_feet", [
    (50, "164ft"), (1000, "3280ft"), (0, "0ft")],
                         ids=["50 Meters to Feet", "1000 Meters to Feet", "0 Meters to Feet"])
def test_meters_to_feet_conversion(setup, meter_input, expected_feet):
    driver = setup
    # This is a workaround because the webpage has an issue where it is continuously loading.
    driver.set_page_load_timeout(load_timeout)
    try:
        # Try to open the page
        driver.get("https://www.metric-conversions.org/length/meters-to-feet.htm")
    except TimeoutException:
        # If the page load times out, stop the loading of the page
        driver.execute_script("window.stop();")
    temperature_page = UnitsPage(driver)
    temperature_page.convert_celsius_to_fahrenheit(meter_input)
    result_f = temperature_page.get_convert_result()
    assert result_f.split()[1] == expected_feet


@allure.description("The tests check the conversion from ounces to grams")
@pytest.mark.parametrize("meter_input, expected_feet", [
    (10, "283.4952g"), (99, "2806.603g"), (999, "28321.17g")],
                         ids=["50 Meters to Feet", "1000 Meters to Feet", "0 Meters to Feet"])
def test_ounces_to_grams_conversion(setup, meter_input, expected_feet):
    driver = setup
    # This is a workaround because the webpage has an issue where it is continuously loading.
    driver.set_page_load_timeout(load_timeout)
    try:
        # Try to open the page
        driver.get("https://www.metric-conversions.org/weight/ounces-to-grams.htm")
    except TimeoutException:
        # If the page load times out, stop the loading of the page
        driver.execute_script("window.stop();")
    temperature_page = UnitsPage(driver)
    temperature_page.convert_celsius_to_fahrenheit(meter_input)
    result_f = temperature_page.get_convert_result()
    assert result_f.split('=')[1].strip() == expected_feet
