import allure

class TestLogo:

    def test_click_yandex_logo_go_to_yandex_main_page(self, logo, driver):
        driver.get("https://qa-scooter.praktikum-services.ru/")
        logo.click_yandex_logo(driver)
        driver.quit()

    def test_click_scooter_logo_go_to_scooter_main_page(self, logo, driver):
        driver.get("https://qa-scooter.praktikum-services.ru/order")
        logo.click_scooter_logo(driver)
        driver.quit()