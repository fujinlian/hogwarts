# 作业：登录企业微信——通讯录——添加成员——保存——在返回的列表页面进行验证
import pytest
import time
from time import sleep
import yaml
from selenium import webdriver


class TestWework:
    # 获取cookie的方法，复用浏览器
    def test_get_cookie(self):
        opt = webdriver.ChromeOptions()
        # 设置debug地址
        opt.debugger_address = "127.0.0.1:9222"
        driver = webdriver.Chrome(options=opt)
        driver.implicitly_wait(5)
        driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        cookie = driver.get_cookies()
        print(cookie)
        with open("data.yaml", "w", encoding="UTF-8") as f:
            yaml.dump(cookie, f)

    # 使用序列化cookie的方法进行登录。使用cookie登录所以就不需要复用了
    def test_login(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(5)
        driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")  # 打开扫描登录的页面
        # 读文件内容，open默认就是读
        with open("data.yaml", encoding="UTF-8") as f:
            yaml_data = yaml.safe_load(f)
            for cookie in yaml_data:
                driver.add_cookie(cookie)
        driver.get("https://work.weixin.qq.com/wework_admin/frame")  # 打开登录的页面
        driver.find_element_by_id("menu_contacts").click()
        print(driver.current_window_handle)  # 打印当前窗口
        print(driver.window_handles)  # 打印当前所有窗口
        time.sleep(3)
        # def test_addmember(self):
        #     driver =webdriver.Chrome()
        # 添加成员
        #  ele = driver.find_element_by_xpath("//*[@id='js_contacts49']/div/div[2]/div/div[2]/div[3]/div[1]/a[1]")
        ele = driver.find_element_by_link_text("添加成员")

        ele.click()
        sleep(3)
        driver.find_element_by_id("username").send_keys("fjl3")
        sleep(3)
        driver.find_element_by_id("memberAdd_acctid").send_keys("fjl3")
        driver.find_element_by_xpath("//*[@id='memberAdd_phone']").send_keys("18711112223")
        # save_ele = driver.find_element_by_xpath("//*[@id='js_contacts49']/div/div[2]/div/div[4]/div/form/div[3]/a[2]")
        save_ele = driver.find_element_by_link_text("保存")
        save_ele.click()

        sleep(3)

        # 断言。去找刚刚加的人的手机号
        iphone = driver.find_element_by_xpath('//*[@title="18711112223"]')
        # 断言如果匹配到了iPhone就说明添加成功了
        if iphone.text == '18711112223':
            pass
        else:
            raise Exception
