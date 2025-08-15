import pytest


def test_method1():
    print("Hi")
#@pytest.mark.smoke
def test_m2():
    print("hello")
@pytest.mark.sanity
def test_method3():
        print("hello there")

#to run the test cases using command promt use
#first copy the directory from pycharm and paste cd and filename and give pytest it will run all the test case
#If you want to run test case with verbose use pytest -v
#If you want run test case and if you want see results then pytest -v-s or pytest -vs
#If you want to run specific method within the test case then give pytest foldername\filename -vsk keyword
#to excute specific suit like sanity or somke then pytest -m sanity
#@pytest.mark.xfail and @pytest.mark.skip