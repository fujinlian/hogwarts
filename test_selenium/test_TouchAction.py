from time import sleep
from selenium import webdriver
from selenium.webdriver import TouchActions


class TestTouchAction():
    def setup(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option('w3c', False)
        self.driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver', options=option)
        self.driver.maximize_window()  # 窗口最大化
        self.driver.implicitly_wait(5)  # 隐式等待，全局的，查找元素之前起作用；非常推荐；只能查找到元素，不知道元素是否可见、是否可点击

    def teardown(self):
        self.driver.quit()  # 浏览器的关闭，资源的回收

    # 打开百度首页，输入selenium，然后点击搜索并滑动到底部
    def test_touchaction_scrollbottom(self):
        self.driver.get("http://www.baidu.com")
        el = self.driver.find_element_by_id("kw")
        el_search = self.driver.find_element_by_id("su")

        el.send_keys("selenium测试")
        action = TouchActions(self.driver)
        action.tap(el_search)
        action.perform()

        action.scroll_from_element(el, 0, 10000).perform()
        sleep(3)
