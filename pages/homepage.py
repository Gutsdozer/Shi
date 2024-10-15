from conftest import browser
from selenium.webdriver.common.by import By


class Homepage:

    def __init__(self, browser):
        self.browser = browser

    def open_reg_form(self):
        regform_button = self.browser.find_element(By.XPATH, '//*[text() = "Регистрация"]').click()

    def lang_switch(self):
        lang_button = self.browser.find_element(By.XPATH, '//*[@class = "flag-icon flag-icon-gb"]').click()
