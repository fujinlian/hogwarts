# 【01】python unittest测试框架
import unittest


class TestStringMethods(unittest.TestCase):
    # 以下每个方法/测试用例 运行前后都执行
    def setUp(self) -> None:  # 默认返回值是None
        print('setup')

    def tearDown(self) -> None:
        print('teardown')

    # 以下2个是类级别的方法，需要加上装饰器@classmethod；在整个类的前后调用
    @classmethod
    def setUpClass(cls) -> None:
        print('set up class')

    @classmethod
    def tearDownClass(cls) -> None:
        print('teardown class')

    def test_abc(self):
        print('test abc')

    def test_upper(self):
        print('test_upper 111')
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        print('test_isupper 222')
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        print('test_split 333')
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == '__main__':
    unittest.main()
