import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

@pytest.fixture(autouse=True)
def start_automatic_fixture():
  print("Start Test With Automatic Fixture")

@pytest.fixture()
def setup_teardown():
  driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=account/login")
  driver.find_element(By.ID, "input-email")\
    .send_keys("Selenium123@gmail.com")
  driver.find_element(By.ID, "input-password")\
    .send_keys("Selenium")
  driver.find_element(By.XPATH,
    "//input[@value='Login']").click()
  print("Log In")
  yield
  driver.find_element(By.PARTIAL_LINK_TEXT,
    "Logout").click()
  print("Log Out")
@pytest.mark.usefixtures("setup_teardown")
def test1_order_history_title():
  driver.find_element(By.PARTIAL_LINK_TEXT,
    "Order").click()
  assert driver.title == "Order History"
  print("Test 1 Is Complete")

def test2_change_password_title(setup_teardown):
  driver.find_element(By.PARTIAL_LINK_TEXT,
    "Password").click()
  assert driver.title == "Change Password"
  driver.find_element(By.ID,'input-password').send_keys("Hello123552252")
  driver.find_element(By.ID,'input-confirm').send_keys("Hello12315525")

  print("Test 2 Is Complete")