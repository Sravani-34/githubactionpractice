from selenium import webdriver

def test_first_program():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.gmail.com")
    print('title',driver.title)


test_first_program()