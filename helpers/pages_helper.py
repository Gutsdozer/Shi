from faker.contrib.pytest.plugin import faker
from faker import Faker
from conftest import browser
from selenium.webdriver.common.by import By
import random
import pytest
from selenium.webdriver.support.ui import Select

from conftest import browser


def fill_text_line(browser, locator, text):
    element = browser.find_element(*locator)
    element.click()
    element.clear()
    element.send_keys(text)


def generate_number(pattern):
    number = ""
    for char in pattern:
        if char == '3':
            number += str(random.randint(0, 9))
        else:
            number += char
    return number


def generate_random_date():
    day = random.randint(1, 28)
    month = random.randint(1, 12)
    year = random.randint(1990, 2006)
    return f"{day:02d}{month:02d}{year}"


def select(browser, locator, visible_text):
    select_element = browser.find_element(*locator)
    select_object = Select(select_element)
    select_object.select_by_visible_text(visible_text)





