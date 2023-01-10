from pages.landing_page import LandingPage

class TestLogoLandingPage:

    def test_click_yandex_logo_go_to_yandex_main_page(self, driver):
        landing_page = LandingPage()
        landing_page.click_yandex_logo(driver)
        assert "dzen" in driver.current_url

    def test_click_scooter_logo_go_to_scooter_main_page(self, driver):
        driver.get("https://qa-scooter.praktikum-services.ru/order")
        landing_page = LandingPage()
        landing_page.click_scooter_logo(driver)
        assert driver.current_url == 'https://qa-scooter.praktikum-services.ru/'
