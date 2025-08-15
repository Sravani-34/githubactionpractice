'''import pytest


@pytest.fixture(scope="session",autouse=True)
def test_prequset():
    print("Lanuch bowser")
    print("enter credentials")
    print("submit detatils")
    yield
    print("Close all the browsers")
    print("Closure")
def pytest_addoption(parser):
    parser.addoption("chrome")'''



from selenium.webdriver.remote.remote_connection import RemoteConnection

from utilities.test_data import TestData
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions


@pytest.fixture(params=["chrome", "firefox", "edge"])
def initialize_driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "firefox":
        driver = webdriver.Firefox()
    elif request.param == "edge":
        driver = webdriver.Edge()

    request.cls.driver = driver  # Make it accessible in self.driver
    print("Browser name:", request.param)
    driver.get(TestData.url)
    driver.maximize_window()
    yield driver   # ✅ FIXED: Yield the driver object
    print("Driver Close")
    driver.close()


# 1st Step: Declare Variables For Setting Up LambdaTest
user_name="musunurisravani34"
Access_key="H2NT7EETPzV7yBaUl8mQ3wh7tBYwxTxRXoIZ5r7gCrnZANzLye"
remote_url = f"https://{user_name}:{Access_key}@hub.lambdatest.com/wd/hub"

@pytest.fixture(params=["chrome", "firefox", "edge"])
def driver_initialization(request):
    browser = request.param

    lt_options = {
        "build": "LambdaTest Sample Build",
        "name": f"LambdaTest Grid On {browser.capitalize()}",
        "platformName": "Windows 10",
        "browserVersion": "latest",
    }

    if browser == "chrome":
        options = ChromeOptions()
    elif browser == "firefox":
        options = FirefoxOptions()
    elif browser == "edge":
        options = EdgeOptions()
    else:
        raise ValueError("Unsupported browser!")

    options.set_capability('LT:Options', lt_options)

    driver = webdriver.Remote(command_executor=remote_url, options=options)
    request.cls.driver = driver
    yield
    driver.quit()


