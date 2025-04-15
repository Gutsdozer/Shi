import pytest

from conftest import browser
from selenium.webdriver.common.by import By
from faker import Faker
from loguru import logger
from helpers import pages_helper


class Loginpage:

    def __init__(self, browser):
        self.browser = browser

    def login(self, username, password):
        element = self.browser.find_element(By.XPATH, '//*[@id="content"]/div[2]/div/div/div/div[2]/div/form/p[2]/label')
        assert element.is_displayed()
        email_line = self.browser.find_element(By.ID, 'identity')
        email_line.click()
        email_line.clear()
        email_line.send_keys(username)
        password_line = self.browser.find_element(By.ID, 'password')
        password_line.click()
        password_line.clear()
        password_line.send_keys(password)
        checkbox = self.browser.find_element(By.ID, 'remember')
        checkbox.click()
        self.browser.find_element(By.XPATH, '//*[@id="content"]/div[2]/div/div/div/div[2]/div/form/p[4]/input').click()






