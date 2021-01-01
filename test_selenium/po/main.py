# 12 page object原则，为代码事例3-1
from test_selenium.po.hogwarts import Hogwarts


class Main:
    def send_key(self):  # 百度首页输入框
        pass

    def click(self):  # 百度首页点击
        pass

    def title(self):  # 百度首页的标题栏
        pass

    def click_first_link(self):  # 百度首页点击链接（搜索结果的）
        # click link
        return Hogwarts()  # 因为跳转到详情页面，所以需要进行return
