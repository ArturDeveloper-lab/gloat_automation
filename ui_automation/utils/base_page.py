from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_until_element_located_click(self, element_by, time_out, scroll_to=False):
        element = WebDriverWait(self.driver, time_out).until(EC.presence_of_element_located(element_by))
        if scroll_to:
            self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'auto', block: 'center'});", element)
        return element.click()

    def wait_until_element_visibility_get_text(self, element_by, time_out):
        return str(WebDriverWait(self.driver, time_out).until(EC.visibility_of_element_located(element_by)).text)

    def wait_until_element_located_send_text(self, element_by, text: str, time_out: int):
        WebDriverWait(self.driver, time_out).until(EC.presence_of_element_located(element_by)).send_keys(text)


