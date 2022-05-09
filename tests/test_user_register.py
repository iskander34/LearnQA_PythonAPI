import pytest
import string
import random
import allure

from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions
from datetime import datetime


@allure.epic("User register cases")
class TestUserRegister(BaseCase):
    exclude_params = [
        "password",
        "username",
        "firstName",
        "lastName",
        "email"
    ]
    name_params = [
        "one_symbol",
        "251_symbol"
    ]

    def setup(self):
        base_part = "learnqa"
        domain = "example.com"
        random_part = datetime.now().strftime("%m%d%Y%H%M%S")
        self.email = f"{base_part}{random_part}@{domain}"

    @allure.description("This test succesfully register user after authorize")
    @allure.tag("Smoke")
    def test_create_user_successfuly(self):
        data = self.prepare_registration_data(None)

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")

    @allure.description("This test checks register status with sending existing email")
    def test_create_user_with_existing_email(self):
        email = 'vinkotov@example.com'
        data = self.prepare_registration_data(email)

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode(
            "utf-8") == f"Users with email '{email}' already exists", f"Unexpected response content {response.content}"

    @allure.description("This test checks register status w/o sending @ in email")
    def test_create_user_with_out_ad(self):
        base_part = "learnqa"
        domain = "example.com"
        random_part = datetime.now().strftime("%m%d%Y%H%M%S")
        email = f"{base_part}{random_part}{domain}"
        data = {
            'password': '123',
            'username': 'learnqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': email
        }

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode(
            "utf-8") == "Invalid email format", f"Unexpected response content {response.content}"

    @pytest.mark.parametrize('no_condition', exclude_params)
    @allure.step
    @allure.description("This test checks register status w/o sending one of the necessary parameters")
    def test_create_user_with_out_part(self, no_condition):
        if no_condition == "password":
            data = {
                'username': 'learnqa',
                'firstName': 'learnqa',
                'lastName': 'learnqa',
                'email': self.email
            }
        elif no_condition == "username":
            data = {
                'password': '123',
                'firstName': 'learnqa',
                'lastName': 'learnqa',
                'email': self.email
            }
        elif no_condition == "firstName":
            data = {
                'password': '123',
                'username': 'learnqa',
                'lastName': 'learnqa',
                'email': self.email
            }
        elif no_condition == "lastName":
            data = {
                'password': '123',
                'username': 'learnqa',
                'firstName': 'learnqa',
                'email': self.email
            }
        else:
            data = {
                'password': '123',
                'username': 'learnqa',
                'firstName': 'learnqa',
                'lastName': 'learnqa'
            }

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode(
            "utf-8") == f"The following required params are missed: {no_condition}", f"Unexpected response content {response.content}"

    @pytest.mark.parametrize('name_params', name_params)
    @allure.step
    @allure.description("This test checks register status with sending short/long simbol in name")
    def test_create_user_with_bad_name(self, name_params):
        if name_params == "one_symbol":
            len_name = 1
            defining_characteristic = "short"
        else:
            len_name = 251
            defining_characteristic = "long"

        user_name = ''.join(random.choice(string.ascii_lowercase) for i in range(len_name))

        data = {
            'password': '123',
            'username': user_name,
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': self.email
        }

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode(
            "utf-8") == f"The value of 'username' field is too {defining_characteristic}", f"Unexpected response content {response.content}"
