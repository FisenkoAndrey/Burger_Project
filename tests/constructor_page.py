from exceptiongroup._suppress import BaseClass
from locators import NavigationLocators, ConstructorLocators
from pages.base_page import BasePage


class ConstructorPage(BasePage):
    def click_bun(self):
        self.click(ConstructorLocators.BUN)

    def modal_window_value_check(self):
        element_text = self.text_retrieve(ConstructorLocators.MODALWINDOWNAME)
        return element_text

    def close_window(self):
        self.click(ConstructorLocators.WINDOWCLOSEBUTTON)

    def profile_check(self):
        return self.check_clickable(NavigationLocators.PROFILE)

    def drag_and_drop_bun(self):
        self.drag_and_drop(ConstructorLocators.BUN, ConstructorLocators.DROP)




