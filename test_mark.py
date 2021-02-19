# 【07】python pytest测试实战（12.13）
import pytest


class Test_demo():
    @pytest.mark.demo  # 加标签
    def test_demo(self):
        print("我的第一个用例")

    @pytest.mark.smoke  # 冒烟用例
    @pytest.mark.demo
    def test_two(self):
        print("我的第二个用例")

    @pytest.mark.flaky(reruns=6, reruns_delay=1)
    def test_three(self):
        print("我的第三个用例")
        assert 1 == 2
