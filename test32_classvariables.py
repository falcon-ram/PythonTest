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
    
emp_1 = Employee('me', 'maw', 20000)
emp_2 = Employee('test2', 'noway', 30000)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

Employee.raise_amount = 1.05
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

#print(Employee.__dict__)

emp_1.raise_amount = 1.06
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

print()
print(Employee.num_of_emps)