import allure

from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions


@allure.epic("Delete user cases")
class TestUserDelete(BaseCase):
    @allure.description("Removing user from closed list")
    def test_user_delete_id2(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        response1 = MyRequests.post("/user/login", data=data)

        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")
        user_id = self.get_json_value(response1, "user_id")

        response2 = MyRequests.get(
            "/user/auth",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        Assertions.assert_json_value_by_name(
            response2,
            "user_id",
            user_id,
            "User id from auth method is not equal to user id from check method"
        )

        response3 = MyRequests.delete(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        Assertions.assert_code_status(response3, 400)
        assert response3.text == "Please, do not delete test users with ID 1, 2, 3, 4 or 5.", f"User with id = {user_id} has been removed"

    @allure.description("Removing user succesful")
    def test_user_delete_succesful(self):
        register_data = self.prepare_registration_data(None)

        response1 = MyRequests.post("/user/", data=register_data)

        email = register_data['email']
        password = register_data['password']
        user_id = self.get_json_value(response1, "id")

        login_data = {
            'email': email,
            'password': password
        }
        response2 = MyRequests.post("/user/login", data=login_data)

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        response3 = MyRequests.delete(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        Assertions.assert_code_status(response3, 200)

        response4 = MyRequests.get(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        Assertions.assert_code_status(response4, 404)
        assert response4.text == "User not found", f"User with id = {user_id} not be deleted"

    @allure.description("Removing user not succeesful")
    def test_user_delete_not_succesful(self):
        register_data = self.prepare_registration_data(None)

        response1 = MyRequests.post("/user/", data=register_data)

        email = register_data['email']
        password = register_data['password']

        login_data = {
            'email': email,
            'password': password
        }
        response2 = MyRequests.post("/user/login", data=login_data)

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        response3 = MyRequests.delete(
            "/user/11234",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        Assertions.assert_code_status(response3, 200)

        response4 = MyRequests.get(
            "/user/11234",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        Assertions.assert_code_status(response4, 200)
        Assertions.assert_json_has_key(response4, "username")
