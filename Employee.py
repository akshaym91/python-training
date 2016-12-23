class Employee(object):
    """docstring for Employee"""
    EMPLOYEE_COUNT = 0

    def __init__(self, salary):
        super(Employee, self).__init__()
        Employee.EMPLOYEE_COUNT += 1
        self.salary = salary

    def display_count(self):
        return Employee.EMPLOYEE_COUNT

    def get_salaray(self):
        return self.salary

e1 = Employee("4LPA")
print e1.display_count()
print e1.get_salaray()
e2 = Employee("5LPA")
print e2.display_count()
print e2.get_salaray()
e3 = Employee("6LPA")
print e3.display_count()
print e3.get_salaray()


class Number(object):
    """docstring for Number"""

    def __init__(self, start):
        super(Number, self).__init__()
        self.start = start

    def __sub__(self, other):
        return Number(self.start - other)

    def display(self):
        return self.start

X = Number(7)
Y = X - 4
print Y.display()
