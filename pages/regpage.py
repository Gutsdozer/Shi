import time

import pytest

from conftest import browser
from selenium.webdriver.common.by import By
from faker import Faker
from loguru import logger
from helpers import pages_helper
from helpers.pages_helper import generate_password

logger.add("test_site.log", rotation="10 MB", retention="1 week")


class Regpage:

    def __init__(self, browser):
        self.browser = browser


    def fill_reg_form_random_test_data(self):
        submit_button = self.browser.find_element(By.XPATH, '//*[@type = "submit"]')
        assert submit_button.is_displayed()
        fake = Faker()
        pages_helper.fill_text_line(self.browser, (By.XPATH, '//*[@name = "first_name"]'), fake.first_name())
        pages_helper.fill_text_line(self.browser, (By.XPATH, '//*[@name = "last_name"]'), fake.last_name())
        pages_helper.fill_text_line(self.browser, (By.ID, 'teuda'), pages_helper.generate_number('333333333'))
        pages_helper.select(self.browser, (By.NAME, 'sex'), 'Женский')
        pages_helper.fill_text_line(self.browser, (By.ID, 'email'), fake.email())
        pages_helper.fill_text_line(self.browser, (By.ID, 'phone'), pages_helper.generate_number('0533333333'))
        pages_helper.fill_text_line(self.browser, (By.ID, 'birthdate'), pages_helper.generate_random_date())
        pages_helper.fill_text_line(self.browser, (By.ID, 'aliya_year'), fake.year())
        pages_helper.fill_text_line(self.browser, (By.ID, 'password'), generate_password())
        time.sleep(4)

    def fill_reg_form(self):
        submit_button = self.browser.find_element(By.XPATH, '//*[@type = "submit"]')
        assert submit_button.is_displayed()
        pages_helper.fill_text_line(self.browser, (By.XPATH, '//*[@name = "first_name"]'), "Bobby")
        pages_helper.fill_text_line(self.browser, (By.XPATH, '//*[@name = "last_name"]'), "Bobson")
        pages_helper.fill_text_line(self.browser, (By.ID, 'teuda'), pages_helper.generate_number('333333333'))
        pages_helper.select(self.browser, (By.NAME, 'sex'), 'Мужской')
        pages_helper.fill_text_line(self.browser, (By.ID, 'email'), "bobby@gmail.com")
        pages_helper.fill_text_line(self.browser, (By.ID, 'phone'), pages_helper.generate_number('0533333333'))













