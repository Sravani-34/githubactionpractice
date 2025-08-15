import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
@pytest.mark.smoke
def test_markers():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://www.lambdatest.com/selenium-playground/ajax-form-submit-demo')
    title_name =driver.find_element(By.ID,'title')
    driver.implicitly_wait(2000.0)
    title_name.send_keys("HI")
    messagebox=driver.find_element(By.ID,'description')
    messagebox.send_keys("Hey namasthe")
    submit_button=driver.find_element(By.ID,'btn-submit')
    submit_button.click()
    request=driver.find_element(By.ID,'submit-control').text
    assert request=='Ajax Request is Processing!'
    driver.close()

def test_e2e_login():
    print("Login Statement")
@pytest.mark.smoke
def test_e2e_logout():
    print("Logout statement")

def test_e2e_print():
    print("Print statement")
test_markers()

def setup_module():
    print("Without test")