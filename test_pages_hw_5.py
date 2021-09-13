from selenium.webdriver import Chrome
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from functions import login, success_alert_is_present, element_is_present
from selenium.webdriver.support import expected_conditions as ec


def test_wait_page():
    with Chrome() as browser:
        browser.get("https://qastand.valhalla.pw/wait")
        browser.maximize_window()
        login(browser)
        wait = WebDriverWait(browser, 10, poll_frequency=0.1)
        button = wait.until(ec.element_to_be_clickable((By.CLASS_NAME, "button")))
        wait.until(ec.text_to_be_present_in_element((By.ID, "demo"), '100'))
        button.click()
        success_alert_is_present(browser, timeout=10)


def test_slow_load():
    with Chrome() as browser:
        browser.get("https://qastand.valhalla.pw/slow_load")
        browser.maximize_window()
        login(browser)
        wait = WebDriverWait(browser, 10)
        input_text = wait.until(ec.visibility_of_element_located((By.ID, "text_input")))
        input_text.send_keys("test")
        wait.until(ec.element_to_be_clickable((By.CLASS_NAME, 'button'))).click()

        assert element_is_present(browser, By.CSS_SELECTOR, '.is-success'), "Необходимый текст отсутствует"
        text = browser.find_element(By.CSS_SELECTOR, '.is-success').text
        assert text == "Успех.", f"Неверный текст: {text}"
        browser.refresh()
        assert not element_is_present(browser, By.CSS_SELECTOR, '.is-success'), "Необходимый текст отсутствует"


def test_navigation():
    with Chrome() as browser:
        browser.get("https://qastand.valhalla.pw/profile")
        browser.maximize_window()
        login(browser)
        browser.find_element(By.XPATH, './/ul/li[2]/*[@class="navbar-item"]').click()
        wait = WebDriverWait(browser, 5)
        wait.until(ec.url_to_be('https://qastand.valhalla.pw/my_pet'))
        browser.refresh()
        assert wait.until(ec.title_is('Course Test Stand')), "Заголовок страницы не равен 'Course Test Stand'"

