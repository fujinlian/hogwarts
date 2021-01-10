# 【05】测试报告美化与定制
import pytest
from selenium import webdriver
import time
import allure


@allure.testcase("http://www.github.com")  # 在测试报告里添加一个链接
@allure.feature("百度搜索")
@pytest.mark.parametrize('test_data1', ['allure', 'pytest', 'unittest'])  # 参数化测试用例功能，运行时动态执行3条测试用例
def test_steps_demo(test_data1):
    with allure.step("打开百度网页"):
        driver = webdriver.Chrome()
        driver.get("http://www.baidu.com")
        driver.maximize_window()

    with allure.step(f"输入搜索词：{test_data1}"):  # 参数化搜索词用例
        driver.find_element_by_id("kw").send_keys(test_data1)
        time.sleep(3)
        driver.find_element_by_id("su").click()
        time.sleep(3)

    with allure.step("保存图片"):
        driver.save_screenshot("./result/b.png")
        allure.attach.file("./result/b.png", attachment_type=allure.attachment_type.PNG)
    with allure.step("关闭浏览器"):
        driver.quit()
