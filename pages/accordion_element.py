from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class AccordionElement:

    accordion_h1 = [By.XPATH, "//div[@class='Home_Header__iJKdX']"]
    accordion_item = [By.XPATH, "//div[@class='accordion__item']"]
    accordion_button = [By.XPATH, "//div[@class='accordion__button']"]
    accordion_heading = [[By.XPATH, "//div[@id='accordion__heading-0']"], [By.XPATH, "//div[@id='accordion__heading-1']"], [By.XPATH, "//div[@id='accordion__heading-2']"], [By.XPATH, "//div[@id='accordion__heading-3']"], [By.XPATH, "//div[@id='accordion__heading-4']"], [By.XPATH, "//div[@id='accordion__heading-5']"], [By.XPATH, "//div[@id='accordion__heading-6']"], [By.XPATH, "//div[@id='accordion__heading-7']"]]
    accordion_panel = [[By.XPATH, "//div[@id='accordion__panel-0']"], [By.XPATH, "//div[@id='accordion__panel-1']"], [By.XPATH, "//div[@id='accordion__panel-2']"], [By.XPATH, "//div[@id='accordion__panel-3']"], [By.XPATH, "//div[@id='accordion__panel-4']"], [By.XPATH, "//div[@id='accordion__panel-5']"], [By.XPATH, "//div[@id='accordion__panel-6']"], [By.XPATH, "//div[@id='accordion__panel-7']"]]
    accordion_exp_panel = [By.XPATH, "//div[@aria-expanded='true']"]
    accordion_h2 = [By.XPATH, "//div[@class='Home_FourPart__1uthg']/div[@class='Home_SubHeader__zwi_E']"]


    def click_accordion_element(self, driver, element_index):
        driver.execute_script("arguments[0].scrollIntoView();", driver.find_element(*self.accordion_heading[element_index]))
        driver.find_elements(*self.accordion_item)[element_index].click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(self.accordion_exp_panel))

    def check_accordion_panel_is_shown(self, driver, element_index):
        return driver.find_element(*self.accordion_panel[element_index]).is_displayed()
