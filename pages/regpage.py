import time

import pytest
from selenium.common import TimeoutException
from selenium.webdriver.support.expected_conditions import presence_of_element_located

from conftest import browser
from selenium.webdriver.common.by import By
from faker import Faker
from helpers.logger import log
from helpers import pages_helper
from helpers.pages_helper import generate_password
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from objects.user import User


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

    def register_login_logout(self):
        global profile_button
        submit_button = self.browser.find_element(By.XPATH, '//*[@type = "submit"]')
        assert submit_button.is_displayed()
        pages_helper.fill_text_line(self.browser, (By.XPATH, '//*[@name = "first_name"]'), 'Bobby')
        pages_helper.fill_text_line(self.browser, (By.XPATH, '//*[@name = "last_name"]'), "Bobson")
        pages_helper.fill_text_line(self.browser, (By.ID, 'teuda'), pages_helper.generate_number('333333333'))
        pages_helper.select(self.browser, (By.NAME, 'sex'), 'Мужской')
        user_email = pages_helper.generate_email()
        pages_helper.fill_text_line(self.browser, (By.ID, 'email'), user_email)
        pages_helper.fill_text_line(self.browser, (By.ID, 'phone'), '0533333333')
        pages_helper.fill_text_line(self.browser, (By.ID, 'birthdate'), '1995')
        pages_helper.fill_text_line(self.browser, (By.ID, 'aliya_year'), '2024')
        pages_helper.fill_text_line(self.browser, (By.ID, 'password'), 'password2')
        pages_helper.fill_text_line(self.browser, (By.NAME, 'password_confirm'), 'password2')
        submit_button.click()
        element = self.browser.find_element(By.ID, 'infoMessage')
        assert "Учетная запись успешно создана" in element.text
        login_email = self.browser.find_element(By.NAME, 'identity')
        login_email.send_keys(user_email)
        login_password = self.browser.find_element(By.NAME, 'password')
        login_password.send_keys('password2')
        submit_login = self.browser.find_element(By.XPATH, '//*[@id="content"]/div[2]/div/div/div/div[2]/div/form/p[4]/input')
        submit_login.click()
        try:
            profile_button = (WebDriverWait(self.browser, 3).until
                              (EC.presence_of_element_located((By.XPATH, '//*[@id="topmenu"]/div/div/div[2]/ul/li[5]/a'))))
        except TimeoutException:
            print("Element did not appear")
        exit_button = self.browser.find_element(By.XPATH, '//*[@id="topmenu"]/div/div/div[2]/ul/li[5]/ul/li[3]/a')
        action = ActionChains(self.browser)
        action.move_to_element(profile_button).move_to_element(exit_button).click().perform()
        exit_sign = self.browser.find_element(By.XPATH, '//*[@id="infoMessage"]/p')
        assert "Выход успешный" in exit_sign.text

    def register_user_obj(self, user_obj):
        submit_button = self.browser.find_element(By.XPATH, '//*[@type = "submit"]')
        assert submit_button.is_displayed()
        log.info(f"Filling registration fields with {user_obj} data")
        pages_helper.fill_text_line(self.browser, (By.NAME, 'first_name'), user_obj.name)
        pages_helper.fill_text_line(self.browser, (By.XPATH, '//*[@name = "last_name"]'), user_obj.second_name)
        pages_helper.fill_text_line(self.browser, (By.ID, 'teuda'), user_obj.teuda)
        pages_helper.select(self.browser, (By.NAME, 'sex'), 'Мужской')
        pages_helper.fill_text_line(self.browser, (By.ID, 'email'), user_obj.email)
        pages_helper.fill_text_line(self.browser, (By.ID, 'phone'), '0533333333')
        pages_helper.fill_text_line(self.browser, (By.ID, 'birthdate'), user_obj.birth_date)
        pages_helper.fill_text_line(self.browser, (By.ID, 'aliya_year'), user_obj.aliah_date)
        pages_helper.fill_text_line(self.browser, (By.ID, 'password'), user_obj.password)
        pages_helper.fill_text_line(self.browser, (By.NAME, 'password_confirm'), user_obj.password)
        log.info(f"All necessary fields are filled with {user_obj} data")
        submit_button.click()
        try:
            info_message = (WebDriverWait(self.browser, 3)
                   .until(presence_of_element_located((By.ID, 'infoMessage'))))
        except TimeoutException:
            log.error(f"Element {info_message} was not found")
        assert "Учетная запись успешно создана" in info_message.text
        log.info(f"Filling login fields with {user_obj} data")
        login_email = self.browser.find_element(By.NAME, 'identity')
        login_email.send_keys(user_obj.email)
        login_password = self.browser.find_element(By.NAME, 'password')
        login_password.send_keys(user_obj.password)
        submit_login = self.browser.find_element(By.NAME, 'submit')
        submit_login.click()
        try:
            profile_button = (WebDriverWait(self.browser, 3).until
                              (EC.presence_of_element_located(
                                  (By.XPATH, '//*[@id="topmenu"]/div/div/div[2]/ul/li[5]/a'))))
        except TimeoutException:
            log.error(f"Element {profile_button} was not found")
        exit_button = self.browser.find_element(By.XPATH, '//*[@id="topmenu"]/div/div/div[2]/ul/li[5]/ul/li[3]/a')
        action = ActionChains(self.browser)
        action.move_to_element(profile_button).move_to_element(exit_button).click().perform()
        try:
            exit_sign = (WebDriverWait(self.browser, 3)
                     .until(presence_of_element_located((By.XPATH, '//*[@id="infoMessage"]/p'))))
        except TimeoutException:
            log.error(f"Element {exit_sign} was not found")
        assert "Выход успешный" in exit_sign.text
























