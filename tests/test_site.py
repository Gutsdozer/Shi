from pages.homepage import Homepage
from pages.regpage import Regpage
from conftest import browser
import pytest





def test_regform(browser):
    homepage = Homepage(browser)
    homepage.open_reg_form()

def test_registration(browser):
    homepage = Homepage(browser)
    homepage.open_reg_form()
    regpage = Regpage(browser)
    regpage.fill_reg_form_random_test_data()



