# page object直播实践，步骤1：做企业微信首页的建模。首页可以跳转到登录页面和注册页面。步骤2：对登录页面进行建模
from test_selenium.po.page.login_page import LoginPage
from test_selenium.po.page.register_page import RegisterPage


class IndexPage:
    def goto_login(self):
        """跳转到登录页面
        ：return:
        """

        return LoginPage()  # 跳转到登录页面的类。直接return类实际有没有实力化，如何执行？

    def goto_register(self):
        """跳转到注册页面
        ：return:
        """

        return RegisterPage()
