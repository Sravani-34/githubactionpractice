import pytest
from selenium.webdriver.common.by import By

from utilities.conftest import initialize_driver


@pytest.mark.usefixtures("initialize_driver")
class BaseClass:
    pass
class Test_Drivers(BaseClass):
 def test_multiple_browser(self):
    self.driver.get("https://www.lambdatest.com/selenium-playground/")
    header= self.driver.find_element(By.XPATH,"//h1[text()='Selenium Playground']").text
    print("Header",header)
    assert header=="Selenium Playground"
class Test1_Drivers(BaseClass):
 def test1_multiple_browser(self):
    self.driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=account/login")
    assert self.driver.title == "Account Login"







