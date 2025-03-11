from _pytest.fixtures import fixture
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from helper import random_string_creation

@fixture()
def driver():
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(4)
    yield driver

    driver.close()


@fixture()
def wait(driver):
    wait = WebDriverWait(driver, 5)
    yield wait


@fixture()
def user_data():
    user_name = random_string_creation()
    user_email = user_name + "@gmail.com"
    user_pass = random_string_creation()
    user_dictionary = {"name": user_name, "email": user_email, "password": user_pass}

    yield user_dictionary


