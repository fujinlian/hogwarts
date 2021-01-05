import yaml
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    # 把所有实例化的操作丢到init里面
    def __init__(self, base_driver=None):  # base_driver是我们设定的参数
        # 注解，不是一个赋值操作。用作ide的类型提示？
        base_driver: WebDriver
        if base_driver is None:
            self.driver = webdriver.Chrome()  # 实例化，会弹窗一个浏览器窗口
            self.driver.get("https://work.weixin.qq.com/wework_admin/frame")  # 打开企业微信页面
            self.__cookie_login()  # 调用cookie登录
        else:
            self.driver = base_driver
        self.driver.implicitly_wait(3)

    def __cookie_login(self):
        # 使用cookie登录
        with open("data.yaml", encoding="UTF-8") as f:
            yaml_data = yaml.safe_load(f)
            for cookie in yaml_data:
                self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")  # 打开登录的页面

    # 因为多个page代码使用到多次self.driver.find_element，所以把它封装成find方法，使用的时候直接调用find即可
    def find(self, by, value=None):
        if value is None:
            return self.driver.find_element(*by)  # 如果value=None,就对by进行解元组/解元组前只有一个参数/因此是by的位置。效果：解元组那里可以不加*进行解元组了
        else:
            return self.driver.find_element(by=by, value=value)

    def finds(self, by, value=None):
        if value is None:
            # 如果传入的是一个元祖，则进行解包元祖传参
            return self.driver.find_elements(*by)  # 如果value=None,就对by进行解元组/解元组前只有一个参数/因此是by的位置。效果：解元组那里可以不加*进行解元组了
        else:
            # 如果传入的是正常的定位信息，则正常传参
            return self.driver.find_elements(by=by, value=value)

    def wait_click(self, locator):
        """
        显示等待封装。等到元素locator出现后再往下进行，就可以使用该方法
        :return:
        """
        return WebDriverWait(self.driver, 9).until(expected_conditions.element_to_be_clickable(locator))

    def quit(self):
        """
        退出二次封装
        :return:
        """
        self.driver.quit()
