class Employee:

    # special methods are surrounded by double '_'
    def __init__(self, first, last):
        self.first = first
        self.last = last
        #self.email = first + '.' + last + '@company.com'

    # Changing fullname function to an attribute
    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    # Creating a getter for attribute
    @property
    def email(self):
        return f'{self.first}.{self.last}@company.com'

    # Creating a setter function
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    # Creating a deleter function. This seems to work sort of like a destructor
    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None



emp_1 = Employee('John', 'Smith')

print(emp_1.first)
print(emp_1.email)
#print(emp_1.fullname())
print(emp_1.fullname)

print()
emp_1.first = 'Jim'
print(emp_1.first)
print(emp_1.email)
#print(emp_1.fullname())
print(emp_1.fullname)

emp_1.fullname = 'Nana Karthi'
print()
print(emp_1.first)
print(emp_1.email)
#print(emp_1.fullname())
print(emp_1.fullname)

del emp_1.fullname