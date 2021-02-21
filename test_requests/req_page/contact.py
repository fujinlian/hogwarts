# 【21】企业微信接口测试实战2021.1.31 ——封装的方法/类似po模式，这个是被测试的代码


import requests

from test_requests.req_page.base import Base


class Contact(Base):

    # 删除成员，封装
    def delete_member(self, userid):
        params = {"userid": userid}  # 因为把token已经放到了session中，所以此处token可以不需要了
        delete_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/delete'
        r = self.s.get(delete_url, params=params)
        return r.json()

        # 读取成员/查询接口，get请求：请求信息更多在请求url中

    def find_member(self, userid):
        params = {"userid": userid}
        get_member_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/get'
        r = self.s.get(get_member_url, params=params)
        return r.json()

        # 更新成员，post请求：请求信息更多在data、请求体中

    def update_member(self, userid: str, name: str, mobile: str, **kwargs):
        update_member_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/update'
        data = {
            "userid": userid,
            "name": name,
            "mobile": mobile
        }  # data里面填的就是post的请求体的字段，将"userid": "fjl2"的名字、手机号
        data.update(kwargs)
        r = self.s.post(url=update_member_url, json=data)
        return r.json()

        # 创建成员

    def create_member(self, userid: str, name: str, mobile: str, department, **kwargs):
        create_member_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/create'
        data = {
            "userid": userid,
            "name": name,
            "mobile": mobile,
            "department": department
        }  # data里面填的就是post的请求体的字段，必填字段至少填
        data.update(kwargs)
        r = self.s.post(url=create_member_url, json=data)
        return r.json()
