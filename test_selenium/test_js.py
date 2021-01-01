# 09执行javascript脚本
import time
from test_selenium.base import Base
from selenium import webdriver
import pytest


class TestJS(Base):
    @pytest.mark.skip
    def test_js_scroll(self):
        self.driver.get("http://www.baidu.com")
        self.driver.find_element_by_id("kw").send_keys("selenium测试")
        # 在selenium中，执行js的代码块的方式，执行我们想要获取的元素或者执行
        element = self.driver.execute_script("return document.getElementById('su')")
        element.click()
        # 滑动到最下面的页
        self.driver.execute_script("document.documentElement.scrollTop=10000")
        time.sleep(3)
        # 点击下一页
        self.driver.find_element_by_xpath("//*[@id='page']/div/a[10]").click()
        time.sleep(3)

        # 其他的常用方法
        # for code in [
        #     'return document.title','return JSON.stringify(performance.timing)'
        # ]:
        #     print(self.driver.execute_script(code)) #不加print，只加return的话默认不会打印出来
        print(self.driver.execute_script(
            "return document.title;return JSON.stringify(performance.timing)"))  # 效果等同于以上4行代码，但只打印第一个脚本

    def test_datetime(self):
        self.driver.get("https://www.12306.cn/index/")
        # 执行js代码
        time_element = self.driver.execute_script(
            "a=document.getElementById('train_date');a.removeAttribute('readonly')")
        self.driver.execute_script("document.getElementById('train_date').value='2020-12-30'")
        time.sleep(3)
        print(self.driver.execute_script("return document.getElementById('train_date').value"))
        time.sleep(3)
