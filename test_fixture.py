import pytest


# 加一个装饰器
# @pytest.fixture()
# def myfixture():
#     print("执行我的fixture")

class Test_demo():
    def test_one(self, myfixture):
        print("执行test_one")
        myenv = myfixture
        print("------in test one %s" % myenv)
        assert 2 + 3 == 5

    def test_two(self):
        print("执行test_two")
        assert 1 == 1

    def test_three(self):
        print("执行test_three")
        assert 1 + 1 == 2
