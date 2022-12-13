import pytest
from pages.test_sets import test_set_1, test_set_2
from pages.order_page import OrderPage


class TestOrderPage:

    @pytest.mark.parametrize("test_set", [test_set_1, test_set_2])
    def test_order_page_via_upbutton_click_order_placed(self, driver, test_set):
        order_page = OrderPage()
        order_page.click_upbutton(driver)
        order_page.for_whom_this_scooter_form_feel(driver, test_set)
        order_page.about_rent_form_feel(driver, test_set)
        assert order_page.is_order_complete(driver)

    @pytest.mark.parametrize("test_set", [test_set_1, test_set_2])
    def test_order_page_via_downbutton_click_order_placed(self, driver, test_set):
        order_page = OrderPage()
        order_page.click_downbutton(driver)
        order_page.for_whom_this_scooter_form_feel(driver, test_set)
        order_page.about_rent_form_feel(driver, test_set)
        assert order_page.is_order_complete(driver)
