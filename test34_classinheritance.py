class Employee:
    raise_amount = 1.04     # Class variable
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)          # this calls the parent class
        # or
        # Employee.__init__(self, first, last, pay) # this is more for multiple inheritance
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, first, last, pay, employee_list=None): # this constructor has a default parameter
        super().__init__(first, last, pay)          # this calls the parent class
        # or
        # Employee.__init__(self, first, last, pay) # this is more for multiple inheritance
        if employee_list is None:
            self.employees = []
        else:
            self.employees = employee_list

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print(f'--> {emp.fullname()}')
    


dev_1 = Developer('me', 'maw', 20000, 'Python')
dev_2 = Developer('test2', 'noway', 30000, 'C/C++')

# print(help(Developer)) shows all the info about Developer class
print(dev_1.email)
print(dev_2.email)
print(dev_2.prog_lang)

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])
print(mgr_1.email)
mgr_1.print_emp()
print()
mgr_1.add_emp(dev_2)
mgr_1.print_emp()
print()
mgr_1.remove_emp(dev_1)
mgr_1.print_emp()

print(isinstance(mgr_1, Employee))
print(isinstance(mgr_1, Manager))
print(isinstance(mgr_1, Developer))

print(issubclass(Developer, Employee))
print(issubclass(Manager, Employee))
print(issubclass(Manager, Developer))
