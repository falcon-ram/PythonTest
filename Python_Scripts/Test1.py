def Question1():
    # Get user input for 1st point
    print ("")
    print ("1st Point")
    x1 = int(input("x: "))
    y1 = int(input("y: "))
    z1 = int(input("z: "))
    # Get user input for 2nd point
    print ("")
    print ("2nd Point")
    x2 = int(input("x: "))
    y2 = int(input("y: "))
    z2 = int(input("z: "))
    # calculate a, b, c
    a = x2 - x1
    b = y2 - y1
    c = z2 - z1
    # Now calculate points on the line
    print ("")
    print ("The 10 points are")
    for lamda in range(10):
        xnew = x1 + ((float(lamda)/10)*a)
        ynew = y1 + ((float(lamda)/10)*b)
        znew = z1 + ((float(lamda)/10)*c)
        print ("=================")
        print ("x: ")
        print (xnew)
        print ("y: ")
        print (ynew)
        print ("z: ")
        print (znew)
        print ("=================")
    print ("")

#Question1()

num1 = 12
num2 = 15
print(str(num1) + ", " + str(num2))

num3 = num1
print(str(num3))
num3 = 20
print(str(num1) + ", " + str(num3))