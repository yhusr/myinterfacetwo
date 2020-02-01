"""
Time:2020/2/1 0001
"""
import unittest
from libs.ddt import ddt, data
from scripts.handle_excel import HandleExcel
from scripts.handle_request import HandleRequests
from scripts.handle_conf import hy, HandleYaml
from scripts.handle_mysql import HandleMysql
from scripts.handle_re import HandleRe
from scripts.handle_log import my_logger
from scripts.handle_os import PHONE_PATH


@ddt
class TestLogin(unittest.TestCase):
    obj_li = HandleExcel('recharge')
    cases = obj_li.read_excel()

    @classmethod
    def setUpClass(cls) -> None:
        cls.hr = HandleRequests()
        cls.hm = HandleMysql()
        cls.hl = HandleYaml(PHONE_PATH)
        cls.hr.common_heads({hy.read_yaml('request', 'request_head'): hy.read_yaml('request', 'request_value')})

    @classmethod
    def tearDownClass(cls) -> None:
        cls.hr.close()
        cls.hm.close()

    @data(*cases)
    def test_register(self, case):
        url = hy.read_yaml('request', 'base_url') + case.url
        data = HandleRe.handle_para(case.data)
        invest_phone = self.hl.read_yaml('investor', 'mobile_phone')
        before_send_amount = 0
        if case.sql:
            phone_result = self.hm.get_mysql_result(case.sql, arg=invest_phone)
            if phone_result['amount']:
                before_send_amount = float(phone_result['amount'])
        res = self.hr.send(url=url, data=data)
        if case.caseId == 2:
            invest_token = res.json()['data']['token_info']['token']
            self.hr.common_heads({'Authorization':'Bearer ' + invest_token})
        try:
            if case.sql:
                after_send_amount = float(self.hm.get_mysql_result(case.sql, arg=invest_phone)['amount'])
                amount_num = round((after_send_amount-before_send_amount), 2)
                self.assertTrue(amount_num == eval(case.data)['amount'])
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

