from conftest import browser
from selenium.webdriver.common.by import By
from helpers.logger import log
from helpers.locators import HomepageLocators


class Homepage:

    def __init__(self, browser):
        self.browser = browser

    def open_reg_form(self):
        self.browser.find_element(*HomepageLocators.REGISTRATION).click()
        log.info("Registration page is opened")


    def open_login_form(self):
        self.browser.find_element(By.XPATH, '//*[text() = "Вход"]').click()
        log.info("Login page is opened")


    def lang_switch(self):
        self.browser.find_element(By.XPATH, '//*[@class = "flag-icon flag-icon-gb"]').click()
