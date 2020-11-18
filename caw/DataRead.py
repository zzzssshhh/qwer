'''
读文件的公共方法
'''
import configparser
import os

import yaml


def getProjectPath():
    '''
    获取当前工程路径
    :return:
    '''
    current_file_path = os.path.realpath(__file__)   # 当前文件路径
    # print(current_file_path)
    dir_name = os.path.dirname(current_file_path)    # 文件所在的目录
    # print(dir_name)
    dir_name = os.path.dirname(dir_name)   # 上一级目录
    # print(dir_name)
    dir_name = os.path.dirname(dir_name)   # 上一级目录
    return dir_name + "\\"


def readini(filePath,key):
    '''
    读取ini文件
    :param filePath:文件路径
    :param key: ini中的关键字
    :return: key对饮的value
    '''
    real_path = getProjectPath()+filePath
    # 调用configparser来解析配置文件
    config = configparser.ConfigParser()
    # 读文件
    config.read(real_path)
    # env表示section根据key在对应的section中取value
    value = config.get("env",key)
    return value


def readyaml(filePath):
    '''
    读取yaml文件
    :param filePath:文件路径
    :return: yaml中的文件内容
    '''
    real_path = getProjectPath() + filePath # 拼接完整路径
    with open(real_path,"r",encoding="utf-8")as f:   # 打开文件
        content = yaml.load(f,Loader=yaml.FullLoader)  #读取文件内容，放到变量content中
        print(content)
        return content




# 测试代码用完可删除
if __name__ == '__main__':
    # 预期返回D:\ApiAutoTest\
    print(getProjectPath())
    # 预期返回值http://ji001:8081/
    print(readini(r"Zonghe\data_env\env.ini","url"))
    print(readini(r"Zonghe\data_env\env.ini","db"))
    print(readyaml(r"Zonghe\data_case\rejister_fail.yaml"))