# 【06】python pytest测试实战（12.09）
# 类似对研发代码撰写的测试用例555
import pytest
from pythoncode.calculator import Calculator


class TestCalc:
    # 因为生成实例是下面方法都需要生成的，可以抽离出来setup，使得代码不冗余
    def setup_class(self):
        self.cal = Calculator()
        print("开始计算")

    def teardown_class(self):
        print("结束计算")

    @pytest.mark.parametrize("a,b,expected", [(3, 5, 8), (-1, -2, -3), (1000, 1000, 2000)],
                             ids=["add1", "add2", "add3"])
    def test_add(self, a, b, expected):
        assert expected == self.cal.add(a, b)

    @pytest.mark.parametrize("a,b,expect", [(3, 5, -2), (99, 44, 55)], ids=["sub1", "sub2"])
    def test_sub(self, a, b, expect):
        assert expect == self.cal.sub(a, b)

    @pytest.mark.parametrize("a,b,expect", [(3, 5, 15), (99, 2, 198)], ids=["mul1", "mul2"])
    def test_mul(self, a, b, expect):
        assert expect == self.cal.mul(a, b)

    @pytest.mark.parametrize("a,b,expect", [(10, 5, 2), (99, 2, 49.5)], ids=["div1", "div2"])
    def test_div(self, a, b, expect):
        assert expect == self.cal.div(a, b)
