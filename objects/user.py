from helpers import pages_helper
from faker import Faker

class User:

    def __init__(self, name, second_name, teuda,
                 email, phone, birth_date, aliah_date, password):
        self.name = name
        self.second_name = second_name
        self.teuda = teuda
        self.email = email
        self.phone = phone
        self.birth_date = birth_date
        self.aliah_date = aliah_date
        self.password = password

users_to_register = [User("Bobbins", "Hryapson", pages_helper.generate_number("333333333"),
                          pages_helper.generate_email(), pages_helper.generate_number("1513333333"),
                          pages_helper.generate_random_date(),
                          '2022', "password1"), User("Lopuh", "Dobkins",
                                                     pages_helper.generate_number("333333333"),
                          pages_helper.generate_email(), pages_helper.generate_number("1513333333"),
                          pages_helper.generate_random_date(),
                          '2024', "password2")]