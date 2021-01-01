# 07网页frame与多窗口处理
from time import sleep
from selenium import webdriver
from test_selenium.base import Base


class Testwindows(Base):  # 继承Base类，所以先执行类中的方法、再往下执行
    def test_windows(self):
        self.driver.get("http://www.baidu.com")
        self.driver.find_element_by_link_text("登录").click()
        print(self.driver.current_window_handle)  # 打印当前窗口
        print(self.driver.window_handles)  # 打印当前所有窗口
        self.driver.find_element_by_link_text("立即注册").click()
        print(self.driver.current_window_handle)  # 打印当前窗口
        print(self.driver.window_handles)  # 打印当前所有窗口，是一个列表，当前有2个窗口
        windows = self.driver.window_handles  # 当前窗口列表
        self.driver.switch_to_window(windows[-1])  # 切换窗口

        self.driver.find_element_by_id("TANGRAM__PSP_4__userName").send_keys("username")
        self.driver.find_element_by_id("TANGRAM__PSP_4__phone").send_keys("13200000000")

        self.driver.switch_to_window(windows[0])  # 切换窗口
        self.driver.find_element_by_id("TANGRAM__PSP_11__footerULoginBtn").click()
        self.driver.find_element_by_id("TANGRAM__PSP_11__userName").send_keys("username")
        self.driver.find_element_by_id("TANGRAM__PSP_11__password").send_keys("13200000000")
        self.driver.find_element_by_id("TANGRAM__PSP_11__submit").click()

        sleep(3)
