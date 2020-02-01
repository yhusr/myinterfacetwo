"""
Time:2020/1/31 0031
"""
import re
from scripts.handle_mysql import HandleMysql
from scripts.handle_conf import HandleYaml, hy
from scripts.handle_os import PHONE_PATH


class HandleRe:
    @classmethod
    def handle_para(cls,data):
        hl = HandleYaml(PHONE_PATH)
        hm = HandleMysql()
        if re.search(r'{no_exist_phone}', data):
            phone = hm.no_exsit_phone_mysql()
            re_data = re.sub(r'{no_exist_phone}', phone, data)
            HandleMysql().close()
            return re_data
        if re.search(r'{invest_phone}', data):
            re_data = re.sub(r'{invest_phone}', hl.read_yaml('investor', 'mobile_phone'), data)
            return re_data
        if re.search(r'{user_id_re}', data):
            re_data = re.sub(r'{user_id_re}', str(hl.read_yaml('investor', 'id')), data)
            return re_data
        if re.search(r'{member_id_re}', data):
            re_data = re.sub(r'{member_id_re}', str(hl.read_yaml('borrower', 'id')), data)
            return re_data
        if re.search(r'{borrow_phone}', data):
            re_data = re.sub(r'{borrow_phone}', hl.read_yaml('borrower', 'mobile_phone'), data)
            return re_data
        if re.search(r'{no_exist_num}', data):
            re_data = re.sub(r'{no_exist_num}', str(hm.get_mysql_result(hy.read_yaml('mysql', 'id_sql'))['maxId']+1), data)
            return re_data
        if re.search(r'{admin_phone}', data):
            re_data = re.sub(r'{admin_phone}', hl.read_yaml('admin', 'mobile_phone'), data)
            return re_data
        if re.search(r'{load_id}', data):
            re_data = re.sub(r'{load_id}', str(getattr(cls, 'program_id')), data)
            return re_data
        if re.search(r'{user_id}', data):
            my_data = re.sub(r'{user_id}', str(hl.read_yaml('investor', 'id')), data)
            re_data = re.sub(r'{loan_id_re}', str(getattr(cls, 'program_id')), my_data)
            return re_data
        return data
