import pytest
from selenium import webdriver
import logging

logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    datefmt='%d-%b-%y %H:%M:%S'
)


@pytest.fixture()
def browser():
    logging.info("Opening Chrome browser")
    browser = webdriver.Chrome()
    logging.info("Opening Shishi Shabbat site")
    browser.get("https://shishi.co.il/")
    browser.maximize_window()
    browser.implicitly_wait(3)
    yield browser
    #browser.close()



