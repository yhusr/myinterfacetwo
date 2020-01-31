"""
Time:2020/1/31 0031
"""
import logging
from scripts.handle_os import LOG_PATH
from scripts.handle_conf import hy


class HandleLog:
    def __init__(self, filepath=None):
        if filepath:
            self.filepath = filepath
        else:
            self.filepath = LOG_PATH

    # 获取logger对象
    def getlogger(self):
        mylogger = logging.getLogger(hy.read_yaml('log', 'logname'))
        my_format = hy.read_yaml('log', 'format')
        mylogger.setLevel(hy.read_yaml('log', 'level'))
        format_log=logging.Formatter(fmt=my_format)

        # 控制台输出
        sh = logging.StreamHandler()
        sh.setLevel(hy.read_yaml('log', 'level'))
        sh.setFormatter(format_log)
        mylogger.addHandler(sh)

        # 日志文件输出
        fh = logging.FileHandler(self.filepath, encoding='utf8')
        fh.setFormatter(my_format)
        fh.setLevel(hy.read_yaml('log', 'level'))
        mylogger.addHandler(fh)

        return mylogger


my_logger = HandleLog().getlogger()