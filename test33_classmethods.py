# Class and static methods
class Employee:
    raise_amount = 1.04     # Class variable
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        #self.pay = int(self.pay * raise_amount) # raise amount is not defined
        #self.pay = int(self.pay * Employee.raise_amount) # this works
        # or
        self.pay = int(self.pay * self.raise_amount)

    @classmethod        # this is a decorator. This decorator declares the method below as a classmethod
    def set_raise_amt(cls, amount): # cls is for the class. Just like self is for the instance
        cls.raise_amount = amount

    @classmethod        # alternate constructor using a string to construct the object
    def from_string(cls, emp_str):
        myfirst, mylast, mypay = emp_str.split('-')
        return cls(myfirst, mylast, mypay)

    @staticmethod           # this is how to declare a static method
    def is_workday(day):    # static methods do not take a class or instance
        if day.weekday() == 5 or day.weekday() == 6: # 5 = Saturday, 6 = Sunday from datetime
            return False
        return True


    


emp_1 = Employee('me', 'maw', 20000)
emp_2 = Employee('test2', 'noway', 30000)

Employee.set_raise_amt(1.05)
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

# Calling the class method using the class or the instance does the same thing
emp_1.set_raise_amt(1.06)
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

first, last, pay = emp_str_1.split('-')

new_emp_1 = Employee(first, last, pay)
print(new_emp_1.email)
print(new_emp_1.pay)

new_emp_2 = Employee.from_string(emp_str_2)
print(new_emp_2.email)
print(new_emp_2.pay)

import datetime
my_date = datetime.date(2020, 2, 20)

print(Employee.is_workday(my_date))