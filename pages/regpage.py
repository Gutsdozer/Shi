import time
from conftest import browser
from selenium.webdriver.common.by import By
from faker import Faker
import random
from loguru import logger
from pages import pages_helper




def generate_phone_number(pattern):
    number = ""
    for char in pattern:
        if char == '3':
            number += str(random.randint(0, 9))
        else:
            number += char
    return number

def fill_text_line(browser, locator, text):
    element = browser.find_element(*locator)
    element.click()
    element.clear()
    element.send_keys(text)


    logger.add("test_site.log", rotation="10 MB", retention="1 week")


class Regpage:

    def __init__(self, browser):
        self.browser = browser

    def fill_reg_form(self):
        submit_button = self.browser.find_element(By.XPATH, '//*[@type = "submit"]')
        assert submit_button is not None
        fake = Faker()
        fill_text_line(self.browser, (By.XPATH, '//*[@name = "first_name"]'), fake.first_name())
        logger.info("First name is filled with fake first name")
        fill_text_line(self.browser, (By.XPATH, '//*[@name = "last_name"]'), fake.last_name())
        fill_text_line(self.browser, (By.ID, 'email'), fake.email())
        fill_text_line(self.browser, (By.ID, 'phone'), generate_phone_number('0533333333'))
        





