import pytest
from selenium import webdriver
from loguru import logger




@pytest.fixture()
def browser():
    browser = webdriver.Chrome()
    try:
        logger.info("Chrome browser is opened")
        browser.get("https://shishi.co.il/")
        logger.info("Shishi shabbat site homepage is opened")
        browser.maximize_window()
        browser.implicitly_wait(3)
        yield browser
    finally:
        browser.quit()





