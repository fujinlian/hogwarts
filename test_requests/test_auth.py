# 【20】服务端接口自动化测试——认证体系

import requests
from requests.auth import HTTPBasicAuth


def test_auth():
    r = requests.get(url="https://httpbin.testing-studio.com/basic-auth/banana/123",
                     auth=HTTPBasicAuth("banana", "123"))
    print(r.text)
