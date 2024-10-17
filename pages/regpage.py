import time

from conftest import browser
from selenium.webdriver.common.by import By
from faker import Faker
import random


def generate_phone_number(pattern):
    number = ""
    for char in pattern:
        if char == '3':
            number += str(random.randint(0, 9))
        else:
            number += char
    return number


class Regpage:

    def __init__(self, browser):
        self.browser = browser

    def fill_reg_form(self):
        reg_button = self.browser.find_element(By.XPATH, '//*[@type = "submit"]')
        assert reg_button is not None

        fake = Faker()
        first_name_line = self.browser.find_element(By.XPATH, '//*[@name = "first_name"]')
        first_name_line.click()
        first_name_line.clear()
        first_name_line.send_keys(fake.first_name())
        last_name_line = self.browser.find_element(By.XPATH, '//*[@name = "last_name"]')
        last_name_line.click()
        last_name_line.clear()
        last_name_line.send_keys(fake.last_name())
        email_line = self.browser.find_element(By.ID, 'email')
        email_line.click()
        email_line.clear()
        email_line.send_keys(fake.email())
        phone_line = self.browser.find_element(By.ID, 'phone')
        phone_line.click()
        phone_line.clear()
        phone_line.send_keys(generate_phone_number('0533333333'))
        time.sleep(10)




