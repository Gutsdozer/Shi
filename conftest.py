import pytest
from selenium import webdriver
from helpers.logger import log





@pytest.fixture()
def browser():
    browser = webdriver.Chrome()
    try:
        log.info("Chrome browser is opened")
        browser.get("https://shishi.co.il/")
        log.info("Shishi shabbat site homepage is opened")
        browser.maximize_window()
        browser.implicitly_wait(3)
        yield browser
    finally:
        browser.quit()



