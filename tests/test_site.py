from helpers import ai_data_generation
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


#This is the main test which checks basic functionality of the site
def test_registration_user_object(browser):
    homepage = Homepage(browser)
    homepage.open_reg_form()
    regpage = Regpage(browser)
    for user_data in users_to_register:
        homepage.open_reg_form()
        regpage.register_user_obj(user_data)

def test_registration_generated_test_data(browser):
    homepage = Homepage(browser)
    homepage.open_reg_form()
    regpage = Regpage(browser)
    role_description = "a standard Israeli male citizen who uses English for filling all the required fields"
    generated_test_data = ai_data_generation.generate_user_data(role_description)
    regpage.register_generated_user_data(generated_test_data)






