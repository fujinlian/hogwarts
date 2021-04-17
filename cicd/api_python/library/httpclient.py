import requests
import urllib3


class HttpClient:
    """Generic Http Client class"""

    def __init__(self, disable_ssl_verify=False, timeout=60):
        """Initialize method"""

        self.client = requests.session()
        # 请求没有https的证书的限制，做测试的时候一般是可信的网站、为了便于做自动化测试，建议去掉此校验，测试也主要是测后端研发的代码
        self.disable_ssl_verify = disable_ssl_verify
        self.timeout = timeout
        if self.disable_ssl_verify:
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    # 封装get方法，便于过程可以灵活做一些配置等
    def Get(self, url, headers=None, data=None, json=None, params=None, *args, **kwargs):
        """Http get method"""

        if headers is None:
            headers = {}

        if self.disable_ssl_verify:
            response = self.client.get(url, headers=headers, data=data, json=json, params=params
                                       , verify=False, timeout=self.timeout, *args, **kwargs)
        else:
            response = self.client.get(url, headers=headers, data=data, json=json, params=params
                                       , timeout=self.timeout, *args, **kwargs)
        response.encoding = 'utf-8'
        print(f'{response.json()}')

        return response
