import pytest
from selenium import webdriver
from loguru import logger




@pytest.fixture()
def browser():
    browser = webdriver.Chrome()
    logger.info("Chrome browser is opened")
    browser.get("https://shishi.co.il/")
    logger.info("Shishi shabbat site homepage is opened")
    browser.maximize_window()
    browser.implicitly_wait(3)
    yield browser
    #browser.close()

@pytest.fixture(scope="module")
def user_credentials():
    return[
        {"username": "bobby@gmail.com", "password": "password1"},
        {"username": "freddy@gmail.com", "password": "password2"}
    ]



