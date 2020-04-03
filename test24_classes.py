# Classes and objects
class Student:
    maleFemale = "Male"
    def __init__(self, name, major, gpa, is_on_probation): # initializes a class
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation


    def printStudentName(self):
        print(self.name)
        print(self.maleFemale)
        print(self.age) # this gives a warning here. But when the "age" member is created in
                        # test24_usingclasses.py, this function works.

    def setMaleFemale(self, male_female):
        self.maleFemale = male_female   # still need to use "self" to access the malefemale attribute
    