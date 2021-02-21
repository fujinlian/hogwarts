# 【21】企业微信接口测试实战2021.1.31 ——封装的方法/类似po模式，这个是测试用例

from test_requests.req_page.contact import Contact
import pytest


class TestContact:

    def setup_class(self):
        self.contact = Contact()  # 初始化实例
        self.userid = "hello123"
        self.name = "hello_today"

    # token部分的封装，已完成，其他的类似
    @pytest.mark.parametrize("corpid,corpsecret,result", [(None, None, 0), ('', None, 41002), (None, '', 41004)])
    def test_token(self, corpid, corpsecret, result):
        r = self.contact.get_token(corpid, corpsecret)
        assert r.get('errcode') == result

    # 创建成员的测试用例封装，其中alias对应的是被测代码里面的其他参数部分**kwargs，别名
    def test_create(self):

        self.contact.create_member(userid=self.userid, name=self.name, mobile="13192837484", department=[1],
                                   alias="bieming")
        # 异常：如果创建发生异常、整个运行就会报错，如果不异常、执行到下面逻辑：删除语句无论如何都执行，而对try里面的查询的语句进行判断异常？？？
        try:
            find_result = self.contact.find_member(self.userid)
        finally:
            self.contact.delete_member(self.userid)  # 数据清理
        assert find_result["name"] == self.name  # 正常思路应该是，先断言错误码先要是0，再断言这个name。删除前已经存到了变量find_result中，所以不影响断言

    def test_update(self):
        # 更新之前先进行创建，确保可以有数据进行更新。保持跟创建用例的独立性，互不影响。重要！
        self.contact.create_member(userid=self.userid, name=self.name, mobile="13192837484", department=[1],
                                   alias="bieming")
        changed_mobile = '13192830000'
        self.contact.update_member(self.userid, self.name, changed_mobile)
        try:
            find_result = self.contact.find_member(self.userid)
        finally:
            self.contact.delete_member(self.userid)  # 数据清理
        assert find_result["mobile"] == changed_mobile

    def test_delete(self):
        self.contact.create_member(userid=self.userid, name=self.name, mobile="13192837484", department=[1],
                                   alias="bieming")
        r = self.contact.delete_member(self.userid)
        print(r)
        assert r.get('errcode') == 0

    # 查找函数里面执行查找前，需要先做数据的创建、确保可以查到，查找之后做数据的删除/数据清理工作
    @pytest.mark.parametrize("userid,name", [("fjl1", "fjl1"), ("fjl3", "fjl3"), ("fjl2", "小柯南")])
    def test_find(self, userid, name):
        r = self.contact.find_member(userid)
        print(r)
        assert name in r["name"]
