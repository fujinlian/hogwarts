# 企业微信首页建模
from selenium.webdriver.common.by import By

from test_selenium.test_web_weixin.page.add_member_page import AddMember
from test_selenium.test_web_weixin.page.base_page import BasePage
from test_selenium.test_web_weixin.page.contact_page import ContactPage
from selenium import webdriver


class MainPage(BasePage):
    _location_goto_member = (By.CSS_SELECTOR, ".ww_indexImg_AddMember")

    def goto_add_member(self):
        """跳转到添加成员页面
                ：return:
                """
        #  driver = webdriver.Chrome()  #实例化，会弹窗一个浏览器窗口
        # self.driver.find_element(By.CSS_SELECTOR,".ww_indexImg_AddMember").click()
        # 解元组操作，把元组内的元素拆分成为不同的参数传入
        # self.driver.find_element(*self._location_goto_member).click()
        # 封装find后，以上代码可使用以下代码替代
        self.find(self._location_goto_member).click()

        return AddMember(self.driver)  # 返回类的对象，实例化类。而该类也继承BasePage

    def goto_contact(self):
        """跳转到通讯录页面
                ：return:
                """
        self.find(by=By.ID, value="menu_contacts").click()
        return ContactPage(self.driver)  # 返回类的对象

    # 返回首页，确保执行完一遍添加成员，就返回到首页、接着才可以查找到元素进行第二遍添加成员
    def back_main(self):
        self.find(By.ID, "menu_index").click()
        self.find(By.CSS_SELECTOR, "a[node-type='cancel'").click()  # 点击"离开此页"弹窗
