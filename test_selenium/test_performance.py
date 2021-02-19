# H5性能分析【录播】
from selenium import webdriver


class TestData:
    def test_data(self):
        driver = webdriver.Chrome()
        driver.get("https://home.testing-studio.com")
        # 对页面进行js的注入
        print(driver.execute_script("return JSON.stringify(window.performance.timing)"))
