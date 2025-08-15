import sys
from datetime import datetime

import pytest
from selenium import webdriver

class Test_Lambda:
  def test_first_skip(self):
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://lambdatest.github.io/sample-todo-app/')
    pytest.skip()
    expected_title="Sample page - lambdatest.com"
    assert expected_title==driver.title
@pytest.mark.skip(reason="Need to implement the code")
def test_first1_skip(self):
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://ecommerce-playground.lambdatest.io/index.php?route=account/login')
    expected_title_page='Account Login'
    assert expected_title_page==driver.title

@pytest.mark.skipif(
      datetime.now() >= datetime(2099, 12, 31),
      reason="Repo Is Not Complete Until After Finishing Tutorial")
def test_pytest_github_repo():
    driver = webdriver.Chrome()
    driver.get("https://github.com/RexJonesII/PytestTutorials")
    expected_title = "RexJonesII"
    print("Title: ", expected_title)
    assert driver.title.__contains__(expected_title)
#feature=True
@pytest.mark.skipif(
       False,
      reason="If it is true then excute")
def test1_pytest_github_repo():
    driver = webdriver.Chrome()
    driver.get("https://github.com/RexJonesII/PytestTutorials")
    expected_title = "RexJonesII"
    print("Title: ", expected_title)
    assert driver.title.__contains__(expected_title)




