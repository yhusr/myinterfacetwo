"""
Time:2020/1/31 0031
"""
from scripts.handle_mysql import HandleMysql
from scripts.handle_request import HandleRequests
from scripts.handle_conf import hy, HandleYaml
from scripts.handle_os import PHONE_PATH


class HandlePhone:

    @classmethod
    def get_phone_nums(cls, username, password='12345678', type=1):
        hm = HandleMysql()
        hr = HandleRequests()
        url = hy.read_yaml('request', 'base_url') + hy.read_yaml('request', 'register_url')
        phone = hm.no_exsit_phone_mysql()
        hr.common_heads({hy.read_yaml('request', 'request_head'): hy.read_yaml('request', 'request_value')})
        datas = {"mobile_phone": phone,
                 "pwd": password,
                 "type": type,
                 "reg_name": username}
        res = hr.send(url=url,data=datas)
        if res.json()['code'] == 0:
            phone_data = {username: datas}
            hm.close()
            hr.close()
            return phone_data

    @classmethod
    def phone_yaml(cls):
        my_yaml = HandleYaml(PHONE_PATH)
        investor_data = cls.get_phone_nums('investor')
        my_yaml.write_yaml(investor_data)
        borrower_data = cls.get_phone_nums('borrower')
        my_yaml.write_yaml(borrower_data)
        admin_data = cls.get_phone_nums('admin', type=0)
        my_yaml.write_yaml(admin_data)

if __name__ == '__main__':
    HandlePhone.phone_yaml()