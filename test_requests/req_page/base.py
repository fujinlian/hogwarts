# 【21】企业微信接口测试实战2021.1.31 ——封装base类，session封装


import requests
from requests import Session


class Base:
    def __init__(self):
        # 声明一个session，只创建了一个session，后面的都用这一个，不是每请求一次就创建一次/不用session之前是没请求一次创建一次
        self.s = Session()
        self.corpid = 'ww490da723739d6f3a'
        self.corpsecret = 'CUlQRat9gYLG_gkXKpOl_e-Ev4-Msy_B9LmUsZVSOco'
        self.s.params["access_token"] = self.get_token().get("access_token")  # 把token塞进session中

    # 因为以下2个参数可能会变的，因此作为参数可传，默认值可以不传，设置为None
    def get_token(self, corpid=None, corpsecret=None):
        if corpid is None:
            corpid = self.corpid
        if corpsecret is None:
            corpsecret = self.corpsecret

        # requests的用法，对于get请求，可以用params参数写法，等同于直接在url后面拼接参数
        params = {"corpid": corpid, "corpsecret": corpsecret}
        r = requests.get('https://qyapi.weixin.qq.com/cgi-bin/gettoken', params=params)
        # token = (r.json()['access_token'])  # 提取token字段，直接写字典容易有问题，建议用get取出来
        # token = r.json().get('access_token')
        # return token
        return r.json()
