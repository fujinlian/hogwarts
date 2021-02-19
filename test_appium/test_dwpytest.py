# 【04】app控件定位;将test_dingwei.py转换为pytest的模式

import pytest
from appium import webdriver


class TestDW():
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['appActivity'] = 'com.xueqiu.android.common.MainActivity'
        desired_caps['dontStopAppOnReset'] = 'true'  # 页面停留在哪个页面上就会继续基于操作，不去每次都从头开始启动app
        desired_caps['skipDeviceInitialization'] = 'true'  # 跳过一些安装、权限设置等操作，可以提升运行速度；用例多的时候效果很明显
        # 要在输入框中输入中文"阿里巴巴"，需要添加以下2行
        desired_caps['unicodeKeyBoard'] = 'true'
        desired_caps['resetKeyBoard'] = 'true'
        # 以下需要增加self
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        # self.driver.back()
        # self.driver.back()
        self.driver.quit()

    def test_search(self):
        print("搜索测试用例")
        """
        1.打开 雪球 app
        2.点击搜索输入框
        3.向搜索输入框里面输入"阿里巴巴"
        4.在搜索结果里面选择"阿里巴巴"，然后进行点击
        5.获取 阿里巴巴的股价，并判断 这只股价的价格>200
        """
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()  # 未点击输入框之前
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys(
            "阿里巴巴")  # 点击输入框后跳转到搜索页面；跟以上是不同页面的不同组建
        self.driver.find_element_by_xpath(
            "//*[@resource-id='com.xueqiu.android:id/stockName' and @text='阿里巴巴']").click()
        current_price = float(self.driver.find_element_by_id("com.xueqiu.android:id/stock_current_price").text)
        assert current_price > 200


if __name__ == '__main__':
    pytest.main()
