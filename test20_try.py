# Try/except
try:
    #value = 10/0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError:
    print("Devided by 0")
except ValueError as err:
    print(err)
    print("Invalid Input")
except: # catches all exceptions
    print("Error")

print("Carry on with code!!!")