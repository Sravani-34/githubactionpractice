import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
@pytest.mark.parametrize("num1,num2,expected_result",
    [
        ("10","20","30"),
        ("30","40","70"),
        ("50","10","60")

    ])
def test_parameter(num1,num2,expected_result):
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://www.lambdatest.com/selenium-playground/simple-form-demo')
    driver.find_element(By.ID,'sum1').send_keys(num1)
    driver.find_element(By.ID,'sum2').send_keys(num2)
    driver.find_element(By.XPATH,"//button[text()='Get Sum']").click()
    actual_text=driver.find_element(By.ID,'addmessage').text
    assert actual_text==expected_result,"Actual total and expected do not match"
    #assert driver.title=='LAMBDATEST'

