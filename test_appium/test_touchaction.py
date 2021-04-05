# 【06】触屏操作自动化
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class TestTouchAction():
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['appPackage'] = 'cn.kmob.screenfingermovelock'
        # desired_caps['appActivity'] = '.common.MainActivity' #也可以写com.xueqiu.android.common.MainActivity
        desired_caps['appActivity'] = 'com.samsung.ui.MainActivity'
        desired_caps['dontStopAppOnReset'] = 'true'  # 页面停留在哪个页面上就会继续基于操作，不去每次都从头开始启动app
        desired_caps['skipDeviceInitialization'] = 'true'  # 跳过一些安装、权限设置等操作，可以提升运行速度；用例多的时候效果很明显
        # 要在输入框中输入中文"阿里巴巴"，需要添加以下2行
        desired_caps['unicodeKeyBoard'] = 'true'
        desired_caps['resetKeyBoard'] = 'true'
        # 以下需要增加self
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_touchaction1(self):
        print("解锁手势密码")
        action = TouchAction(self.driver)
        action.press(x=196, y=266).wait(200).move_to(x=597, y=285).wait(200).move_to(x=972, y=251).wait(200) \
            .move_to(x=975, y=683).wait(200).move_to(x=979, y=1052).release().perform()
