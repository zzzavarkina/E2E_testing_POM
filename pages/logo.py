from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class Logo:

    yandex_logo = [By.XPATH, "//a[@class='Header_LogoYandex__3TSOI']"]
    scooter_logo = [By.XPATH, "//a[@class='Header_LogoScooter__3lsAR']"]
    scooter_main_page_header = [By.XPATH, "//div[@class='Home_Header__iJKdX']"]
    yandex_main_page_header = [By.XPATH, "//header[@class='dzen-header-desktop__header-ST']"]

    def click_yandex_logo(self, driver):
        original_window = driver.current_window_handle
        assert len(driver.window_handles) == 1
        driver.find_element(*self.yandex_logo).click()
        WebDriverWait(driver, 10).until(expected_conditions.number_of_windows_to_be(2))
        for window_handle in driver.window_handles:
            if window_handle != original_window:
                driver.switch_to.window(window_handle)
                break
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(self.yandex_main_page_header))


    def click_scooter_logo(self, driver):
        driver.find_element(*self.scooter_logo).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(self.scooter_main_page_header))
