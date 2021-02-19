# 【07】python pytest测试实战（12.13）
from time import sleep

import pytest


class Test_demo():
    @pytest.mark.flaky(reruns=6)
    def test_three(self):
        print("我的第三个用例")
        assert 1 == 2

    def test_one_0(self):
        sleep(1)
        assert 1 == 1

    def test_one_1(self):
        sleep(1)
        assert 1 == 1

    def test_one_2(self):
        sleep(1)
        assert 1 == 1

    def test_one_3(self):
        sleep(1)
        assert 1 == 1

    def test_one_4(self):
        sleep(1)
        assert 1 == 1

    def test_one_5(self):
        sleep(1)
        assert 1 == 1

    @pytest.mark.run(order=2)  # 让第二个执行
    def test_one_6(self):
        sleep(1)
        assert 1 == 1

    @pytest.mark.run(order=1)  # 让第一个执行
    def test_one_7(self):
        sleep(1)
        assert 1 == 1
