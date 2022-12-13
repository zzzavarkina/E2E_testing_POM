from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class OrderPage:

    order_upbutton = [By.XPATH, "//button[@class='Button_Button__ra12g']"]
    order_downbutton = [By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"]
    rent_form = [By.XPATH, "//div[@class='Order_Content__bmtHS']"]
    for_whom_this_scooter_header = [By.XPATH, "//div[@class='Order_Header__BZXOb']"]
    input_field = [By.XPATH, "//input[@class='Input_Input__1iN_Z Input_Responsible__1jDKN']"]
    metro_input_field = [By.XPATH, "//input[@class='select-search__input']"]
    metro_dropdown = [By.XPATH, "//div[@class='select-search__select']"]
    metro_dropdown_item = [By.XPATH, "//button[@class='Order_SelectOption__82bhS select-search__option']"]
    next_button = [By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"]
    about_rent_header = [By.XPATH, "//div[@class='Order_Header__BZXOb']"]
    calendar_field = [By.XPATH, "//input[@class='Input_Input__1iN_Z Input_Responsible__1jDKN']"]
    calendar_field_datepicker = [By.XPATH, "//div[@class='react-datepicker']"]
    calendar_field_datepicker_item = [By.CSS_SELECTOR, ".react-datepicker__day--today"]
    rent_period_dropdown = [By.XPATH, "//div[@class='Dropdown-control']"]
    rent_period_dropdown_menu = [By.XPATH, "//div[@class='Dropdown-menu' and @aria-expanded='true']"]
    rent_period_dropdown_menu_item = [By.XPATH, "//div[@class='Dropdown-option']"]
    scooter_color = [By.XPATH, "//div[@class='Order_Title__3EKne']"]
    scooter_color_checkbox_label_black = [By.CSS_SELECTOR, "label[for='black']"]
    scooter_color_checkbox_label_grey = [By.CSS_SELECTOR, "label[for='grey']"]
    scooter_color_checkbox = [By.XPATH, "//input[@class='Checkbox_Input__14A2w']"]
    comment_field = [By.XPATH, "//input[@class='Input_Input__1iN_Z Input_Responsible__1jDKN']"]
    place_order_button = [By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"]
    modal_window = [By.XPATH, "//div[@class='Order_Modal__YZ-d3']"]
    modal_header = [By.XPATH, "//div[@class='Order_ModalHeader__3FDaJ']"]
    modal_back_button = [By.XPATH, "//button[@class='more Button_Button__ra12g Button_Middle__1CSJM Button_Inverted__3IF-i']"]
    modal_yes_button = [By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"]
    modal_ok_status = [By.XPATH, "//div[@class='Order_ModalHeader__3FDaJ']"]
    cookie_window = [By.XPATH, "//div[@class='App_CookieConsent__1yUIN']"]
    cookie_button = [By.XPATH, "//div[@class='App_CookieConsent__1yUIN']//button[@id='rcc-confirm-button']"]

    test_set = {}

    def click_upbutton(self, driver):
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(self.cookie_window))
        driver.find_element(*self.cookie_button).click()
        driver.find_element(*self.order_upbutton).click()

    def click_downbutton(self, driver):
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(self.cookie_window))
        driver.find_element(*self.cookie_button).click()
        driver.find_element(*self.order_downbutton).click()

    def for_whom_this_scooter_form_feel(self, driver, test_set):
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(self.for_whom_this_scooter_header))
        input_fields = driver.find_elements(*self.input_field)
        input_fields[0].send_keys(test_set['Имя'])
        input_fields[1].send_keys(test_set['Фамилия'])
        input_fields[2].send_keys(test_set['Адрес'])
        driver.find_element(*self.metro_input_field).send_keys(test_set['Станция метро'])
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(self.metro_dropdown))
        driver.find_element(*self.metro_dropdown_item).click()
        input_fields[3].send_keys(test_set['Телефон'])
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(self.next_button)).click()

    def about_rent_form_feel(self, driver, test_set):
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(self.about_rent_header))
        driver.find_element(*self.calendar_field).click()
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(self.calendar_field_datepicker))
        driver.find_element(*self.calendar_field_datepicker_item).click()
        driver.find_element(*self.rent_period_dropdown).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(self.rent_period_dropdown_menu))
        driver.find_element(*self.rent_period_dropdown_menu_item).click()
        driver.find_element(*self.scooter_color_checkbox_label_black).click()
        driver.find_element(*self.comment_field).send_keys(test_set['Комментарий'])
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(self.place_order_button)).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(self.modal_header))
        driver.find_elements(*self.modal_yes_button)[1].click()

    def is_order_complete(self, driver):
        return driver.find_element(*self.modal_ok_status).is_displayed()