from pages.homepage import Homepage
from pages.regpage import Regpage
from conftest import browser
import pytest
from pages.login_page import Loginpage





def test_regform(browser):
    homepage = Homepage(browser)
    homepage.open_reg_form()

def test_registration(browser):
    homepage = Homepage(browser)
    homepage.open_reg_form()
    regpage = Regpage(browser)
    regpage.fill_reg_form_random_test_data()

def test_login_params(browser, user_credentials):
    homepage = Homepage(browser)
    homepage.open_login_form()
    loginpage = Loginpage(browser)
    for credentials in user_credentials:
        loginpage.login(credentials["username"], credentials["password"])







