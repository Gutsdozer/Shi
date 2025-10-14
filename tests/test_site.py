from objects.user import users_to_register
from pages.homepage import Homepage
from pages.regpage import Regpage
from conftest import browser
import pytest
from pages.login_page import Loginpage



@pytest.fixture(params=[
    ("bobby@gmail.com", "password1"),
    ("freddy@gmail.com", "password2"),
])
def user_credentials(request):
    return request.param


def test_regform(browser):
    homepage = Homepage(browser)
    homepage.open_reg_form()

def test_registration(browser):
    homepage = Homepage(browser)
    homepage.open_reg_form()
    regpage = Regpage(browser)
    regpage.fill_reg_form_random_test_data()

def test_registration_login_logout(browser):
    homepage = Homepage(browser)
    homepage.open_reg_form()
    regpage = Regpage(browser)
    regpage.register_login_logout()

def test_registration_user_object(browser):
    homepage = Homepage(browser)
    homepage.open_reg_form()
    regpage = Regpage(browser)
    for user_data in users_to_register:
        homepage.open_reg_form()
        regpage.register_user_obj(user_data)






