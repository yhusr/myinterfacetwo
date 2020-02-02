"""
Time:2020/1/31 0031
"""
import pytest
from scripts.handle_excel import HandleExcel
from scripts.handle_conf import hy
from scripts.handle_re import HandleRe
from scripts.handle_log import my_logger


@pytest.mark.usefixtures('set_up')
class TestRegister:
    obj_li = HandleExcel('register')
    cases = obj_li.read_excel()

    @pytest.mark.parametrize('case', cases)
    def test_register(self, set_up, case):
        url = hy.read_yaml('request', 'base_url') + case.url
        data = HandleRe.handle_para(case.data)
        res = set_up[0].send(url=url, data=data)
        try:
            assert [case.expected, case.msg] == [res.json()['code'], res.json()['msg']]
            self.obj_li.write_excel(int(case.caseId) + 1, 8, value=str(res.json()))
        except AssertionError as e:
            my_logger.error(f'用例{case.title}断言失败')
            self.obj_li.write_excel(int(case.caseId)+1,7, value='fail')
            raise e
        else:
            my_logger.info(f'用例{case.title}断言成功')
            self.obj_li.write_excel(int(case.caseId)+1,7, value='success')

