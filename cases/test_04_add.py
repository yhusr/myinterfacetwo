"""
Time:2020/2/1 0001
"""
import unittest
import decimal
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
    obj_li = HandleExcel('add')
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
        borrower_id = self.hl.read_yaml('borrower', 'id')
        result = self.hm.get_mysql_result(hy.read_yaml('mysql', 'loan_amount_sql'), arg=borrower_id)
        before_send_amount = 0
        if result['amount']:
            before_send_amount = result['amount']
        res = self.hr.send(url=url, data=data)
        if case.caseId == 2:
            invest_token = res.json()['data']['token_info']['token']
            self.hr.common_heads({'Authorization':'Bearer ' + invest_token})
        try:
            after_result = self.hm.get_mysql_result(hy.read_yaml('mysql', 'loan_amount_sql'), arg=borrower_id)
            if case.caseId == 3:
                after_send_amount = after_result['amount']
                amount_num = round((after_send_amount-before_send_amount), 2)
                expected_result = float(eval(case.data)['amount'])
                self.assertTrue(amount_num == expected_result)
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

