import time
from urllib import request

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import pytest

from pages.auth_page import AuthPage
from pages.registration_page import RegistrationPage
from tests.conftest import user_data
from tests.constructor_page import ConstructorPage


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
    time.sleep(5)













