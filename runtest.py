import unittest
from BeautifulReport import BeautifulReport

# 用例存放位置
test_case_path = "E:/test/auto_test_local/Auto_Test/Test_Case"
# 测试报告存放位置
log_path = 'E:/test/auto_test_local/Auto_Test/Test_Result/Test_Report'
# 测试报告名称
filename = '测试报告-百度'
# 用例名称
description = '百度登录'
# 需要执行哪些用例，如果目录下的全部，可以改为"*.py"，如果是部分带test后缀的，可以改为"*test.py"
pattern = "login_test.py"

if __name__ == '__main__':
    test_suite = unittest.defaultTestLoader.discover(test_case_path, pattern=pattern)
    result = BeautifulReport(test_suite)
    result.report(filename=filename, description=description, log_path=log_path)
