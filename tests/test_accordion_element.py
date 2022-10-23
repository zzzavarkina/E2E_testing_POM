import allure

class TestAccordionElement:

    def test_accordion_element_1_click_text_shown(self, accordion, driver_for_class):
        accordion.click_accordion_element(driver_for_class, 0)
        assert accordion.check_accordion_panel_is_shown(driver_for_class, 0)

    def test_accordion_element_2_click_text_shown(self, accordion, driver_for_class):
        accordion.click_accordion_element(driver_for_class, 1)
        assert accordion.check_accordion_panel_is_shown(driver_for_class, 1)

    def test_accordion_element_3_click_text_shown(self, accordion, driver_for_class):
        accordion.click_accordion_element(driver_for_class, 2)
        assert accordion.check_accordion_panel_is_shown(driver_for_class, 2)

    def test_accordion_element_4_click_text_shown(self, accordion, driver_for_class):
        accordion.click_accordion_element(driver_for_class, 3)
        assert accordion.check_accordion_panel_is_shown(driver_for_class, 3)

    def test_accordion_element_5_click_text_shown(self, accordion, driver_for_class):
        accordion.click_accordion_element(driver_for_class, 4)
        assert accordion.check_accordion_panel_is_shown(driver_for_class, 4)

    def test_accordion_element_6_click_text_shown(self, accordion, driver_for_class):
        accordion.click_accordion_element(driver_for_class, 5)
        assert accordion.check_accordion_panel_is_shown(driver_for_class, 5)

    def test_accordion_element_7_click_text_shown(self, accordion, driver_for_class):
        accordion.click_accordion_element(driver_for_class, 6)
        assert accordion.check_accordion_panel_is_shown(driver_for_class, 6)

    def test_accordion_element_8_click_text_shown(self, accordion, driver_for_class):
        accordion.click_accordion_element(driver_for_class, 7)
        assert accordion.check_accordion_panel_is_shown(driver_for_class, 7)
        driver_for_class.quit()
