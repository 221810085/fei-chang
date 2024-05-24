class Employee:
    def __init__(self,first,last,salary):
        self.first=first
        self.last=last
        self.salary=salary

    def give_raise(self,raising=5000):
        """接受默认的涨金，但是也可以接受其他的"""
        self.salary+=raising
        return self.salary

