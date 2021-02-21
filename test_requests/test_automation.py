# 【21】企业微信接口测试实战2021.1.31

import requests
import pytest


class TestContact:

    # 获取企业微信的token，因为是共用的步骤，所以可以封装成一个函数：
    def get_token(self):
        r = requests.get(
            'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww490da723739d6f3a&corpsecret=CUlQRat9gYLG_gkXKpOl_e-Ev4-Msy_B9LmUsZVSOco')
        # print(type(r))      #response对象
        # print(r.json())
        token = (r.json()['access_token'])  # 提取token字段
        return token
        # assert 0 == r.json()['errcode']

        # 创建成员

    def test_create_member(self):
        create_member_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.get_token()}'
        data = {
            "userid": "f123",
            "name": "小红",
            "mobile": "13804730000",
            "department": [1]
        }  # data里面填的就是post的请求体的字段，必填字段至少填

        r = requests.post(url=create_member_url, json=data)
        # assert 'created' == r.json().get('errmsg',None)  #断言

    def setup(self):
        self.test_create_member()

        # 删除成员

    def test_delete_member(self):
        delete_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.get_token()}&userid=f123'  # 以上"张三"的
        proxies = {"https": "127.0.0.1:8888"}
        r = requests.get(delete_url, proxies=proxies, verify=False)  # 代理抓包charles
        print(r.json())

    # 数据清洗（进行一个闭环，如：谁创建的数据、谁负责去清洗它）；方法级的teardown，每执行完一个方法就会调用一次，从而创建完又会删除
    def teardown(self):
        delete_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.get_token()}&userid=f123'  # 以上"张三"的
        r = requests.get(delete_url)
        print(r.json())


def get_token():
    r = requests.get(
        'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww490da723739d6f3a&corpsecret=CUlQRat9gYLG_gkXKpOl_e-Ev4-Msy_B9LmUsZVSOco')
    token = (r.json()['access_token'])  # 提取token字段
    return token

    # 读取成员/查询接口，get请求：请求信息更多在请求url中


@pytest.mark.parametrize("tmp", range(50))
def test_defect_member(tmp):
    get_member_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={get_token()}&userid=fjl2'
    r = requests.get(get_member_url)
    print(r.json())
    assert '小柯南' == r.json()['name']

    # 更新成员，post请求：请求信息更多在data、请求体中


def test_update_member():
    update_member_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={get_token()}'
    data = {
        "userid": "fjl2",
        "name": "小柯南",
        "mobile": "13800000111"
    }  # data里面填的就是post的请求体的字段，将"userid": "fjl2"的名字、手机号

    r = requests.post(url=update_member_url, json=data)
    print(r.json())


# 【22】企业微信接口测试实战2021.1.31
# 数据生成函数[边界值7点法]，pre是精度的意思
@pytest.mark.parametrize("left,right", [(2, 6), (3, 8), (4, 5)])
def test_generate(left, right, pre=1):
    result = []
    lefts = [left - pre, left, left + pre]
    rights = [right - pre, right, right + pre]
    mid = (left + right) // 2  # /代表python的除法、浮点数，//代表c语言的除法、类似四舍五入
    result += lefts
    result.append(mid)
    result += rights
    print(set(result))  # 将结果转换为集合
