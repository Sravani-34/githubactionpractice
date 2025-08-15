from selenium import webdriver
from selenium.webdriver.common.by import By



def test_lamda():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://ecommerce-playground.lambdatest.io/')
    print("Title of the url",driver.title)
    search_box=driver.find_element(By.XPATH,"//input[@name='search']")
    search_box.send_keys("Iphone")
    submit=driver.find_element(By.XPATH,"//button[@class='type-text']")
    print("Hello")
    driver.implicitly_wait(3000)
    submit.click()
    driver.quit()

test_lamda()
