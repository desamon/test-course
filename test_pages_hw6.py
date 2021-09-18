from selenium.webdriver import Chrome, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


from functions import login, wait_until_visible, check_alert_is_present, wait_until_clickable


def test_new_window():
    with Chrome() as browser:
        login(browser)
        browser.get("https://qastand.valhalla.pw/new_window_button")
        browser.maximize_window()

        assert len(browser.window_handles) == 1, "Открыто более 1 вкладки"

        wait_until_visible (browser, (By.CLASS_NAME, "button")).click()
        windows = browser.window_handles
        browser.switch_to.window(windows[1])

        assert len(browser.window_handles) == 2, "Открыто не 2 вкладки"

        wait_until_visible(browser, (By.CLASS_NAME, "button")).click()
        check_alert_is_present(browser, timeout=10)
        browser.switch_to.alert.accept() #переключаемся на алерт и принимаем его

        assert len(browser.window_handles) == 1, "Открыто более 1 вкладки"


def test_modal_windows():
    with Chrome() as browser:
        login(browser)
        browser.get("https://qastand.valhalla.pw/three_buttons")
        browser.maximize_window()
        wait_until_visible(browser, (By.XPATH, '//button[text()="Confirm"]')).click()
        alert = WebDriverWait(browser, 5).until(ec.alert_is_present())
        confirm = browser.switch_to.alert.dismiss() #нажимаем "отмену" в алерте
        assert (wait_until_visible(browser, (By.ID, "confirm_text"))).text == "Не запускаем", "Текст не отобразился"


def test_iframe_page():
    with Chrome() as browser:
        login(browser)
        browser.get("https://qastand.valhalla.pw/iframe_page")
        browser.maximize_window()
        browser.switch_to.frame(browser.find_element(By.NAME, "iframe")) #переключение на фрейм

        assert wait_until_visible(browser, (By.ID, "photo")), "Картинки нет на странице"

        wait_until_visible(browser, (By.CLASS_NAME, "button")).click()
        alert = WebDriverWait(browser, 5).until(ec.alert_is_present())
        browser.switch_to.alert.accept() #переключаемся на алерт и принимаем его
        browser.switch_to.default_content() #возврат на основную страницу


def test_drag_and_drop_page():
    with Chrome() as browser:
        login(browser)
        browser.get("https://qastand.valhalla.pw/drag_and_drop_page")
        browser.maximize_window()
        koala_to_drag = wait_until_clickable(browser, (By.ID, "draggable"))
        element_to_drop = wait_until_clickable(browser, (By.ID, "droppable"))
        ActionChains(browser).drag_and_drop(koala_to_drag, element_to_drop).perform()
        assert (wait_until_clickable(browser, (By.ID, "droppable"))).text == "Успех!", "Текст не появился"

