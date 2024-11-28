import pytest

from conftest import browser
from selenium.webdriver.common.by import By
from faker import Faker
from loguru import logger
from helpers import pages_helper


class Loginpage:

    def __init__(self, browser):
        self.browser = browser

    # @pytest.mark.parametrize('creds', [
    #     pytest.param(('user1@mail.com', 'sdfasdf'), id='user1@mail.com, sdfasdf'),
    #     pytest.param(('user2@mail.com', 'qwiuehdsj'), id='user2@mail.com, qwiuehdsj'),
    #     pytest.param(('user3@mail.com', 'pqwidsncsd'), id='user3@mail.com, pqwidsncsd')
    # ])
    # def fill_login_form_parametrize(self, creds):
    #     login, passw = creds
    #     submit_button = self.browser.find_element(By.CLASS_NAME, 'button gradient')
    #     assert submit_button is not None
    #     self.browser.find_element(By.NAME, 'identity').click()
    #     self.browser.find_element(By.NAME, 'identity').send_keys(login)
    #     self.browser.find_element(By.NAME, 'password').click()
    #     self.browser.find_element(By.NAME, 'password').send_keys(passw)
