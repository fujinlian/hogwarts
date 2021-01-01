# 3种等待方式
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWait:
    def setup(self):
        # self.driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
        self.driver = webdriver.Chrome()
        self.driver.get("http://home.testing-studio.com/")
        self.driver.implicitly_wait(3)  # 隐式等待

    def test_wait(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, '//*[@class="activity sortable num"]')))
        # 以上，可以用selenium自带的方法，等同于下面3行；也可以自定义方法来使用
        # def wait(x): #需要加x，因为return函数调用
        #     return len(self.driver.find_elements(By.XPATH,'//*[@class="activity sortable num"]')) >= 1 #活动是否出现，浏览器-查找寻找
        # WebDriverWait(self.driver,10).until(wait)   #强制等待，python方法传参，不能写括号、只是传进来，如果写括号就是调用的意思
        self.driver.find_element(By.XPATH, '//*[@title="在最近的一年，一月，一周或一天最活跃的主题"]').click()
    # print("hello")
