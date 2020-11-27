"""
1.计算器加法除法的测试用例
2.使用参数化完成测试用例的自动生成-参数化装饰函数
3.在调用测试方法之前打印开始计算；调用测试方法之后打印计算结束
注：使用等价类边界值因果图等测试用例添加断言
验证结果灵活使用setup()teardown()
round()方法四舍五入保留几位
"""
# 文件名test_开头；类名Test开头；方法名test_开头；类不能有init方法

import pytest
import yaml

from calculat_code.calculation import Caculater

with open('./calc.yml') as f:
    data = yaml.safe_load(f)
    print(data)

    add_data = data['add']
    print(add_data)
    add_datas = add_data['add_data']
    print(add_datas)
    add_ids = add_data['add_id']
    print(add_ids)

    div_data = data['div']
    div_datas = div_data['div_data']
    print(div_datas)
    div_ids = div_data['div_id']
    print(div_ids)


class TestCalclater:

    # setup方法实例化计算器
    def setup_class(self):
        print("开始计算")
        self.cal = Caculater()

    def teardown_class(self):
        print("结束计算")

    @pytest.mark.add
    @pytest.mark.parametrize('a, b, expect', add_datas, ids=add_ids)
    def test_add(self, a, b, expect):
        result = self.cal.add(a, b)
        if isinstance(result, float):
            result = round(result, 2)
        # 断言结果和预期是否一致
        assert expect == result

    @pytest.mark.div
    @pytest.mark.parametrize('a, b, expect', div_datas, ids=div_ids)
    # 测试除法的方法
    def test_div(self, a, b, expect):
        result = self.cal.div(a, b)
        if isinstance(result, float):
            result = round(result, 2)
        # 断言除法结果
        assert expect == result
