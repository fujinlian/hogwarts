# 07网页frame与多窗口处理
from test_selenium.base import Base


class TestFrame(Base):
    def test_frame(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to_frame("iframeResult")  # 下面元素所在的iframe的id值，切换才可能找到下面的元素
        print(self.driver.find_element_by_id("draggable").text)
        # 以下2种方式都可以切换至原来的页面进行操作submit，因为两个控件都不在一个frame上，因此需要切换frame才能操作
        # self.driver.switch_to_parent_frame()
        self.driver.switch_to_default_content()
        print(self.driver.find_element_by_id("submitBTN").text)
