from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from utilities import conftest

@pytest.mark.usefixtures("driver_initialization")
class TestBaseClass:
    pass
class Test_selenium_Grid(TestBaseClass):
    def test_lambdatest_remaining_checkboxes(self):
        driver=self.driver
        driver.get("https://lambdatest.github.io/sample-todo-app/")
        driver.find_element(By.XPATH,"//input[@name='li2']").click()
        remaining_checkboxes= driver.find_element(By.CSS_SELECTOR,'span.ng-binding').text
        assert remaining_checkboxes=="4 of 5 remaining"


