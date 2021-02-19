# 【07】python pytest测试实战（12.13）
import pytest
import yaml


# 读文件的方法 封装
def get_datas():
    with open("./data.yml") as f:
        datas = yaml.safe_load(f)
        print(datas)
        add_datas = datas["datas"]
        add_ids = datas["myid"]
        return [add_datas, add_ids]


def add_function(a, b):
    return a + b


# 数据驱动
@pytest.mark.parametrize("a,b,expected", get_datas()[0], ids=get_datas()[1])
def test_add(a, b, expected):
    assert add_function(a, b) == expected
