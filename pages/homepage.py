from conftest import browser
from selenium.webdriver.common.by import By


class Homepage:


    def __init__(self, browser):
        self.browser = browser


    def open_reg_form(self):
        reg_form_button = self.browser.find_element(By.XPATH, "//*[]")