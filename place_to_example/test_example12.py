import requests

class TestExamples12:
    def test_check_headers_ex12(self):
        response = requests.get("https://playground.learnqa.ru/api/homework_header")
        print(response.headers)

        expected_response_header = 'Some secret value'
        actual_response_header = response.headers['x-secret-homework-header']

        assert actual_response_header == expected_response_header, "Actual header in response is not correct"

