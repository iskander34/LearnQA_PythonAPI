import pytest
import requests


class TestExample13:
    testdata = [
        (
        "Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
        "Mobile", "No", "Android"),
        (
        "Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1",
        "Mobile", "Chrome", "iOS"),
        ("Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/", "Googlebot", "Unknown", "Unknown"),
        (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0",
        "Web", "Chrome", "No"),
        (
        "Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
        "Mobile", "No", "iPhone")
    ]

    @pytest.mark.parametrize("user_agent, expected_platform, expected_browser, expected_device", testdata)
    def test_check_user_agent(self, user_agent, expected_platform, expected_browser, expected_device):
        url_link = "https://playground.learnqa.ru/ajax/api/user_agent_check"

        response = requests.get(url_link, headers={"User-Agent": user_agent})

        actual_platform = response.json()["platform"]
        assert actual_platform == expected_platform, f"By User Agent {user_agent} platform: {actual_platform} is not true"

        actual_browser = response.json()["browser"]
        assert actual_browser == expected_browser, f"By User Agent {user_agent} browser:{actual_browser} is not true"

        actual_device = response.json()["device"]
        assert actual_device == expected_device, f"By User Agent {user_agent} device:{actual_device} is not true"
