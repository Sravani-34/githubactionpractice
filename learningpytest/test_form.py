from selenium import webdriver
from selenium.webdriver.common.by import By

def test_formsubmit():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://www.lambdatest.com/selenium-playground/simple-form-demo')
    print("Title",driver.title)
    search_box=driver.find_element(By.XPATH,"//input[@id='user-message']")
    search_box.send_keys("Hello")
    submit_button=driver.find_element(By.ID,'showInput')
    submit_button.click()
    message = driver.find_element(By.ID, 'message').text
    assert message=="Hello"
test_formsubmit()
