"""
Time:2020/2/1 0001
"""
import pytest
from scripts.handle_excel import HandleExcel
from scripts.handle_conf import hy
from scripts.handle_re import HandleRe
from scripts.handle_log import my_logger


@pytest.mark.usefixtures('set_up')
class TestLogin:
    obj_li = HandleExcel('invest')
    cases = obj_li.read_excel()

    @pytest.mark.parametrize('case', cases)
    def test_register(self, set_up, case):
        url = hy.read_yaml('request', 'base_url') + case.url
        data = HandleRe.handle_para(case.data)
        res = set_up[0].send(url=url, data=data)
        if case.caseId == 2:
            invest_token = res.json()['data']['token_info']['token']
            set_up[0].common_heads({'Authorization':'Bearer ' + invest_token})
        try:
            self.obj_li.write_excel(int(case.caseId) + 1, 8, value=str(res.json()))
            assert [case.expected, case.msg] == [res.json()['code'], res.json()['msg']]
        except AssertionError as e:
            my_logger.error(f'用例{case.title}断言失败')
            self.obj_li.write_excel(int(case.caseId) + 1, 7, value='fail')
            raise e
        else:
            my_logger.info(f'用例{case.title}断言成功')
            self.obj_li.write_excel(int(case.caseId) + 1, 7, value='success')