import pytest


# params 其实就是一个列表，列表里面可以存任何数据
@pytest.fixture(params=["---参数1---", "---参数2---"])
def myfixture(request):
    print("\n执行我的fixture,里面的参数是：%s\n" % request.param)
    # env = request.param #比如，可以实际用来传不同的测试环境
    # return env
    # return [env1,env2] #也可以返回列表
    # a = 1
    # return a #如果不return，那就是None
    yield request.param  # 类似return，同时下面的语句也会执行
    print("激活fixture里面的teardown操作")


@pytest.fixture()
def connectdb():  # 可以根据不同需求灵活添加
    print("执行我的fixture--connectdb")


def pytest_collection_modifyitems(session, config, items):
    print(type(items))  # items是一个列表list，每个item是一个用例
    # items.reverse()  #添加后，用例就可以倒序运行
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')
        print("item.name是%s" % item.name)
        print("tem._nodeid是%s" % item._nodeid)
        # 通过hook函数加mark标签，运行的代码里不加标签
        if "add" in item._nodeid:
            item.add_marker(pytest.mark.add)
        if "div" in item._nodeid:
            item.add_marker(pytest.mark.div)
