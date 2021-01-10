# 【05】测试报告美化与定制。demo
import allure
import pytest


def test_with_no_severity_label():
    pass


# 定义测试用例级别：可以在类上面（作为类级别的装饰器），方法上面
@allure.severity(allure.severity_level.TRIVIAL)
def test_with_trivial_severity():
    pass


@allure.severity(allure.severity_level.NORMAL)
def test_with_normal_severity():
    pass


@allure.severity(allure.severity_level.NORMAL)
class TestClassWithNormalSeverity(object):

    def test_inside_the_normal_severity_test_class(self):
        pass

    @allure.severity(allure.severity_level.CRITICAL)
    def test_inside_the_normal_severity_test_with_overriding_critical_(self):
        pass


if __name__ == '__main__':
    pytest.main()
