import allure

from pages.auth_page import AuthPage
from pages.registration_page import RegistrationPage
from pages.profile_page import ProfilePage

@allure.feature("Ссылка регистрации")
@allure.story("Пользователь кликает на ссылку регистрации")
@allure.tag("auth", "positive")
@allure.severity(allure.severity_level.CRITICAL)
def test_redirect_to_registration(driver, wait):
    page = AuthPage(driver, wait)
    page.open_base_page()
    page.click_profile()
    page.click_registration()

    assert RegistrationPage.url == page.get_current_url()

@allure.feature("Регистрация")
@allure.story("Пользователь регистрируется на сайте")
@allure.tag("auth", "positive")
@allure.severity(allure.severity_level.CRITICAL)
def test_registration(driver,wait, user_data):
    reg_page = RegistrationPage(driver, wait)
    page = AuthPage(driver, wait)
    page.open_base_page()
    page.click_profile()
    page.click_registration()
    reg_page.input_name(user_data["name"])
    reg_page.input_email(user_data["email"])
    reg_page.input_password(user_data["password"])
    reg_page.press_button()
    page1 = ProfilePage(driver, wait)
    page.click_profile()
    # print(user_data["name"])
    # print(user_data["password"])
    # print(page1.value_retrieve())
    # print(page1.email_retrieve())


    assert False  # assert user_data["name"] == page1.name_check(user_data["name"])

    assert user_data["email"] == page1.email_check(user_data["email"])







