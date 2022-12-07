from pages.landing_page import LandingPage
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

load_dotenv('../.env')

class TestAccordionLandingPage:

    driver = None

    @classmethod
    def setup_class(cls):
        options = Options()
        options.binary_location = os.getenv('FIREFOX_PATH')
        cls.driver = webdriver.Firefox(executable_path=os.getenv('GECKODRIVER_PATH'), options=options)
        cls.driver.get("https://qa-scooter.praktikum-services.ru/")

    def test_accordion_element_1_click_text_shown(self):
        landing_page = LandingPage(self.driver)
        landing_page.click_accordion_element(self.driver, 0)
        assert landing_page.check_accordion_panel_is_shown(self.driver, 0)

    def test_accordion_element_2_click_text_shown(self):
        landing_page = LandingPage(self.driver)
        landing_page.click_accordion_element(self.driver, 1)
        assert landing_page.check_accordion_panel_is_shown(self.driver, 1)

    def test_accordion_element_3_click_text_shown(self):
        landing_page = LandingPage(self.driver)
        landing_page.click_accordion_element(self.driver, 2)
        assert landing_page.check_accordion_panel_is_shown(self.driver, 2)

    def test_accordion_element_4_click_text_shown(self):
        landing_page = LandingPage(self.driver)
        landing_page.click_accordion_element(self.driver, 3)
        assert landing_page.check_accordion_panel_is_shown(self.driver, 3)

    def test_accordion_element_5_click_text_shown(self):
        landing_page = LandingPage(self.driver)
        landing_page.click_accordion_element(self.driver, 4)
        assert landing_page.check_accordion_panel_is_shown(self.driver, 4)

    def test_accordion_element_6_click_text_shown(self):
        landing_page = LandingPage(self.driver)
        landing_page.click_accordion_element(self.driver, 5)
        assert landing_page.check_accordion_panel_is_shown(self.driver, 5)

    def test_accordion_element_7_click_text_shown(self):
        landing_page = LandingPage(self.driver)
        landing_page.click_accordion_element(self.driver, 6)
        assert landing_page.check_accordion_panel_is_shown(self.driver, 6)

    def test_accordion_element_8_click_text_shown(self):
        landing_page = LandingPage(self.driver)
        landing_page.click_accordion_element(self.driver, 7)
        assert landing_page.check_accordion_panel_is_shown(self.driver, 7)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
