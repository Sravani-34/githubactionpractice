import pytest
from selenium import webdriver
@pytest.mark.xfail(reason="Invalid data")
class Testfail:

 def test_fail(self):
     num=10
     result= num+num
     assert result==200

@pytest.mark.xfail(reason="Invalid number")
def test_fail1():
         num = 100
         result = num + num
         assert result == 200

@pytest.mark.xfail(reason="Invalid data")
@pytest.mark.skip(reason="Invalid data")
class Testfail:

 def test_fail(self):
     num=10
     result= num+num
     assert result==200
 def test_fail1(self):
         num = 100
         result = num + num
         assert result == 200

