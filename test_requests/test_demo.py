import requests
from jsonpath import jsonpath  # 导入想要的jsonpath方法
from hamcrest import *


class TestDemo:
    # 【13】服务端接口自动化测试——接口测试框架
    def test_get(self):
        r = requests.get('https://httpbin.testing-studio.com/get')
        print(r)  # 返回的实际是一个response对象
        print(r.status_code)
        print(r.text)  # 响应文本
        print(r.json())
        assert r.status_code == 200

    # 【14】服务端接口自动化测试——接口请求构造
    def test_query(self):
        payload = {
            "level": 1,
            "name": "seveniruby"
        }
        r = requests.get('https://httpbin.testing-studio.com/get', params=payload)
        print(r.status_code)
        print(r.text)  # 响应文本
        assert r.status_code == 200

    def test_post_form(self):
        payload = {
            "level": 1,
            "name": "seveniruby"
        }
        r = requests.post('https://httpbin.testing-studio.com/post', data=payload)
        print(r.status_code)
        print(r.text)  # 响应文本
        assert r.status_code == 200

    # 【15】服务端接口自动化测试——接口测试断言
    def test_header(self):
        r = requests.get('https://httpbin.testing-studio.com/get', headers={"h": "header demo"})
        print(r.status_code)
        print(r.text)  # 响应文本
        print(r.json())
        assert r.status_code == 200
        assert r.json()["headers"]["H"] == "header demo"  # 断言，沿着json结构体一层层找元素

    # 【16】服务端接口自动化测试——json xml请求
    def test_post_form(self):
        payload = {
            "level": 1,
            "name": "seveniruby"
        }
        r = requests.post('https://httpbin.testing-studio.com/post', json=payload)
        print(r.status_code)
        print(r.text)  # 响应文本
        assert r.status_code == 200
        assert r.json()["json"]["level"] == 1

    # 【17】服务端接口自动化测试——json xml响应断言
    def test_post_form(self):
        r = requests.get('https://ceshiren.com/categories.json')
        print(r.status_code)
        print(r.text)  # 响应文本
        assert r.status_code == 200
        # assert r.json()["category_list"]["categories"]["name"] == "开源项目"   #这样写是错的，因为这个是一个数组、一个列表
        assert r.json()["category_list"]["categories"][0]["name"] == "开源项目"
        print(jsonpath(r.json(), '$..name'))  # 可以打印看看取出来的是什么？
        assert jsonpath(r.json(), '$..name')[0] == "开源项目"  # 深度递归找name，取找到的第一个值

    # hamcrest断言
    def test_hamcrest(self):
        r = requests.get('https://ceshiren.com/categories.json')
        print(r.status_code)
        print(r.text)  # 响应文本
        assert r.status_code == 200
        # assert r.json()["category_list"]["categories"]["name"] == "开源项目"   #这样写是错的，因为这个是一个数组、一个列表
        assert_that(r.json()["category_list"]["categories"][0]["name"], equal_to("开源项目"))  # 使用匹配器equal_to
