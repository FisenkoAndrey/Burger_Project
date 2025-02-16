from exceptiongroup._suppress import BaseClass
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import ProfileLocators
from pages.base_page import BasePage


class ProfilePage(BasePage):
    def name_check(self, value):
        self.value_retrieve(ProfileLocators.PRPOFILENAME)
        return value

    def email_check(self, value):
        self.value_retrieve(ProfileLocators.PROFILEEMAIL)
        return value
