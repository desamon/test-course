from selenium.webdriver import Chrome


def test_open_main_page():
    with Chrome() as driver:
        driver.get('https://qastand.valhalla.pw/')
        print(f'{driver.current_url} is open')