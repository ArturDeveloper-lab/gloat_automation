import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def setup():
    options = Options()
    # options.headless = True
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.maximize_window()
    yield driver
    # Teardown code: runs after each tests
    driver.quit()
