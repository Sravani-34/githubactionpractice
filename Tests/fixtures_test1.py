import pytest


@pytest.fixture
def setup():
    print("Start the browser")
    print("Enter credentials")
    print("Submit the details")
    yield
    print("Checkout the process")
    print("Close the browser")


def test_login(setup):
    print("This is login method")



def test_logout(setup):
    print("This is logout method")
