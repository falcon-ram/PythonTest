# Python OOP

class Employee:
    #pass    #this allows the class to be empty
    # Test 2: With the init function
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return f'{self.first} {self.last}'

#emp_1 = Employee() #instance of a class
#emp_2 = Employee()
emp_1 = Employee('me', 'maw', 20000)
emp_2 = Employee('test2', 'noway', 30000)

print(emp_1)
print(emp_2)

# Test 2: Commenting out the manual assignments
# emp_1.first = 'Hello'
# emp_1.last= 'World'
# emp_1.email = 'memain@yahoo.com.sg'
# emp_1.pay = 50000

# emp_2.first = 'Test'
# emp_2.last= 'User'

# Test 1 commenting out these 2 lines
#emp_2.email = 'test@yahoo.com.sg' 
#emp_2.pay = 60000

# After Test 2: this line prints out the default email address
print(emp_1.email)
# After Test 1: this line causes an error cause emp_2 has no attribute called email
# so this means that the emp_2 has different attributes than emp_1
# After Test 2: this line prints out the default email address
print(emp_2.email) 

print(f'{emp_1.first} {emp_1.last}')
print(emp_1.fullname())
print(emp_2.fullname())
print()
# using the class instead of the instance to call the function
# then using the instance as a parameter to the function
# this is actually what happens in the background
print(Employee.fullname(emp_1))


