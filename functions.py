from webbrowser import Chrome

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from typing import Tuple
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import Chrome


def login(browser):
    browser.get("https://qastand.valhalla.pw/login")
    browser.add_cookie({'name': 'session', 'value': '.eJwlzj0OwjAMQOG7ZGZwEjuOe5kq_hOsLZ0Qd6cSb3nr9yl7HnE-y_Y-rniU_eVlK4sgmouwWwoOncA6vCOzLVkgno0H1RaGnVARddSRlPe5SqU7bLDEFboQy1ScvoQMpjXvzINz5mwM1EPNuDdcXKFatVSKckOuM46_hsr3B2nILjw.YUXS4w.GVnihkZ93AsGahmx3pOHA_wulCY'})
    browser.refresh()


def wait_until_clickable(driver: Chrome, locator: Tuple, timeout: int = 5) -> WebElement:
    return WebDriverWait(driver, timeout).until(ec.element_to_be_clickable(locator))


def wait_until_present(driver: Chrome, locator: Tuple, timeout: int = 5) -> WebElement:
    return WebDriverWait(driver, timeout).until(ec.presence_of_element_located(locator))


def wait_until_visible(driver: Chrome, locator: Tuple, timeout: int = 5):
    return WebDriverWait(driver, timeout).until(ec.visibility_of_element_located(locator))


def element_is_present(browser: Chrome, locator: Tuple, timeout: int = 5) -> bool:
    try:
        wait_until_visible(browser, locator, timeout)
        return True
    except TimeoutException:
        return False


def check_alert_is_present(driver: Chrome, timeout=5) -> None:
    alert = WebDriverWait(driver, timeout).until(ec.alert_is_present())
    assert "Успех!" in alert.text, "Неправильный текст"
