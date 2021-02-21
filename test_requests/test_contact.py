# 【21】企业微信接口测试实战2021.1.28

import requests


# 获取企业微信的token，因为是共用的步骤，所以可以封装成一个函数：
def get_token():
    r = requests.get(
        'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww490da723739d6f3a&corpsecret=CUlQRat9gYLG_gkXKpOl_e-Ev4-Msy_B9LmUsZVSOco')
    # print(type(r))      #response对象
    # print(r.json())
    token = (r.json()['access_token'])  # 提取token字段
    return token
    # assert 0 == r.json()['errcode']

    # 读取成员，get请求：请求信息更多在请求url中


def test_defect_member():
    get_member_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={get_token()}&userid=fjl2'
    r = requests.get(get_member_url)
    print(r.json())
    assert '柯南' == r.json()['name']

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

    # 创建成员


def test_create_member():
    create_member_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={get_token()}'
    data = {
        "userid": "f123",
        "name": "小红",
        "mobile": "13804730000",
        "department": [1]
    }  # data里面填的就是post的请求体的字段，必填字段至少填

    r = requests.post(url=create_member_url, json=data)
    print(r.json())

    # 删除成员


def test_delete_member():
    delete_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={get_token()}&userid=f123'  # 以上"张三"的
    r = requests.get(delete_url)
    print(r.json())
