# 10文件上传弹窗处
from time import sleep
from test_selenium.base import Base


class TestFile(Base):
    def test_file_upload(self):
        self.driver.get("https://image.baidu.com/")
        self.driver.find_element_by_xpath("//*[@id='sttb']/img[1]").click()
        self.driver.find_element_by_id("stfile").send_keys("/Users/jinlianfu/Desktop/linux/41.jpeg")
        sleep(8)
