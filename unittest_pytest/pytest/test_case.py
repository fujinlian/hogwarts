# 【05】测试报告美化与定制
import allure

# 可以让报告关联测试用例链接地址，以下地址可以随便填：
TEST_CASE_LINK = 'https://www.baidu.com/'


@allure.testcase(TEST_CASE_LINK, '测试链接')
def test_with_testcase_link():
    pass
