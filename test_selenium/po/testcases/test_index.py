# 用pytest
from test_selenium.po.page.index_page import IndexPage


class TestIndex:
    def setup_class(self):
        # 测试用例先从首页进入，所以先实例化首页的类。index_page前面不加self就只能本方法使用、加的话就可以本class内其他方法也可以使用
        self.index_page = IndexPage()

    def test_login(self):
        # 1.跳转到登录页面  2。登录页面扫码登录
        self.index_page.goto_login().login_scanf()

    def test_register(self):
        # 1.跳转到注册页面  2。在注册页面进行注册
        self.index_page.goto_register().register()
