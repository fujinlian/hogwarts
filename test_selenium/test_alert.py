# 10文件上传弹窗处理
from time import sleep
from selenium.webdriver import ActionChains
from test_selenium.base import Base


class TestAlert(Base):
    def test_alert(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to_frame("iframeResult")

        drag = self.driver.find_element_by_id("draggable")
        drog = self.driver.find_element_by_id("droppable")
        action = ActionChains(self.driver)
        action.drag_and_drop(drag, drog).perform()
        sleep(3)
        print("点击 alert 确认")
        self.driver.switch_to.alert.accept()
        self.driver.switch_to_default_content()  # 切换回默认首页/默认的frame页面
        self.driver.find_element_by_id("submitBTN").click()
        sleep(3)
