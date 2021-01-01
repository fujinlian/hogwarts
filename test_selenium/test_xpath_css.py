from selenium import webdriver
from selenium.webdriver.common.by import By


class TestWait:
    def setup(self):
        self.driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
        self.driver.get("https://www.baidu.com/")

    # self.driver.implicitly_wait(3)   #隐式等待
    def test_wait(self):
        # 元素定位，by是使用什么定位、以下是使用xpath定位
        # self.driver.find_element(By.XPATH,'//*[@id="kw"]').send_keys("霍格沃滋测试学院")
        # 使用id定位
        # self.driver.find_element(By.ID,'kw').send_keys("霍格沃滋测试学院")
        # 使用css定位
        self.driver.find_element(By.CSS_SELECTOR, '#kw').send_keys("霍格沃滋测试学院")
        # 使用css定位
        # self.driver.find_element(By.CSS_SELECTOR, '[id=kw]').send_keys("霍格沃滋测试学院")
        self.driver.find_element(By.ID, 'su').click()
