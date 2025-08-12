import pytest
from selene import browser, have, be
from selene.support.shared import config

@pytest.fixture
def browser_size():
    config.browser_width = 1380
    config.browser_height = 720

@pytest.fixture
def browser_open(browser_size):
    browser.config.browser_name = "chrome"
    browser.open("https://www.google.com/")
    yield browser
    browser.quit()