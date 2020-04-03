#special methods

class Employee:
    raise_amount = 1.04     # Class variable
    num_of_emps = 0

    # special methods are surrounded by double '_'
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

    # 'repr' is supposed to be a unique representation of an object
    # used for debugging and logging
    # the class should at least have a repr method
    # it sould return something that allows the developer to recreate the object
    def __repr__(self):
        return f"Employee('{self.first}', '{self.last}', {self.pay})"

    # 'str' supposed to be a readable representation of the object for the user
    def __str__(self):
        return f"{self.fullname()} - {self.email}"

    # define this method to do overloading of the '+' operator
    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())

emp_1 = Employee('me', 'maw', 20000)
emp_2 = Employee('test2', 'noway', 30000)

print(emp_1)
print(repr(emp_1))
print(str(emp_1))
print(emp_1.__repr__())
print(emp_1.__str__())

print(1+2)
print(int.__add__(1,2)) # this is what python is doing when you call the above 1 + 2

print(emp_1 + emp_2)

print(len(emp_1))