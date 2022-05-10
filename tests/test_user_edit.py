import allure

from lib.my_requests import MyRequests
from datetime import datetime
from lib.base_case import BaseCase
from lib.assertions import Assertions

@allure.epic("Edit user cases")
class TestUserEdit(BaseCase):
    @allure.step
    @allure.tag("Smoke")
    @allure.severity(severity_level="Blocker")
    @allure.description("Edit user after created")
    def test_edit_just_created_user(self):
        # REGISTER
        register_data = self.prepare_registration_data(None)
        response1 = MyRequests.post("/user/", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data['email']
        first_name = register_data['firstName']
        password = register_data['password']
        user_id = self.get_json_value(response1, "id")

        # LOGIN
        login_data = {
            'email': email,
            'password': password
        }
        response2 = MyRequests.post("/user/login", data=login_data)

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        # EDIT
        new_name = "Changed Name"

        response3 = MyRequests.put(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data={"firstName": new_name}
        )

        Assertions.assert_code_status(response3, 200)

        # GET
        response4 = MyRequests.get(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        Assertions.assert_json_value_by_name(
            response4,
            "firstName",
            new_name,
            "Wrong name of the user after edit"
        )

        # NEGATIVE
        #
        # edit with out authorization

        response5 = MyRequests.put(f"/user/{user_id}", data={"firstName": new_name})

        Assertions.assert_code_status(response5, 400)
        assert response5.text == "Auth token not supplied", "User is edit with out authorization"

        #
        # edit with authorization by another user

        response6 = MyRequests.put(
            "/user/100",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data={"firstName": new_name}
        )

        Assertions.assert_code_status(response6, 200)

        response7 = MyRequests.get(
            "/user/100",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        Assertions.assert_code_status(response7, 404)
        assert response7.text == "User not found", "User is edit with authorization by another user"

        #
        # changed email with authorization user

        base_part = "learnqa"
        domain = "example.com"
        random_part = datetime.now().strftime("%m%d%Y%H%M%S")
        new_email = f"{base_part}{random_part}{domain}"

        response8 = MyRequests.put(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data={"email": new_email}
        )

        Assertions.assert_code_status(response8, 400)
        assert response8.text == "Invalid email format"

        response9 = MyRequests.get(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        Assertions.assert_json_value_by_name(
            response9,
            "email",
            email,
            "Wrong email of the user after edit"
        )

        #
        # changed "firstName"

        new_email_short_symbol = "@"

        response10 = MyRequests.put(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data={"email": new_email_short_symbol}
        )

        Assertions.assert_code_status(response10, 400)
        assert response8.text == "Invalid email format"

        response11 = MyRequests.get(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        Assertions.assert_json_value_by_name(
            response11,
            "email",
            email,
            "Wrong email of the user after edit"
        )
