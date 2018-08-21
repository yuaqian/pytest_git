import pytest

from page.login_page import LoginPage

class TestLogin:

    def setup(self):
        self.login_page = LoginPage()

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("username,password", [("zhangsan", "zhangsan123"), ("lisi", "lisi123")])
    def test_login1(self, username, password):
        self.login_page.input_username(username)
        self.login_page.input_password(password)
        self.login_page.click_login()

        assert 1

    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    def test_login2(self):
        self.login_page.input_password("2")
        self.login_page.input_username("2")
        self.login_page.click_login()

        assert 0
