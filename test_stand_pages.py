from selenium.webdriver import Chrome
from functions import login, element_is_present, wait_until_present
from selenium.webdriver.common.by import By


def test_inputs_page():
    with Chrome() as browser:
        browser.get("https://qastand.valhalla.pw/inputs")
        browser.maximize_window()
        login(browser)
        wait_until_present(browser, By.CSS_SELECTOR, '[name="test"]').send_keys("Test")
        wait_until_present(browser, By.CSS_SELECTOR, '.button:nth-child(2)').click()
        text = wait_until_present(browser, By.CSS_SELECTOR, '.is-success').text

        assert element_is_present(browser, By.CSS_SELECTOR, '.is-success'), "Необходимый текст отсутствует"
        assert text == "Верно", f"Неверный текст: {text}"


def test_pet_page():
    with Chrome() as browser:
        browser.get("https://qastand.valhalla.pw/my_pet")
        browser.maximize_window()
        login(browser)
        wait_until_present(browser, By.NAME, "pet").send_keys("Кот")
        wait_until_present(browser, By.NAME, "name").send_keys("Семён")
        wait_until_present(browser, By.NAME, "age").send_keys("18")
        wait_until_present(browser, By.NAME, "sex").send_keys("Мужской")
        wait_until_present(browser, By.CSS_SELECTOR, '.button').click()
        text = wait_until_present(browser, By.XPATH, '//*[contains(text(), "Успех.")]').text
        assert element_is_present(browser, By.CSS_SELECTOR, '.is-success'), "Необходимый текст отсутствует"
        assert text == "Успех.", f"Неверный текст: {text}"


def test_pet_page_negativ():
    with Chrome() as browser:
        browser.get("https://qastand.valhalla.pw/my_pet")
        browser.maximize_window()
        login(browser)
        wait_until_present(browser, By.NAME, "pet").send_keys("Кот")
        wait_until_present(browser, By.CSS_SELECTOR, '.button').click()
        text = wait_until_present(browser, By.XPATH, '//*[contains(text(), "Заполнены не все поля.")]').text
        assert element_is_present(browser, By.CLASS_NAME, "notification"), "Необходимый текст отсутствует"
        assert text == "Заполнены не все поля.", f"Неверный текст: {text}"
        assert not element_is_present(browser, By.CSS_SELECTOR, '.is-success'), "Сообщение об успехе отображается"


def test_main_page():
    with Chrome() as browser:
        browser.get("https://qastand.valhalla.pw/")
        browser.maximize_window()
        wait_until_present(browser, By.CSS_SELECTOR, '#login').click()
        login(browser)
        page_name = ['Поля ввода и кнопки', 'Мой питомец', 'О себе', 'Загрузка файла', 'Ожидание', 'Медленная загрузка',
                     'Модальные окна', 'Новая вкладка', 'iframe', 'Drag-and-drop']
        page_name_1 = []
        elements = browser.find_elements(By.CSS_SELECTOR, '.menu-list>li .navbar-item')
        for i in elements:
            page_name_1.append(i.text)
        assert page_name == page_name_1, "Списки неодинаковые"
