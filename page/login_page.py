import allure


class LoginPage:

    @allure.step(title='输入用户名')
    def input_username(self, username):
        allure.attach('用户名是：' + username, '' )
        print("输入用户名" + username)

    @allure.step(title='输入密码')
    def input_password(self, password):
        allure.attach('密码是', password)
        print("输入密码" + password)

    @allure.step(title='点击登录')
    def click_login(self):
        print("点击登录")
