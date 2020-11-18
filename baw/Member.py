'''
用户模块的接口（注册，登录，充值，用户列表，取现。。。）
'''

def register(url,baserequests,data):
    '''
    发送注册请求
    :param url: http://jy001:8081/
    :param baserequests: 是BaseRequests的一个实例
    :param data: 注册接口的参数
    :return: 响应信息
    '''
    url = url + "futureloan/mvc/api/member/register"
    r = baserequests.post(url,data=data)
    return r


def getList(url,baserequests):
    url = url+"futureloan/mvc/api/member/list"
    r = baserequests.get(url)
    return r

def login(url,baserequests,data):
    '''
    发送注册请求
    :param url: http://jy001:8081/
    :param baserequests: 是BaseRequests的一个实例
    :param data: 登录接口的参数
    :return: 响应信息
    '''
    url = url + "futureloan/mvc/api/member/login"
    r = baserequests.post(url,data=data)
    return r
# 测试代码，用完删除
# if __name__ == '__main__':
#     from Zonghe.caw.BaseRequests import BaseRequests
#
#     baserequests = BaseRequests()
#     canshu = {"mobilephone":12323123,"pwd":132}
#     r = register("http://jy001:8081/",baserequests,canshu)
#     print(r.json())