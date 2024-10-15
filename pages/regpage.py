from selenium.webdriver.support.wait import WebDriverWait
from conftest import browser
from selenium.webdriver.common.by import By
from faker import Faker
from selenium.webdriver.support import expected_conditions as EC


class Regpage:

    def __init__(self, browser):
        self.browser = browser


    def fill_reg_form(self):
        fake = Faker()
        first_name_line = self.browser.find_element(By.XPATH, '//*[@name = "first_name"]')
        first_name_line.click()
        first_name_line.clear()
        first_name_line.send_keys(fake.first_name())
        last_name_line = self.browser.find_element(By.XPATH, '//*[@name = "last_name"]')
        last_name_line.click()
        last_name_line.clear()
        last_name_line.send_keys(fake.last_name())
        reg_button = self.browser.find_element(By.XPATH, '//*[@type = "submit"]')
        assert reg_button is not None

