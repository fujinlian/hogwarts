# 用IDE录制协助定位元素，打开测试人社区的脚本
# 推荐使用pytest的测试框架

from selenium import webdriver
from time import sleep


class Testerhome():
    def setup(self):
        self.driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
        self.driver.maximize_window()  # 窗口最大化
        self.driver.implicitly_wait(5)  # 隐式等待，全局的，查找元素之前起作用；非常推荐；只能查找到元素，不知道元素是否可见、是否可点击

    def teardown(self):
        self.driver.quit()  # 浏览器的关闭，资源的回收

    def test_testerhome(self):
        self.driver.get("https://testerhome.com/")
        sleep(2)
        self.driver.find_element_by_link_text("社团").click()
        sleep(2)
        self.driver.find_element_by_link_text("求职面试圈").click()
        sleep(3)
        self.driver.find_element_by_css_selector(".topic-26766 .title > a").click()
        sleep(2)
