from locators import NavigationLocators, ConstructorLocators, OrderLocators, TapeOfOrders
from pages.base_page import BasePage


class TapePage(BasePage):

    def collect_order_numbers(self):
        order_numbers = self.driver.find_elements(*TapeOfOrders.ORDERNUMBERS)
        list_of_numbers = []
        for i in order_numbers:
            list_of_numbers.append(i.text)
        return list_of_numbers

