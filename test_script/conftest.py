'''
脚本层的公共方法
'''

import pytest

from Zonghe.caw import DataRead



from Zonghe.caw.BaseRequests import BaseRequests

# 从环境变量中读取url
@pytest.fixture(scope='session')
def url():
    return DataRead.readini('Zonghe/data_env/env.ini', 'url')


# 从环境文件中读取db
@pytest.fixture(scope='session')
def db():
    # 从ini中读取出来是字符串，将字符串转成字典，使用eval函数
    return eval(DataRead.readini('Zonghe/data_env/env.ini', 'db'))



# 创建一个BaseRequests实例
@pytest.fixture(scope='session')
def baserequests():
    return BaseRequests()
