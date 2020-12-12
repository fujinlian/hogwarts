import pytest


def add_function(a, b):
    return a + b


@pytest.mark.parametrize("a,b,expected", [(3, 5, 8), (-1, -2, -3), (1000, 1000, 2000)], ids=["case1", "case2", "case3"])
def test_add(a, b, expected):
    assert add_function(a, b) == expected

#
# class Test_demo():
#     def test_one(self):
#         a = 5
#         b = 1
#         assert a!=b
#         print("测试case")
#
#     def test_two(self):
#         a = 5
#         b = 1
#         assert a != b
#         print("测试case")
