# 类似对研发代码撰写的测试用例
import pytest
from pythoncode.calculator import Calculator


class TestCalc:
    def setup_class(self):
        self.cal = Calculator()
        print("开始计算")

    def teardown_class(self):
        print("结束计算")

    @pytest.mark.parametrize("a,b,expect", [(3, 5, 8), (-1, -2, -3)], ids=["add1", "add2"])
    def test_add(self, a, b, expect):
        assert expect == self.cal.add(a, b)

    @pytest.mark.parametrize("a,b,expect", [(3, 5, -2), (99, 44, 55)], ids=["sub1", "sub2"])
    def test_sub(self, a, b, expect):
        assert expect == self.cal.sub(a, b)

    @pytest.mark.parametrize("a,b,expect", [(3, 5, 15), (99, 2, 198)], ids=["mul1", "mul2"])
    def test_mul(self, a, b, expect):
        assert expect == self.cal.mul(a, b)

    @pytest.mark.parametrize("a,b,expect", [(10, 5, 2), (99, 2, 49.5)], ids=["div1", "div2"])
    def test_div(self, a, b, expect):
        assert expect == self.cal.div(a, b)
