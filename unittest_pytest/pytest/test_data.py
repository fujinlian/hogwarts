# 【03】参数化用例
import pytest

# 使用string
import yaml


class TestData:
    @pytest.mark.parametrize("a,b", [(10, 20), (10, 5), (3, 9)])
    def test_data(self, a, b):
        print(a + b)


# 使用list
class TestData1:
    @pytest.mark.parametrize(["c", "d"], [(10, 20), (10, 5), (3, 9)])
    def test_data1(self, c, d):
        print(c + d)


# 使用元祖
class TestData2:
    @pytest.mark.parametrize(("e", "f"), [(10, 20), (10, 5), (3, 9)])
    def test_data2(self, e, f):
        print(e + f)


# 使用yaml
class TestData3:
    @pytest.mark.parametrize(("x", "y"), yaml.safe_load(open("./data.yaml")))
    def test_data3(self, x, y):
        print(x + y)
