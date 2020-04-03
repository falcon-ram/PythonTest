#reading from files
emp_file = open("employees.txt", "r") # open employees.txt file in read mode

if emp_file.readable(): # is file readable?
    print(emp_file.readline())
    print("------------")
    print(emp_file.read())

emp_file.close()

print("------------------ Next Test ------------")
emp_file = open("employees.txt", "r") # open employees.txt file in read mode

if emp_file.readable(): # is file readable?
    #print(emp_file.readlines())
    #print(emp_file.readlines()[1])
    for employee in emp_file.readlines():
        print(employee)
    
emp_file.close()