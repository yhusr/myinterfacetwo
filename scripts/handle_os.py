"""
Time:2020/1/31 0031
"""
import os
import time

# 项目根目录
current_file = os.path.abspath(__file__)
files_path = os.path.dirname(current_file)
root_path = os.path.dirname(files_path)

# excel所在目录
data_file = os.path.join(root_path, 'data')
EXCEL_PATH = os.path.join(data_file, 'excelcases.xlsx')

# config所在目录
config_file = os.path.join(root_path, 'config')
YAML_PATH = os.path.join(config_file, 'my_yaml.yaml')
CONFIG_PATH = os.path.join(config_file, 'my_config.config')
PHONE_PATH = os.path.join(config_file, 'phone_num.yaml')

# log所在目录
strtime = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
logs_file_path = os.path.join(root_path, 'logs')
LOG_PATH = os.path.join(logs_file_path, 'log' + strtime + '.log')

# case所在目录
CASE_PATH = os.path.join(root_path, 'cases')

# report所在目录
reports_file = os.path.join(root_path, 'reports')
REPORT_PATH = os.path.join(reports_file, 'report'+strtime+'.html')
