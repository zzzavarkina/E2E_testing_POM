from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import allure

class TestAccordionElement:

    driver = None

    @classmethod
    def setup_class(cls):
        options = Options()
        options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
        cls.driver = webdriver.Firefox(executable_path=r'C:\geckodriver\geckodriver.exe', options=options)
        cls.driver.get("https://qa-scooter.praktikum-services.ru/")

    def test_accordion_element_1_click_text_shown(self, accordion):
        accordion.click_accordion_element(self.driver, 0)
        assert accordion.check_accordion_panel_is_shown(self.driver, 0)

    def test_accordion_element_2_click_text_shown(self, accordion):
        accordion.click_accordion_element(self.driver, 1)
        assert accordion.check_accordion_panel_is_shown(self.driver, 1)

    def test_accordion_element_3_click_text_shown(self, accordion):
        accordion.click_accordion_element(self.driver, 2)
        assert accordion.check_accordion_panel_is_shown(self.driver, 2)

    def test_accordion_element_4_click_text_shown(self, accordion):
        accordion.click_accordion_element(self.driver, 3)
        assert accordion.check_accordion_panel_is_shown(self.driver, 3)

    def test_accordion_element_5_click_text_shown(self, accordion):
        accordion.click_accordion_element(self.driver, 4)
        assert accordion.check_accordion_panel_is_shown(self.driver, 4)

    def test_accordion_element_6_click_text_shown(self, accordion):
        accordion.click_accordion_element(self.driver, 5)
        assert accordion.check_accordion_panel_is_shown(self.driver, 5)

    def test_accordion_element_7_click_text_shown(self, accordion):
        accordion.click_accordion_element(self.driver, 6)
        assert accordion.check_accordion_panel_is_shown(self.driver, 6)

    def test_accordion_element_8_click_text_shown(self, accordion):
        accordion.click_accordion_element(self.driver, 7)
        assert accordion.check_accordion_panel_is_shown(self.driver, 7)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()