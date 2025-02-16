from locators import NavigationLocators, AuthPageLocators
from pages.base_page import BasePage


class AuthPage(BasePage):

    url = 'https://stellarburgers.ru/login'

    def click_registration(self):
        self.click(AuthPageLocators.REGISTRATIONLINK)

    def insert_login(self, email):
        self.input(AuthPageLocators.INPUTEMAIL, email)

    def insert_password(self, password):
        self.input(AuthPageLocators.INPUTPASSWORD, password)

    def press_enter_button(self):
        self.click(AuthPageLocators.PRESSBUTTON)

    def login(self, user_data):
        self.open_base_page()
        self.click_profile()
        self.insert_login(user_data["email"])
        self.insert_password(user_data["password"])
        self.press_enter_button()


