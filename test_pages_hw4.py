from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from functions import login, element_is_present, wait_until_clickable, wait_until_present
from selenium.webdriver.common.by import By
import os


def test_about_myself_page():
   with Chrome() as browser:
       browser.get("https://qastand.valhalla.pw/about")
       browser.maximize_window()
       login(browser)
       placeholder_name = wait_until_clickable(browser, By.NAME, "name").send_keys("Имя")
       wait_until_clickable(browser, By.NAME, "surname").send_keys("Фамилия")
       assert wait_until_clickable(browser, By.ID, "age1").get_attribute("checked"), "Радиобаттон по умолчанию не включен"
       wait_until_clickable(browser, By.ID, "age2").click()
       wait_until_clickable(browser, By.ID, "lang1").click() #выбираем Python
       wait_until_clickable(browser, By.ID, "lang4").click() #выбираем Go
       Select(wait_until_clickable(browser, By.TAG_NAME, "select")).select_by_index(4)  # выбираем Senior
       placeholder_name = wait_until_clickable(browser, By.NAME, "name").send_keys(Keys.ENTER) #ENTER в "Имя"

       assert element_is_present(browser, By.CSS_SELECTOR, '.is-success'), "Необходимый текст отсутствует"

       text = wait_until_clickable(browser, By.CSS_SELECTOR, '.is-success').text

       assert text == "Успех.", f"Неверный текст: {text}"


def test_upload_file():
    with Chrome() as browser:
        browser.get("https://qastand.valhalla.pw/upload_file")
        browser.maximize_window()
        login(browser)
        element_for_upload = wait_until_present(browser, By.CSS_SELECTOR, '[type="file"]')
        element_for_upload.send_keys(os.path.join(os.getcwd(), 'resources', 'koala.jpg'))
        wait_until_clickable(browser, By.CLASS_NAME, "button").click()
        assert element_is_present(browser, By.CSS_SELECTOR, '.is-success'), "Необходимый текст отсутствует"
        text = wait_until_clickable(browser, By.CSS_SELECTOR, '.is-success').text

        assert text == "Успех", f"Неверный текст: {text}"
        browser.refresh()
        assert not element_is_present(browser, By.CSS_SELECTOR, '.is-success'), "Необходимый текст отсутствует"


