"""
Time:2020/1/31 0031
"""
import unittest
import pytest
from scripts.handle_os import strtime, CASE_PATH, REPORT_PATH
from HTMLTestRunnerNew import HTMLTestRunner

# class Run:
#
#     @staticmethod
#     def run_my_test():
#         unit = unittest.defaultTestLoader.discover(CASE_PATH)
#         runner = HTMLTestRunner(stream=open(REPORT_PATH,'wb'),
#                                 tester='y.h',
#                                 description='这是我的接口测试',
#                                 title='接口测试')
#         runner.run(unit)


if __name__ == '__main__':
    pytest.main(["--reruns", "2", "--reruns-delay", "5",
                 "--junitxml=reports/allure.xml"])
