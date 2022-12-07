from pages.landing_page import LandingPage
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

load_dotenv('../.env')

class TestLogoLandingPage:

    driver = None

    @classmethod
    def setup_class(cls):
        options = Options()
        options.binary_location = os.getenv('FIREFOX_PATH')
        cls.driver = webdriver.Firefox(executable_path=os.getenv('GECKODRIVER_PATH'), options=options)

    def test_click_yandex_logo_go_to_yandex_main_page(self):
        self.driver.get("https://qa-scooter.praktikum-services.ru/")
        landing_page = LandingPage(self.driver)
        landing_page.click_yandex_logo(self.driver)
        assert "dzen" in self.driver.current_url

    def test_click_scooter_logo_go_to_scooter_main_page(self):
        self.driver.get("https://qa-scooter.praktikum-services.ru/order")
        landing_page = LandingPage(self.driver)
        landing_page.click_scooter_logo(self.driver)
        assert self.driver.current_url == 'https://qa-scooter.praktikum-services.ru/'

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()