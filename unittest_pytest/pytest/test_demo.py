# 【04】数据驱动
import pytest
import yaml


class TestDemo:

    @pytest.mark.parametrize("env", yaml.safe_load(open("./env.yaml")))
    def test_demo(self, env):
        if "test" in env:
            print("这是测试环境")
            print(env)
            print("测试环境的ip是：", env["test"])

        elif "dev" in env:
            print("这是开发环境")
            print(env)
            print("开发环境的ip是：", env["dev"])

    # 验证、查看yaml读取出来的信息
    def test_yaml(self):
        print(yaml.safe_load(open("./env.yaml")))
