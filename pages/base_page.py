from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seletools.actions import drag_and_drop
from locators import NavigationLocators, TapeOfOrders
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    BASE_URL = "https://stellarburgers.ru/"
    url = BASE_URL

    def __init__(self, driver: webdriver.Chrome, wait: WebDriverWait):
        self.driver = driver
        self.wait = wait

    def click(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator)).click()

    def open_base_page(self):
        self.driver.get(self.BASE_URL)

    def get_current_url(self):
        return self.driver.current_url

    def get_url(self):
        self.driver.get(self.url)

    def input(self, locator, keys):
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(keys)

    def text_retrieve(self, locator):
        element_text = self.wait.until(EC.visibility_of_element_located(locator)).text
        return element_text

    def value_retrieve(self, locator):
        value = self.wait.until(EC.visibility_of_element_located(locator)).get_attribute("value")
        return value

    def click_profile(self):
        self.click(NavigationLocators.PROFILE)

    def check_clickable(self, locator):
        return EC.element_to_be_clickable(locator)

    def drag_and_drop(self, obj_locator, to_obj_locator):
        obj = self.wait.until(EC.visibility_of_element_located(obj_locator))
        to_obj = self.wait.until(EC.visibility_of_element_located(to_obj_locator))
        ActionChains(self.driver).drag_and_drop(obj, to_obj).perform()

    def wait_until_element_visible_and_catch(self, locator):
        text = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locator)).text
        return text

    def click_tape_of_orders(self):
        self.click(TapeOfOrders.TAPE)
