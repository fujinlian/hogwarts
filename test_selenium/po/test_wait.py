# 12 page object原则，为代码事例3-3
from test_selenium.po.main import Main


class TestWait:
    def setup(self):
        main = Main()
        main.click_first_link().get_text()  # 因为main的这个函数return了hogwarts，所以就可以直接调用它的方法get_text
