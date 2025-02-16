import time

import pytest

from pages.auth_page import AuthPage
from pages.registration_page import RegistrationPage
from tests.conftest import user_data
from tests.profile_page import ProfilePage


#@pytest.mark.usefixtures("registration")
def test_check_correct_login(user_data, driver, wait):
    RegistrationPage(driver, wait).registration(user_data)
    page = AuthPage(driver, wait)
    page.open_base_page()
    page.click_profile()
    page.insert_login(user_data["email"])
    page.insert_password(user_data["password"])
    page.press_enter_button()
    page1 = ProfilePage(driver, wait)
    assert user_data["name"] == page1.name_check(user_data["name"])
    assert user_data["email"] == page1.email_check(user_data["email"])

