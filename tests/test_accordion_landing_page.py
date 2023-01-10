from pages.landing_page import LandingPage

class TestAccordionLandingPage:

    def test_accordion_element_1_click_text_shown(self, driver):
        landing_page = LandingPage()
        landing_page.click_accordion_element(driver, 0)
        assert landing_page.check_accordion_panel_is_shown(driver, 0)

    def test_accordion_element_2_click_text_shown(self, driver):
        landing_page = LandingPage()
        landing_page.click_accordion_element(driver, 1)
        assert landing_page.check_accordion_panel_is_shown(driver, 1)

    def test_accordion_element_3_click_text_shown(self, driver):
        landing_page = LandingPage()
        landing_page.click_accordion_element(driver, 2)
        assert landing_page.check_accordion_panel_is_shown(driver, 2)

    def test_accordion_element_4_click_text_shown(self, driver):
        landing_page = LandingPage()
        landing_page.click_accordion_element(driver, 3)
        assert landing_page.check_accordion_panel_is_shown(driver, 3)

    def test_accordion_element_5_click_text_shown(self, driver):
        landing_page = LandingPage()
        landing_page.click_accordion_element(driver, 4)
        assert landing_page.check_accordion_panel_is_shown(driver, 4)

    def test_accordion_element_6_click_text_shown(self, driver):
        landing_page = LandingPage()
        landing_page.click_accordion_element(driver, 5)
        assert landing_page.check_accordion_panel_is_shown(driver, 5)

    def test_accordion_element_7_click_text_shown(self, driver):
        landing_page = LandingPage()
        landing_page.click_accordion_element(driver, 6)
        assert landing_page.check_accordion_panel_is_shown(driver, 6)

    def test_accordion_element_8_click_text_shown(self, driver):
        landing_page = LandingPage()
        landing_page.click_accordion_element(driver, 7)
        assert landing_page.check_accordion_panel_is_shown(driver, 7)

