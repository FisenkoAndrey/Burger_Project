import time

from pages.auth_page import AuthPage


def test_redirect_to_authorization(driver, wait):
    page = AuthPage(driver, wait)
    page.open_base_page()
    page.click_profile()
    time.sleep(10)

    assert page.url == page.get_current_url()
