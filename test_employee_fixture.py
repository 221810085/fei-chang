from employee import Employee
import pytest
@pytest.fixture
def employee():
    return Employee('chang','fei',8000)

def test_give_default_raise(employee):
    """能够正确测试默认涨工资吗"""
    employee.give_raise()
    assert employee.salary==13000


def test_give_custom_raise(employee):
    """测试能够识别其他涨幅的工资"""
    employee.give_raise(3000)
    assert employee.salary==11000