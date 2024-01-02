from selenium.webdriver.common.by import By
from ui_automation.utils.base_page import BasePage


class UnitsPage(BasePage):
    input_celsius = (By.XPATH, "//input[@id = 'argumentConv']")
    result_of_convert = (By.XPATH, "//p[@id = 'answer']")

    def convert_celsius_to_fahrenheit(self, value):
        self.wait_until_element_located_send_text(self.input_celsius, value, 15)

    def get_convert_result(self):
        return self.wait_until_element_visibility_get_text(self.result_of_convert, 10)
