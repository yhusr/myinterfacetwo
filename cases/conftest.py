"""
Time:2020/2/1 0001
"""
import pytest
from scripts.handle_request import HandleRequests
from scripts.handle_conf import hy, HandleYaml
from scripts.handle_mysql import HandleMysql
from scripts.handle_os import PHONE_PATH


@pytest.fixture(scope="class")
def set_up():
    hr = HandleRequests()
    hm = HandleMysql()
    hl = HandleYaml(PHONE_PATH)
    hr.common_heads({hy.read_yaml('request', 'request_head'): hy.read_yaml('request', 'request_value')})
    yield hr, hm, hl
    hr.close()
    hm.close()