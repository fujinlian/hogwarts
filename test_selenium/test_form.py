# 表单的操作，跟其他的方法类似
from time import sleep
from selenium import webdriver


class TestTouchAction():
    def setup(self):
        #  option = webdriver.ChromeOptions()
        # option.add_experimental_option('w3c',False)
        self.driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
        self.driver.maximize_window()  # 窗口最大化
        self.driver.implicitly_wait(5)  # 隐式等待，全局的，查找元素之前起作用；非常推荐；只能查找到元素，不知道元素是否可见、是否可点击

    def teardown(self):
        self.driver.quit()  # 浏览器的关闭，资源的回收

    def test_form(self):
        self.driver.get("https://testerhome.com/account/sign_in")
        self.driver.find_element_by_id("user_login").send_keys("123")
        self.driver.find_element_by_id("user_password").send_keys("password")
        self.driver.find_element_by_id("user_remember_me").click()
        self.driver.find_element_by_xpath('//*[@id="new_user"]/div[4]/input').click()  # 这一步只是查找元素，实际起了什么作用呢？
        sleep(5)
