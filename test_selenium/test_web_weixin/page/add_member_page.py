# 添加成员页面
from selenium.webdriver.common.by import By

from test_selenium.test_web_weixin.page.base_page import BasePage
from test_selenium.test_web_weixin.page.contact_page import ContactPage
from selenium import webdriver


class AddMember(BasePage):  # 继承类，可以使用init构造函数的实例变量driver
    # 前面加上_ 代表私有变量
    _location_username = (By.ID, "username")
    _location_acctid = (By.ID, "memberAdd_acctid")
    _location_Add_phone = (By.ID, "memberAdd_phone")

    def add_member(self):
        """添加成员操作
                ：return:
                """
        # driver = webdriver.Chrome()  #实例化，会弹窗一个浏览器窗口
        # 为什么location_username上面不需要加self，而下面需要？？以下多一个括号？？
        self.driver.find_element(*self._location_username).send_keys("赫敏2")
        self.driver.find_element(*self._location_acctid).send_keys("0091")
        self.driver.find_element(*self._location_Add_phone).send_keys("13766665556")
        self.driver.find_element_by_css_selector(".js_btn_save").click()

        return ContactPage(self.driver)  # 添加完成员之后回到通讯录页面，return

    def add_member_fail(self, acctid, phone):
        self.driver.find_element(*self._location_username).send_keys("赫敏2")
        self.driver.find_element(*self._location_acctid).send_keys(acctid)
        self.driver.find_element(*self._location_Add_phone).send_keys(phone)
        self.driver.find_element_by_css_selector(".js_btn_save").click()
        # 获取"账号"字段的报错信息：该账号已被"赫敏2"占有
        # error_message = self.driver.find_element(By.CSS_SELECTOR,".member_edit_item_right.ww_inputWithTips_WithErr .ww_inputWithTips_tips").text
        # phone_error_message = self.driver.find_element(By.CSS_SELECTOR,".member_edit_item_right.ww_inputWithTips_WithErr .ww_inputWithTips_tips").text
        # error_list = [error_message,phone_error_message]
        res = self.finds(By.CSS_SELECTOR, ".ww_inputWithTips_tips")
        print(res)
        error_list = [i.text for i in res]
        print(error_list)
        # print(error_message)
        return error_list
