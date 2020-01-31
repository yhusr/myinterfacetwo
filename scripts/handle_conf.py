"""
Time:2020/1/31 0031
"""
import yaml
import configparser
from scripts.handle_os import YAML_PATH, CONFIG_PATH


# 操作yaml配置文件
class HandleYaml:
    def __init__(self, filepath=None):
        if filepath:
            self.filepath = filepath
        else:
            self.filepath = YAML_PATH

    # 读取yaml中的内容
    def read_yaml(self, section_name, option_name):
        with open(self.filepath, 'r', encoding='utf8') as f:
            yaml_read = yaml.full_load(f)
        value = yaml_read[section_name][option_name]
        return value

    # 写入内容到yaml中
    def write_yaml(self, datas):
        with open(self.filepath, 'a', encoding='utf8') as f:
            yaml.dump(data=datas, stream=f, allow_unicode=True)


hy = HandleYaml()


# 操作config配置文件
class HandleConfig:
    def __init__(self, filepath=None):
        if filepath:
            self.filepath = filepath
        else:
            self.filepath = CONFIG_PATH
        self.my_config = configparser.ConfigParser()

    # 获取config文件中的内容
    def read_config(self, section_name, option_name):
        config_read = self.my_config.read(self.filepath,encoding='utf8')
        value = config_read[section_name][option_name]
        return value

    # 写入内容到config文件中
    def write_config(self, datas):
        for data in datas:
            self.my_config[data] = datas[data]
        with open(self.filepath, 'a', encoding='utf8') as f:
            f.write(datas)


hc = HandleConfig()