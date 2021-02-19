import pytest


# 加一个装饰器
# @pytest.fixture()
# def myfixture():
#     print("执行我的fixture")

class Test_demo():
    def test_one2(self, myfixture):
        print("执行test_one2")
        assert 2 + 3 == 5

    def test_two2(self, myfixture):
        print("执行test_two2")
        assert 1 == 1

    def test_three2(self, connectdb):
        print("执行test_three2")
        assert 1 + 1 == 2
