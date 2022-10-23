import os
from dotenv import load_dotenv
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from pages.positive_flow import PositiveFlow
from pages.accordion_element import AccordionElement
from pages.logo import Logo

load_dotenv('../.env')

@pytest.fixture()
def accordion():
    accordion = AccordionElement()
    return accordion

@pytest.fixture()
def test_flow():
    test_flow = PositiveFlow()
    return test_flow

@pytest.fixture()
def logo():
    logo = Logo()
    return logo

@pytest.fixture()
def driver():
    options = Options()
    options.binary_location = os.getenv('FIREFOX_PATH')
    driver = webdriver.Firefox(executable_path=os.getenv('GECKODRIVER_PATH'), options=options)
    return driver

@pytest.fixture(scope="class")
def driver_for_class():
    options = Options()
    options.binary_location = os.getenv('FIREFOX_PATH')
    driver_for_class = webdriver.Firefox(executable_path=os.getenv('GECKODRIVER_PATH'), options=options)
    driver_for_class.get("https://qa-scooter.praktikum-services.ru/")
    return driver_for_class