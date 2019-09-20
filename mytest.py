import unittest
from BeautifulReport import BeautifulReport as BF


class TestT(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("setUpClass")

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')

    def test_1(self):
        """
        测试相等
        :return:
        """
        unittest.TestCase.assertEqual(self, 3, 3, msg='测试失败')

    def test_2(self):
        """
        测试大于
        :return:
        """
        unittest.TestCase.assertGreater(self, 4, 6, msg='测试失败')


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTests([TestT('test_1'), TestT('test_2')])
    # runner = unittest.TextTestRunner()
    # runner.run(suite)

    run = BF(suites=suite)  # 实例化BeautifulReport模块
    # run.report(filename='test', description='这个描述参数是必填的')
    # run.report(filename='test2', description='这个描述参数是必填的', theme='theme_cyan')
    # run.report(filename='test3', description='这个描述参数是必填的', theme='theme_candy')
    run.report(filename='report.html', description='这个描述参数是必填的', theme='theme_memories')
