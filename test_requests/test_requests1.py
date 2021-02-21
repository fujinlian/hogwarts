# 【19】服务端接口自动化测试——header cookie处理

import requests


# 第一种传递cookie方法：请求头header传递
def test_demo():
    url = "https://httpbin.testing-studio.com/cookies"
    header = {
        "Cookie": "hogwarts=school",
        'User-Agent': 'hogwarts'
    }  # Cookie 首字母一定要大写，要不然会认为不是cookie是别的东西；header还可以定制请求头信息
    r = requests.get(url=url, headers=header)  # 响应结果
    print(r.request.headers)  # 获取请求头信息


# 第二种传递cookie方法：cookies传递
def test_cookies():
    url = "https://httpbin.testing-studio.com/cookies"
    header = {
        'User-Agent': 'hogwarts'
    }  # Cookie 首字母一定要大写，要不然会认为不是cookie是别的东西；header还可以定制请求头信息
    cookie_data = {
        "hogwarts": "school",
        "teacher": "AD"
    }  # 可以传递1条或者多条cookie
    r = requests.get(url=url, headers=header, cookies=cookie_data)  # 响应结果
    print(r.request.headers)  # 获取请求头信息
