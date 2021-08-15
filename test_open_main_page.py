from selenium import webdriver

def test_open_main_page():
    driver = webdriver.Chrome()
    driver.get("https://qastand.valhalla.pw/")
    print(f'{driver.current_url} is open')
    driver.quit()

