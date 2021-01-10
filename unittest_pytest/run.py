# 【01】python unittest测试框架
import unittest

from unittest_pytest.HTMLTestRunner.HTMLTestRunner_PY3 import HTMLTestRunner

if __name__ == '__main__':
    # 以下3行：htmltestrunner报告相关
    report_title = '用例执行报告 我的标题'
    desc = '用于展示修改样式后的HTMLTestRunner'
    report_file = 'ExampleReport.html'  # 测试报告保存路径

    test_dir = './testcase'  # .代表当前工程目录，即1212pytest
    discover = unittest.defaultTestLoader.discover(test_dir, pattern="test_*.py")
    # unittest.TextTestRunner(verbosity=2).run(discover)

    # 以下是 htmltestrunner报告相关
    with open(report_file, 'wb') as report:
        runner = HTMLTestRunner(stream=report, title=report_title, description=desc)
        runner.run(discover)
