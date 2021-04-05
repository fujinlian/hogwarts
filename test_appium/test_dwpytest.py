# 【04】app控件定位;将test_dingwei.py转换为pytest的模式
# 【05】app控件交互
from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class TestDW():
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['appPackage'] = 'com.xueqiu.android'
        # desired_caps['appActivity'] = '.common.MainActivity' #也可以写com.xueqiu.android.common.MainActivity
        desired_caps['appActivity'] = '.view.WelcomeActivityAlias'
        desired_caps['dontStopAppOnReset'] = 'true'  # 页面停留在哪个页面上就会继续基于操作，不去每次都从头开始启动app
        desired_caps['skipDeviceInitialization'] = 'true'  # 跳过一些安装、权限设置等操作，可以提升运行速度；用例多的时候效果很明显
        # 要在输入框中输入中文"阿里巴巴"，需要添加以下2行
        desired_caps['unicodeKeyBoard'] = 'true'
        desired_caps['resetKeyBoard'] = 'true'
        # 以下需要增加self
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

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
        # self.driver.find_element_by_xpath(
        #    "//*[@resource-id='com.xueqiu.android:id/stockName' and @text='阿里巴巴']").click()
        # 因为切换了欢迎页，默认到"热门"页，之前写的定位不到元素，重新写如下：
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()
        self.driver.find_element_by_xpath(
            "//*[@resource-id='com.xueqiu.android:id/stockName' and @text='阿里巴巴']").click()

        current_price = float(self.driver.find_element_by_id("com.xueqiu.android:id/stock_current_price").text)
        assert current_price > 200

    # 【05】app控件交互
    def test_attr(self):
        """
        打开【雪球】应用首页
        定位首页的搜索框
        判断搜索框是否可用，并查看搜索框name属性值
        打印搜索框这个元素的左上角坐标和它的宽高
        向搜索框输入：alibaba
        判断【阿里巴巴】是否可见
        如果可见，打印"搜索成功"点击，如果不可见，打印"搜索失败"
        :return:
        """
        element = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")  # 未点击输入框之前
        # print(element.is_enabled())
        search_element = element.is_enabled()
        print(element.text)  # 打印搜索框name属性值
        print(element.location)  # 打印左上角坐标
        print(element.size)  # 打印宽高
        if search_element == True:
            element.click()
            self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("alibaba")
            # alibaba_element = self.driver.find_element_by_xpath(
            #    "//*[@resource-id='com.xueqiu.android:id/stockName' and @text='阿里巴巴']")
            alibaba_element = self.driver.find_element_by_xpath(
                "//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']")
            # print(alibaba_element.get_attribute("displayed"))
            element_display = alibaba_element.get_attribute("displayed")
            if element_display == 'true':
                print("搜索成功")
            else:
                print("搜索失败")

    # 【06】触屏操作自动化
    def test_touchaction(self):
        action = TouchAction(self.driver)
        # 滑动太快，手机可能没反应那么快、加一个等待200ms。使用坐标点的方式不灵活，可能会变化，手机不同可能也不一样
        window_rect = self.driver.get_window_rect()  # {'width': 1170, 'height': 1872, 'x': 0, 'y': 0}获取像素
        width = window_rect['width']
        height = window_rect['height']
        x1 = int(width / 2)
        y_start = int(height * 4 / 5)
        y_end = int(height * 1 / 5)
        action.press(x=x1, y=y_start).wait(200).move_to(x=x1, y=y_end).release().perform()

    # 【07】高级定位技巧
    def test_get_current(self):
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()  # 未点击输入框之前
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys(
            "阿里巴巴")  # 点击输入框后跳转到搜索页面；跟以上是不同页面的不同组建
        # self.driver.find_element_by_xpath(
        #    "//*[@resource-id='com.xueqiu.android:id/stockName' and @text='阿里巴巴']").click()
        # 因为切换了欢迎页，默认到"热门"页，之前写的定位不到元素，重新写如下：
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()
        current_price = self.driver.find_element_by_xpath(
            "//*[@text=09988]/../../..//*[@resource-id='com.xueqiu.android:id/current_price']").text
        print(f"当前09988 对应的股票价格是：{current_price}")
        assert float(current_price) > 200

    # 【07】高级定位技巧
    def test_myinfo(self):
        """
        1，点击我的，进入到个人信息页面
        2，点击登录，进入到登录页面
        3，输入用户名，输入密码
        4，点击登录
        :return:
        """
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("我的")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("帐号密码")').click()
        # self.driver.find_element_by_android_uiautomator('new UiSelector().text("帐号密码登录")').click()
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("com.xueqiu.android:id/login_account")').send_keys("123456")
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("com.xueqiu.android:id/login_password")').send_keys("123456")
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("com.xueqiu.android:id/button_next")').click()

    # 【07】高级定位技巧 --滚动查找
    def test_scroll_find_element(self):
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("关注")').click()
        self.driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("丁菲特").instance(0));').click()
        sleep(5)


# 入口函数
if __name__ == '__main__':
    pytest.main()
