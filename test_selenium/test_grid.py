# 跨平台设备管理方案 selenium grid【录播】
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver import Remote


class TestGrid:
    def test_grid(self):
        hub_url = "http://127.0.0.1:4444/wd/hub"
        # copy：对它的拷贝不影响原来的字典；官网的使用方式
        capability = DesiredCapabilities.CHROME.copy()
        for i in range(1, 5):
            # 倒入remote之后，可以远程连接hub；desired_capabilities 根据参数进行匹配node，hub就把脚本发送到node上
            driver = Remote(command_executor=hub_url, desired_capabilities=capability)
            # 因为循环写在一个线程中，所以会等待第一个get打开完成后才会进入下一次的循环
            driver.get("http://home.testing-studio.com/")
