"""
Time:2020/1/31 0031
"""
import pymysql
import random
from scripts.handle_conf import hy


class HandleMysql:
    def __init__(self):
        self.connect = pymysql.connect(host=hy.read_yaml('mysql', 'host'),
                                       user=hy.read_yaml('mysql', 'user'),
                                       password=hy.read_yaml('mysql', 'password'),
                                       port=hy.read_yaml('mysql', 'port'),
                                       charset=hy.read_yaml('mysql', 'charset'),
                                       db=hy.read_yaml('mysql', 'db'),
                                       cursorclass=pymysql.cursors.DictCursor)
        self.cursor = self.connect.cursor()

    # 自动生成随机的手机号
    @staticmethod
    def random_telephone():
        return hy.read_yaml('phone', 'pre') + ''.join(random.sample('0123456789', 8))

    # 获取从mysql获取的数据
    def get_mysql_result(self, sql, arg=None, is_more=False):
        self.cursor.execute(sql, args=arg)
        self.connect.commit()
        if is_more:
            result = self.cursor.fetchall()
        else:
            result = self.cursor.fetchone()
        return result

    # 判断随机生成的手机号是否在mysql中存在
    def if_exsit_phone(self, phone):
        result = self.get_mysql_result(sql=hy.read_yaml('phone', 'phone_sql'), arg=phone)
        if result:
            return True
        else:
            return False

    # 生成mysql中不存在的手机号
    def no_exsit_phone_mysql(self):
        while True:
            phone = self.random_telephone()
            if not self.if_exsit_phone(phone=phone):
                break
        return phone

    # 关闭mysql连接
    def close(self):
        self.cursor.close()
        self.connect.close()

if __name__ == '__main__':
    phone_sql = hy.read_yaml('phone', 'phone_sql')
    print(HandleMysql().get_mysql_result(phone_sql, '15816298405'))
