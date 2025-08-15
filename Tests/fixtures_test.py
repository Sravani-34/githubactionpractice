'''import pytest


@pytest.fixture
def test_prequset():
    print("Lanuch bowser")
    print("enter credentials")
    print("submit detatils")
@pytest.fixture()
def test_close():
        print("Close all the browsers")
        print("Closure")

def test_login(test_prequset):
    print("This is login method")



def test_logout(test_close):
    print("This is logout method")



#2nd method


@pytest.fixture
def test_prequset():
    print("Lanuch bowser")
    print("enter credentials")
    print("submit detatils")
    yield
    print("Close all the browsers")
    print("Closure")

def test_login(test_prequset):
    print("This is login method")



def test_logout(test_prequset):
    print("This is logout method")'''