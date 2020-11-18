'''
登录的测试脚本（pytest)
'''
import pytest
from Zonghe.caw import DataRead
from Zonghe.baw import Member, DbOp
import requests
#读取yaml文件
@pytest.fixture(params=DataRead.readyaml("Zonghe/data_case/login_fail.yaml"))
def fail_data(request):
    return request.param

@pytest.fixture(params=DataRead.readyaml("Zonghe/data_case/login_pass.yaml"))
def pass_data(request):
    return request.param
#测试前置和后置
@pytest.fixture()
def register(pass_data, url, baserequests, db):
    # 注册
    phone = pass_data['casedata']['mobilephone']
    DbOp.deleteUser(db, phone)
    Member.register(url, baserequests, pass_data['casedata'])
    yield
    #删除注册用户
    DbOp.deleteUser(db, phone)

def test_login(register,pass_data, baserequests, url, db):
    print(f"测试数据为：{pass_data['casedata']}")
    print(f"预期结果为：{pass_data['expect']}")
    phone = pass_data['casedata']['mobilephone']
    r = Member.login(url, baserequests, pass_data['casedata'])
    assert r.json()['code'] == pass_data['expect']['code']
    assert r.json()['msg'] == pass_data['expect']['msg']

#注册失败
def test_register_fail(fail_data,url,baserequests):
    print(f"测试数据为：{fail_data['casedata']}")
    print(f"预期结果为：{fail_data['expect']}")
    r = Member.login(url, baserequests,fail_data['casedata'])
    assert r.json()['code'] == fail_data['expect']['code']
    assert r.json()['msg'] == fail_data['expect']['msg']

