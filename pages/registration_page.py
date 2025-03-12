from locators import NavigationLocators, RegistrationLocators
from pages.auth_page import AuthPage
from pages.base_page import BasePage
import allure


class RegistrationPage(BasePage):
    def fillout_profile(self):
        self.click(NavigationLocators.PROFILE)

    url = 'https://stellarburgers.ru/register'

    @allure.step("Вводим имя")
    def input_name(self, name):
        self.input(RegistrationLocators.NAME, name)

    @allure.step("Вводим email")
    def input_email(self, email):
        self.input(RegistrationLocators.EMAIL, email)

    @allure.step("Вводим пароль")
    def input_password(self, password):
        self.input(RegistrationLocators.PASSWORD, password)

    @allure.step("Нажать кнопку")
    def press_button(self):
        self.click(RegistrationLocators.BUTTON)

    @allure.step("Регистрация для других тестов, где необходиа регистрация")
    def registration(self, user_data):
        self.open_base_page()
        self.click_profile()
        AuthPage.click_registration(self)
        self.input_name(user_data["name"])
        self.input_email(user_data["email"])
        self.input_password(user_data["password"])
        self.press_button()

