from selenium.webdriver.common.by import By

def login(browser):
   email = browser.find_element(By.NAME, "email")
   email.send_keys("qa_test@test.ru")
   password = browser.find_element(By.NAME, "password")
   password.send_keys("!QAZ2wsx")
   browser.find_element(By.CLASS_NAME, "button").click()