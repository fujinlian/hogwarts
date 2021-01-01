from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains
import pytest
from selenium.webdriver.common.keys import Keys


class TestActionChains():
    def setup(self):
        self.driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
        self.driver.maximize_window()  # 窗口最大化
        self.driver.implicitly_wait(5)  # 隐式等待，全局的，查找元素之前起作用；非常推荐；只能查找到元素，不知道元素是否可见、是否可点击

    def teardown(self):
        self.driver.quit()  # 浏览器的关闭，资源的回收

    # 案例一：进入页面模拟进行单击、双击、右键的操作，使用ActionChains方法
    @pytest.mark.skip  # 加了这个，执行时会跳过下面这一条用例
    def test_case_click(self):
        self.driver.get("http://sahitest.com/demo/clicks.htm")
        #  element_click = self.driver.find_element_by_xpath("/html/body/form/input[3]")
        # 上面可以定位，下面使用相对路径定位方法也可以定位? xath的语法是什么？
        elemenet_click = self.driver.find_element_by_xpath("//input[@value='click me']")
        elemenet_doubleclick = self.driver.find_element_by_xpath("//input[@value='dbl click me']")
        elemenet_rightclick = self.driver.find_element_by_xpath("//input[@value='right click me']")
        action = ActionChains(self.driver)  # 为什么一定要添加self？
        action.click(elemenet_click)
        action.double_click(elemenet_doubleclick)
        action.context_click(elemenet_rightclick)
        sleep(3)
        action.perform()
        sleep(3)

    # 案例二：ActionChains方法，鼠标光标移动到某个元素上
    @pytest.mark.skip  # 加了这个，执行时会跳过下面这一条用例
    def test_movetoelement(self):
        self.driver.get("https://www.baidu.com/")
        ele = self.driver.find_element_by_link_text("更多")  # 为什么改为设置时不成功，说找不到这个元素？
        action = ActionChains(self.driver)
        action.move_to_element(ele)
        action.perform()
        sleep(3)

    # 案例三：ActionChains方法，拖拽
    @pytest.mark.skip  # 加了这个，执行时会跳过下面这一条用例
    def test_dragdrop(self):
        self.driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
        drag_element = self.driver.find_element_by_id("dragger")
        drop_element = self.driver.find_element_by_xpath("/html/body/div[2]")
        action = ActionChains(self.driver)
        # 用以下三行的任意一行都可以
        # action.drag_and_drop(drag_element,drop_element).perform()
        # action.click_and_hold(drag_element).release(drop_element).perform()
        action.click_and_hold(drag_element).move_to_element(drop_element).release().perform()

        sleep(3)

    # 案例四：ActionChains方法，模拟键盘等操作
    #   @pytest.mark.skip  # 加了这个，执行时会跳过下面这一条用例
    def test_keys(self):
        self.driver.get("http://sahitest.com/demo/label.htm")
        ele = self.driver.find_element_by_xpath("/html/body/label[1]/input")
        ele.click()
        action = ActionChains(self.driver)
        action.send_keys("username").pause(1)  # 等待1s
        action.send_keys(Keys.SPACE).pause(1)
        action.send_keys("tom").pause(1)
        action.send_keys(Keys.BACK_SPACE).perform()
        sleep(3)


if __name__ == '_main_':
    pytest.main(['-v', '-s', 'test_ActionChains.py'])
