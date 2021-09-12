from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from functions import login, element_is_present
from selenium.webdriver.common.by import By
import os


def test_about_myself_page():
   with Chrome() as browser:
       browser.get("https://qastand.valhalla.pw/about")
       browser.maximize_window()
       login(browser)
       placeholder_name = browser.find_element_by_name("name").send_keys("Имя")
       browser.find_element_by_name("surname").send_keys("Фамилия")
       assert browser.find_element(By.ID, "age1").get_attribute("checked"), "Радиобаттон по умолчанию не включен"
       browser.find_element(By.ID, "age2").click()
       browser.find_element(By.ID, "lang1").click() #выбираем Python
       browser.find_element(By.ID, "lang4").click() #выбираем Go
       Select(browser.find_element_by_tag_name("select")).select_by_index(4)  # выбираем Senior
       placeholder_name = browser.find_element_by_name("name").send_keys(Keys.ENTER) #ENTER в "Имя"

       assert element_is_present(browser, By.CSS_SELECTOR, '.is-success'), "Необходимый текст отсутствует"

       text = browser.find_element(By.CSS_SELECTOR, '.is-success').text

       assert text == "Успех.", f"Неверный текст: {text}"


def test_upload_file():
    with Chrome() as browser:
        browser.get("https://qastand.valhalla.pw/upload_file")
        browser.maximize_window()
        login(browser)
        element_for_upload = browser.find_element(By.CSS_SELECTOR, '[type="file"]')
        element_for_upload.send_keys(os.path.join(os.getcwd(), 'resources', 'koala.jpg'))
        browser.find_element(By.CLASS_NAME, "button").click()
        assert element_is_present(browser, By.CSS_SELECTOR, '.is-success'), "Необходимый текст отсутствует"
        text = browser.find_element(By.CSS_SELECTOR, '.is-success').text

        assert text == "Успех", f"Неверный текст: {text}"
        browser.refresh()
        assert not element_is_present(browser, By.CSS_SELECTOR, '.is-success'), "Необходимый текст отсутствует"


