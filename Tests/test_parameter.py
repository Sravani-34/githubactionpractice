import pytest


@pytest.mark.parametrize("username,password",
                          [
                        ("Java","Selenium"),
                        ("JavaScript","Cypress")
                          ]
                        )
def test_m(username,password):
    print(username)
    print(password)
