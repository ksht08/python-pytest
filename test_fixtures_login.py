import pytest

@pytest.fixture
def login_page(browser):
    print("Login Page")

@pytest.fixture
def user():
    print("User Fixture")
    return "username", "password"

def test_login(login_page, user):
    username, password = user
    assert username == "username", "Username should match"
    assert password == "password", "Password should match"

def test_logout(login_page, user):
    username, password = user
    assert username == "username", "Username should match"
    assert password == "password", "Password should match"