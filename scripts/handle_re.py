"""
Time:2020/1/31 0031
"""
import re
from scripts.handle_mysql import HandleMysql
from scripts.handle_conf import HandleYaml
from scripts.handle_os import PHONE_PATH


class HandleRe:
    @classmethod
    def handle_para(cls,data):
        hl = HandleYaml(PHONE_PATH)
        if re.search(r'{no_exist_phone}', data):
            phone = HandleMysql().no_exsit_phone_mysql()
            re_data = re.sub(r'{no_exist_phone}', phone, data)
            HandleMysql().close()
            return re_data
        if re.search(r'{invest_phone}', data):
            re_data = re.sub(r'{invest_phone}', hl.read_yaml('investor', 'mobile_phone'), data)
            return re_data
        if re.search(r'{user_id_re}', data):
            re_data = re.sub(r'{user_id_re}', str(hl.read_yaml('investor', 'id')), data)
            return re_data
        return data
