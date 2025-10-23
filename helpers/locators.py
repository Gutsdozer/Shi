from selenium.webdriver.common.by import By

class RegpageLocators:
    FIRST_NAME = (By.NAME, 'first_name')
    LAST_NAME = (By.XPATH, '//*[@name = "last_name"]')
    TEUDA = (By.ID, 'teuda')
    SEX = (By.NAME, 'sex')
    EMAIL = (By.ID, 'email')
    PHONE = (By.ID, 'phone')
    BIRTHDATE = (By.ID, 'birthdate')
    ALIYA_YEAR = (By.ID, 'aliya_year')
    PASSWORD = (By.ID, 'password')
    PASSWORD_CONFIRM = (By.NAME, 'password_confirm')

class LoginpageLocators:
    LOGIN_EMAIL = (By.NAME, 'identity')
    PASSWORD = (By.NAME, 'password')
    SUBMIT_BUTTON = (By.NAME, 'submit')

class ProfilePageLocators:
    PROFILE_BUTTON = (By.XPATH, '//*[@id="topmenu"]/div/div/div[2]/ul/li[5]/a')
    EXIT_BUTTON = (By.XPATH, '//*[@id="infoMessage"]/p')
