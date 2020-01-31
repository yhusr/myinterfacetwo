"""
Time:2020/1/31 0031
"""
import re
from scripts.handle_mysql import HandleMysql


class HandleRe:
    @classmethod
    def handle_para(cls,data):
        if re.search(r'{no_exist_phone}', data):
            phone = HandleMysql().no_exsit_phone_mysql()
            re_data = re.sub(r'{no_exist_phone}', phone, data)
            HandleMysql().close()
            return re_data
        return data
