# import sqlite3
#
# conn = sqlite3.connect('test.db')


class Employee:
    pay_raise = 1.04
    def __init__(self, first, last, pay):
        print(self)

    def pay(self):
        pay = self.pay*self.pay_raise

emp_1 = Employee()

emp_1.first = 'Corey'
emp_1.last = 'Shafer'
print(emp_1)