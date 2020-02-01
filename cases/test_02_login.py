"""
Time:2020/2/1 0001
"""
import unittest
from libs.ddt import ddt, data
from scripts.handle_excel import HandleExcel
from scripts.handle_request import HandleRequests
from scripts.handle_conf import hy
from scripts.handle_mysql import HandleMysql
from scripts.handle_re import HandleRe
from scripts.handle_log import my_logger


@ddt
class TestLogin(unittest.TestCase):
    obj_li = HandleExcel('login')
    cases = obj_li.read_excel()

    @classmethod
    def setUpClass(cls) -> None:
        cls.hr = HandleRequests()
        cls.hm = HandleMysql()
        cls.hr.common_heads({hy.read_yaml('request', 'request_head'): hy.read_yaml('request', 'request_value')})

    @classmethod
    def tearDownClass(cls) -> None:
        cls.hr.close()
        cls.hm.close()

    @data(*cases)
    def test_register(self, case):
        url = hy.read_yaml('request', 'base_url') + case.url
        data = HandleRe.handle_para(case.data)
        res = self.hr.send(url=url, data=data)
        try:
            self.assertListEqual([case.expected, case.msg], [res.json()['code'], res.json()['msg']],
                                 msg=f'用例{case.title}执行完成')
            self.obj_li.write_excel(int(case.caseId) + 1, 8, value=str(res.json()))
        except AssertionError as e:
            my_logger.error(f'用例{case.title}断言失败')
            self.obj_li.write_excel(int(case.caseId) + 1, 7, value='fail')
            raise e
        else:
            my_logger.info(f'用例{case.title}断言成功')
            self.obj_li.write_excel(int(case.caseId) + 1, 7, value='success')