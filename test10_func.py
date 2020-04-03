def say_hi():
    print("Hello World!!")

print("Me")
say_hi()
#not_Top() -- does not work. Function undefined
print("You")

def not_Top():
    print("Checking calling.")

def hello_Name(name):
    print("Hello " + name)

hello_Name("Mike")
hello_Name("Steve")

def hello_NameAge(name, age):
    print("Hello " + name + " you are " + age)

#hello_NameAge("Mike", 35) -- does not work cause passing int
hello_NameAge("Steve", "45")

def cube(num):
    return num*num*num
    # print("Hello World!!!") -- does not work. Returned back to caller.

print(cube(3))
print(cube(5))

result = cube(12)
print(result)