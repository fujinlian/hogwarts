import os
from selenium import webdriver


class Base():
    def setup(self):
        browser = os.getenv("browser")
        if browser == 'firefox':
            self.driver = webdriver.Firefox()
        else:
            # self.driver = webdriver.Chrome()
            self.driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
        self.driver.maximize_window()  # 窗口最大化
        self.driver.implicitly_wait(5)  # 隐式等待，全局的，查找元素之前起作用；非常推荐；只能查找到元素，不知道元素是否可见、是否可点击

    def teardown(self):
        self.driver.quit()  # 浏览器的关闭，资源的回收
