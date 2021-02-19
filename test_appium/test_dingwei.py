# 【03】元素定位方法与隐式等待

from appium import webdriver
import time

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0'
desired_caps['deviceName'] = 'emulator-5554'
desired_caps['appPackage'] = 'com.xueqiu.android'
desired_caps['appActivity'] = 'com.xueqiu.android.common.MainActivity'
desired_caps['dontStopAppOnReset'] = 'true'  # 页面停留在哪个页面上就会继续基于操作，不去每次都从头开始启动app
desired_caps['skipDeviceInitialization'] = 'true'  # 跳过一些安装、权限设置等操作，可以提升运行速度；用例多的时候效果很明显

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(5)
driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()  # 未点击输入框之前
driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("alibaba")  # 点击输入框后跳转到搜索页面；跟以上是不同页面的不同组建
time.sleep(3)
# driver.find_element_by_accessibility_id("Accessibility Node Provider")
driver.back()  # 返回上一页
driver.back()  # 返回上一页，即回到了首页
driver.quit()
