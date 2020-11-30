# -*- coding: utf-8 -*-

"""
1.加减乘除测试用例
2.使用数据驱动完成加减乘除测试用例生成
3.修改测试用例收集规则，执行所有以test_和check_开头测试用例
4.创建Fixture方法实现执行测试用例前打印开始计算执行测试用例后打印结束计算
5.将fixture方法存放在conftest.py 灵活设置scope级别
autouse默认false
scope:session module class function
"""

import pytest
import yaml


with open('./calc.yml') as f:
    data = yaml.safe_load(f)
    add_data = data['add']
    add_datas = add_data['add_data']
    print(f"加法的测试数据是{add_datas}")
    add_ids = add_data['add_id']
    sub_data = data['sub']
    sub_datas = sub_data['sub_data']
    print(f"减法的测试数据是{sub_datas}")
    sub_ids = sub_data['sub_id']
    mult_data = data['multi']
    mult_datas = mult_data['mult_data']
    print(f"乘法的测试数据是{mult_datas}")
    mult_ids = mult_data['mult_id']
    div_data = data['div']
    div_datas = div_data['div_data']
    print(f"除法的测试数据是{div_datas}")
    div_ids = div_data['div_id']

@pytest.fixture(params=add_datas, ids=add_ids)
def get_adddata(request):
    return request.param

#减法数据的参数化
@pytest.fixture(params=sub_datas, ids=sub_ids)
def get_subsdata(request):
    return request.param

#乘法数据的参数化
@pytest.fixture(params=mult_datas, ids=mult_ids)
def get_multdata(request):
    return request.param

#除法数据的参数化
@pytest.fixture(params=div_datas, ids=div_ids)
def get_divdata(request):
    return request.param

# fixture 是pytest的外壳函数，模拟setup teardown操作
# 执行测试用例前传入fixture方法
# yield 关键字激活fixture 的teardown方法


# 创建加减测试类，只包含加减测试方法。当前类和方法都以test开头
class Test_Calc1:

    # 测试加法的方法以test开头
    def test_add(self, get_calc, get_adddata):
       result = get_calc.add(get_adddata[0],get_adddata[1])
       if isinstance(result, float):
           result = round(result, 2)
       assert get_adddata[2] == result

    #测试减法方法以test开头
    def test_subs(self,get_calc, get_subsdata):
        result = get_calc.subs(get_subsdata[0], get_subsdata[1])
        if isinstance(result, float):
            result = round(result, 2)
        assert get_subsdata[2] == result

    # 乘法方法以check开头
    def check_mult(self,get_calc, get_multdata):
        result = get_calc.mult(get_multdata[0], get_multdata[1])
        if isinstance(result, float):
            result = round(result, 2)
        assert get_multdata[2] == result

# 创建乘除测试类包含乘除测试方法且以check开头
class Check_Calc2:

    # 测试方法以check开头
    def check_div(self, get_calc, get_divdata):
        result = get_calc.div(get_divdata[0], get_divdata[1])
        if isinstance(result, float):
            result = round(result, 2)
        assert get_divdata[2] == result