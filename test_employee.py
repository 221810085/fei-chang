from employee import Employee
def test_give_default_raise():
    """能够正确测试默认涨工资吗"""
    employee=Employee('chang','fei',6000)
    employee.give_raise()
    assert employee.salary==11000


def test_give_custom_raise():
    """测试能够识别其他涨幅的工资"""
    employee=Employee('chang','fei',6000)
    employee.give_raise(3000)
    assert employee.salary==9000
