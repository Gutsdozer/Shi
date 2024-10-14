from pages.homepage import Homepage
from conftest import browser

def test_regform(browser):
    homepage = Homepage(browser)
    homepage.open_reg_form()



