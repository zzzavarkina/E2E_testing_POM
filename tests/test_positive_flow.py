from pages.test_sets import test_set_1, test_set_2
import allure

class TestPositiveFlow:

    driver = None

    def test_positive_flow_via_upbutton_click_order_placed(self, test_flow, driver):
        driver.get("https://qa-scooter.praktikum-services.ru/")
        test_flow.click_upbutton(driver)
        test_flow.for_whom_this_scooter_form_feel(driver, test_set_1)
        test_flow.about_rent_form_feel(driver, test_set_1)
        driver.quit()

    def test_positive_flow_via_downbutton_click_order_placed(self, test_flow, driver):
        driver.get("https://qa-scooter.praktikum-services.ru/")
        test_flow.click_downbutton(driver)
        test_flow.for_whom_this_scooter_form_feel(driver, test_set_2)
        test_flow.about_rent_form_feel(driver, test_set_1)
        driver.quit()