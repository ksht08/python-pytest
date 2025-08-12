from selene import browser, have, be
from selene.support.shared import config
import pytest


def test_google_search(browser_open):
    search_text = "KKDRFT ww21323123"
    browser.element("[name='q']").should(be.visible).type(search_text).press_enter()
    browser.element(".card-section").should(have.text("Your search"))
    browser.element(".card-section").should(have.text(search_text))
    browser.element(".card-section").should(have.text("did not match any documents"))
