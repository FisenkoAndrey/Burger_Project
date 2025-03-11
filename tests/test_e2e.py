import time

from pages.registration_page import RegistrationPage
from pages.constructor_page import ConstructorPage
from pages.tape_page import TapePage


def test_bun_check(driver, wait):
    actual_value = "Детали ингредиента"
    page = ConstructorPage(driver, wait)
    page.open_base_page()
    page.click_bun()
    element_text = page.modal_window_value_check()
    assert actual_value == element_text


def test_profile_check(driver, wait):
    page = ConstructorPage(driver, wait)
    page.open_base_page()
    page.click_bun()
    page.close_window()
    assert page.profile_check()


def test_make_order(driver, wait, user_data):
    page = RegistrationPage(driver, wait)
    page.open_base_page()
    page.registration(user_data)
    page1 = ConstructorPage(driver, wait)
    page1.drag_and_drop_bun()
    page1.drag_and_drop_stuff()
    page1.click_order_button()
    order = page1.catch_order_number()
    page1.close_order_window()
    page1.click_tape_of_orders()
    page2 = TapePage(driver, wait)

    assert order in page2.collect_order_numbers()

















