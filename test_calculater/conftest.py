# conftest 与运行用例在同一个package下，有一个init文件
# conftest项目下的数据共享
import pytest

from calculat_code.calculation import Calculater


# 获取计算器的实例
@pytest.fixture(scope='class')
def get_calc():
    calc = Calculater()
    print("开始计算")
    yield calc
    print("结束计算")
