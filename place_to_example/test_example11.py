import requests

class TestExample11:

    def test_check_cookies_ex11(self):
        response = requests.get("https://playground.learnqa.ru/api/homework_cookie")
        print(dict(response.cookies))

        expected_responce_cookie = {'HomeWork': 'hw_value'}
        actual_response_cookie = dict(response.cookies)

        assert actual_response_cookie == expected_responce_cookie, "Actual cookie in response is not correct"

