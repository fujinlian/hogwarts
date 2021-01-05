# 通讯录页面建模
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_selenium.test_web_weixin.page.base_page import BasePage


class ContactPage(BasePage):
    _location_member_list = (By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
    _location_goto_add_member = (By.CSS_SELECTOR, ".ww_operationBar .js_add_member")

    def goto_add_member(self):
        # 解决循环导入的问题
        from test_selenium.test_web_weixin.page.add_member_page import AddMember
        """添加成员操作
                ：return:
                """
        # 添加显示等待，保证按钮可以点击
        # WebDriverWait(self.driver,9).until(expected_conditions.element_to_be_clickable(self._location_goto_add_member))
        self.wait_click(self._location_goto_add_member)
        self.find(self._location_goto_add_member).click()
        return AddMember(self.driver)

    def get_member(self):
        """
        获取成员列表，用来做断言信息
        :return:
        """
        # 拿到列表元素
        # member_list = self.driver.find_elements(*self.location_member_list)
        member_list = self.finds(*self._location_member_list)

        member_list_res = [i.text for i in member_list]
        # 以上表达方式等同于以下3行。列表推导式
        # member_list2 = []
        # for i in member_list:
        #     member_list2.append(i.text)
        return member_list_res
