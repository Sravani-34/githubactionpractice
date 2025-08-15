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

import pytest
from selenium import webdriver
from selenium.webdriver.remote.remote_connection import RemoteConnection

from utilities.test_data import TestData


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
remote_url = "https://" + user_name + ":" + Access_key + "@hub.lambdatest.com/wd/hub"
# 2nd Step: Define The Desired Capabilities (3 Caps)
chrome_caps={
    "build"    :"1.0",
    "name"   :"LambdaTest Grid On Chrome",
    "platform":"windows11",
    "browserName" : "chrome",
    "version"   : "latest"
    }
firefox_caps={
    "build"  :"2.0",
    "name"   : "LambdaTest Grid On Firefox",
    "platform":"windows11",
    "browserName" :"Firefox",
    "version" :"latest"
}
edge_caps={
    "build"  :"3.0",
    "name"   : "LambdaTest Grid On Edge",
    "platform":"windows11",
    "browserName" :"Edge",
    "version" :"latest"
}

#3rd Step: Connect To LambdaTest Using A Fixture & RemoteConnection
@pytest.fixture(params=["chrome","firefox","edge"])
def driver_intialization(request):
    desired_caps={}
    if request.param=="chrome":
       desired_caps.update(chrome_caps)
       driver=webdriver.Remote(
           command_executor=RemoteConnection(remote_url),
           desired_capabilities={"LT: Options":desired_caps})
    elif request.param=="firefox":
        desired_caps.update(firefox_caps)
        driver=webdriver.Remote(
            command_executor=RemoteConnection(remote_url),
            desired_capabilities={"LT: Options":desired_caps})
    elif request.param=="edge":
        desired_caps.update(edge_caps)
        driver=webdriver.Remote(
            command_executor=RemoteConnection(remote_url),
            desired_capabilities={"LT: Options":desired_caps})
        request.cls.driver=driver
        yield
        driver.close()


