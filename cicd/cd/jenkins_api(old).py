# 【01】jenkins api接口，简单封装的操作

import configparser
import datetime
import logging
import os
import re

from jenkinsapi.jenkins import Jenkins

# 日志打印的设置，没写完。。。
logging.basicConfig(level=logging.INFO, format='[%(asctime)s] -[%(name)s]- [%(levelname)s] ')
log = logging.getLogger(__name__)


# 获取配置文件
def get_jk_config(chose):
    config = configparser.ConfigParser()
    config.read(os.path.join(os.getcwd(), 'jenkins_server.ini'))
    username = config.get(chose, 'username')
    password = config.get(chose, 'password')
    host = config.get(chose, 'host')
    port = config.get(chose, 'port')
    url = "http://" + host + ":" + port
    return url, username, password


class JenkinsDemo:

    # 计划：可以模糊匹配去查找任务进行构建
    def __init__(self, job_name, chose: 'jenkins'):
        self.job_name = job_name
        config = get_jk_config(chose)
        # config是return的？
        print(config)
        # 实例化类，以元组的方式传参
        self.jk = Jenkins(*config, useCrumb=True)

    # 获取job
    def __get__job_from_keys(self):
        choose_list = []
        print(self.jk.keys())
        # 遍历所有的job，如果job_name在所有的job里面，就加入到list（模糊匹配）
        for my_job_name in self.jk.keys():
            if self.job_name in self.job_name:
                choose_list.append(my_job_name)
        return choose_list

    # 构建一个job
    def __job_build(self, my_job_name):
        # 如果有这个job，就去定义
        if self.jk.has_job(my_job_name):
            my_job = self.jk.get_job(my_job_name)
            # 是否已经在跑？在跑的话是计划不去打印日志的
            if not my_job.is_queued_or_running():
                try:
                    last_build = my_job.get_last_buildnumber()
                except:
                    last_build = 0
                    build_num = last_build + 1
                    # 开始打包
                    try:
                        self.jk.build_job(my_job_name)
                    except Exception as e:
                        log.error(str(e))
