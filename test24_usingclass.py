#using the class defined in test24_classes.py
from test24_classes import Student

student1 = Student("Jim", "Business", 3.1, False)

print(student1.name)
print(student1.gpa)

student2 = Student("Pam", "Art", 2.1, True)
print(student2.gpa)

# Added a new attribute to the student class outside of the class definition
# and the class member printStudentName managed to pick it up
# no errors
student2.age = 20 
student2.printStudentName()
student2.setMaleFemale("Female")
student2.printStudentName()

student2.maleFemale = "Male"    # this attribute is outside the __init__ function
                                # there does not seem to be any difference
student2.printStudentName()

student2.name = "Pamela"
student2.printStudentName()

print(student2.age)


