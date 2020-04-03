# writing to external text file

emp_file = open("employees.txt", "r") # reading the file
print(emp_file.read())
emp_file.close()

emp_file = open("employees.txt", "a") # appending to the file
#emp_file.write("Toby - Human Resources")
emp_file.write("\nKelly - Customer Service")
emp_file.close()

emp_file = open("employees.txt", "w") # overwrite the file
#emp_file.write("Toby - Human Resources")
emp_file.write("\nKelly - Customer Service")
emp_file.close()