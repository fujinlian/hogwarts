# 【01】jenkins api接口
# -*- coding: utf-8 -*-

import requests
import json

# url = "http://admin:9ea40687d4c443d1b38da3614e2a8967@10.12.160.21:8080/job/first_test/build"
# ret = requests.post(url)
# print(ret.text)

# 返回最新任务编号
# url = "http://admin:9ea40687d4c443d1b38da3614e2a8967@10.12.160.21:8080/job/first_test/lastBuild/buildNumber"
# ret = requests.get(url)
# print(ret.text)

# 查询任务状态
url = "http://admin:9ea40687d4c443d1b38da3614e2a8967@10.12.160.21:8080/job/first_test/6/api/json"
ret = requests.get(url)
# print(ret.text)    该方式展示格式不美观,indent是控制换行的
print(json.dumps(ret.json(), indent=2))
