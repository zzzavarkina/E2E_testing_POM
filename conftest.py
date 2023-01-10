import os
import pytest
from dotenv import load_dotenv
from selenium.webdriver.firefox.options import Options
from selenium import webdriver


load_dotenv('../.env')

@pytest.fixture()
def driver():
    options = Options()
    options.binary_location = os.getenv('FIREFOX_PATH')
    driver = webdriver.Firefox(executable_path=os.getenv('GECKODRIVER_PATH'), options=options)
    driver.get("https://qa-scooter.praktikum-services.ru/")
    yield driver
    driver.quit()