'''
对rquests中的get，post的方法进行一层封装
1.增加异常处理
2.增加日志打印
3，创建一个session，确保能自动管理cookie
'''
import requests


class BaseRequests:
    def __init__(self):
        # 创建一个session,赋值给属性session
        self.session = requests.session()

    def get(self,url,**kwargs):
        try:
            # 使用session的方式调用requests中的get接口
            r = self.session.get(url,**kwargs)
            print(f"发送get强求：{url}，参数：{kwargs}，成功")
            return r
        except Exception as e:
            print(f"发送get强求：{url}，参数：{kwargs}异常，异常信息为{e}")


    def post(self,url,**kwargs):
        try:
            # 使用session的方式调用requests中的get接口
            r = self.session.post(url,**kwargs)
            print(f"发送get强求：{url}，参数：{kwargs}，成功")
            return r
        except Exception as e:
            print(f"发送get强求：{url}，参数：{kwargs}异常，异常信息为{e}")


# 测试代码。用完可以删除
if __name__ == '__main__':
    r = BaseRequests().get("http://www.httpbin.org/get?wsername=root&pwd=123123")
    print(r.text)
