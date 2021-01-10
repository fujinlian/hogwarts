# 【02】pytest测试框架
# content of test_sample.py
import pytest


def func(x):
    return x + 1


# 参数化前
# def test_answer():
#     assert func(3) == 5
# 参数化后
@pytest.mark.parametrize('a,b', [(1, 2), (10, 20), ('a', 'a1')])
def test_answer(a, b):
    assert func(a) == b


# 一旦加入下面这行，login就不是普通方法了，是装饰器
@pytest.fixture()
def login():
    print("登录操作")
    username = 'Lily'
    return username


class TestDemo:
    # 传入login，代表了以上login函数返回的结果。在这条用例执行前，会先去执行login登录、其他用例则不会
    def test_a(self, login):
        print(f"a username = {login}")

    def test_b(self):
        print("b")

    def test_c(self):  # 不满足测试用例命名，不会当作用例执行
        print(f"c username = {login}")


# python解释器的入口函数
if __name__ == '__main__':
    # 以下运行的，跟命令行运行的是一样的。可以指定运行某个类。-v加上详细的打印日志
    pytest.main(['test_a.py::TestDemo', '-v'])
