from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class LandingPage:

    accordion_h1 = [By.XPATH, "//div[@class='Home_Header__iJKdX']"]
    accordion_item = [By.XPATH, "//div[@class='accordion__item']"]
    accordion_button = [By.XPATH, "//div[@class='accordion__button']"]
    accordion_heading = [[By.XPATH, "//div[@id='accordion__heading-0']"], [By.XPATH, "//div[@id='accordion__heading-1']"], [By.XPATH, "//div[@id='accordion__heading-2']"], [By.XPATH, "//div[@id='accordion__heading-3']"], [By.XPATH, "//div[@id='accordion__heading-4']"], [By.XPATH, "//div[@id='accordion__heading-5']"], [By.XPATH, "//div[@id='accordion__heading-6']"], [By.XPATH, "//div[@id='accordion__heading-7']"]]
    accordion_panel = [[By.XPATH, "//div[@id='accordion__panel-0']"], [By.XPATH, "//div[@id='accordion__panel-1']"], [By.XPATH, "//div[@id='accordion__panel-2']"], [By.XPATH, "//div[@id='accordion__panel-3']"], [By.XPATH, "//div[@id='accordion__panel-4']"], [By.XPATH, "//div[@id='accordion__panel-5']"], [By.XPATH, "//div[@id='accordion__panel-6']"], [By.XPATH, "//div[@id='accordion__panel-7']"]]
    accordion_exp_panel = [By.XPATH, "//div[@aria-expanded='true']"]
    accordion_h2 = [By.XPATH, "//div[@class='Home_FourPart__1uthg']/div[@class='Home_SubHeader__zwi_E']"]
    yandex_logo = [By.XPATH, "//a[@class='Header_LogoYandex__3TSOI']"]
    scooter_logo = [By.XPATH, "//a[@class='Header_LogoScooter__3lsAR']"]
    scooter_main_page_header = [By.XPATH, "//div[@class='Home_Header__iJKdX']"]
    yandex_main_page_header = [By.XPATH, "//header[@class='dzen-header-desktop__header-ST']"]


    def click_accordion_element(self, driver, element_index):
        driver.execute_script("arguments[0].scrollIntoView();", driver.find_element(*self.accordion_heading[element_index]))
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(self.accordion_heading[element_index]))
        driver.find_elements(*self.accordion_item)[element_index].click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(self.accordion_exp_panel))

    def check_accordion_panel_is_shown(self, driver, element_index):
        return driver.find_element(*self.accordion_panel[element_index]).is_displayed()

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

