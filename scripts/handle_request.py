"""
Time:2020/1/31 0031
"""
import requests
import json


class HandleRequests:
    def __init__(self):
        self.my_request = requests.session()

    def common_heads(self, heads):
        self.my_request.headers.update(heads)

    # 发送请求
    def send(self, url, method='post', data=None, is_json=True, **kwargs):
        if isinstance(data, str):
            try:
                data = json.loads(data)
            except Exception as e:
                data = eval(data)
                print(e)
        method = method.lower()
        if method == 'get':
            res = self.my_request.request(method=method, url=url, params=data, **kwargs)
        elif method in ('post', 'delete', 'put', 'patch'):
            """
            put:表示覆盖请求
            patch:表示局部覆盖
            1. Get是不安全的，因为在传输过程，数据被放在请求的URL中；Post的所有操作对用户来说都是不可见的。 
            2. Get传送的数据量较小，这主要是因为受URL长度限制；Post传送的数据量较大，一般被默认为不受限制。 
            3. Get限制Form表单的数据集的值必须为ASCII字符；而Post支持整个ISO10646字符集。 
            4. Get执行效率却比Post方法好。Get是form提交的默认方法。
            """
            if is_json:
                res = self.my_request.request(method=method, url=url, json=data, **kwargs)
            else:
                res = self.my_request.request(method=method, url=url, data=data, **kwargs)
        else:
            res = None
            print(f'此{method}不存在')
        return res

    # 关闭请求
    def close(self):
        self.my_request.close()


if __name__ == '__main__':
    hr = HandleRequests()
    res = hr.send(url='https://www.baidu.com/', method='get')
    print(res.content)