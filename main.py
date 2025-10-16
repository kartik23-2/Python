#import 
import math                     #importing math module or any other if it is in same directory
from math import sqrt           #importing only specific function from module
# import sys                                                                                        #importing sys module to get the path of python interpreter
# sys.path.append('C:\\Users\\Kartik\\AppData\\Local\\Programs\\Python\\Python310\\Lib')            #adding path of module if not in same directory

#CLASS AND OBJECTS
#----------------------------------------------

class Students():
    no_of_student = 0
    
    def __init__(self, name, student_no):
        self.name = name
        self.student_no = student_no
        self.id = name + str(student_no) + '@akgec.ac.in'
    
        Students.no_of_student += 1  #class variable to count number of students

    def mail(self):  #this is method to return the mail id same as self.id is doing above , regular methods automatically passes the instance as first argument i.e, self
        return self.id

    @classmethod  #these are alternative constructors , they take class as first argument instead of instance
    def from_str(cls, string):
        name, student_no = string.split('-')
        return cls(name, int(student_no))


print(Students.no_of_student)  

stu_1 = Students("Kartik", 2410167)
stu_2 = Students("Rahul", 2410168)

stu_str_1 = "Ankit-2410169"   #using alternative constructor
stu_3 = Students.from_str(stu_str_1)

print(Students.no_of_student)  #to check number of students after creating two objects

print(stu_1.mail())         #calling method to return mail id

print(stu_1.id)             #both are wways of getting mail id either by method or directly using self.id

print("{}{}{}".format(stu_1.name, stu_1.student_no, '@akgec.ac.in'))  #another way of printing name and roll no

print(Students.mail(stu_2))            #calling method using class name and passing object as argument

print(stu_3)
print(stu_3.mail())         #checking mail id of object created using alternative constructor

print(stu_1.__dict__) #to get all the attributes of the object




#File objects
#----------------------------------------------
f = open('test.txt', 'r')  #opening file in read mode
       #OR
  #CONTEXT MANAGER
with open('test.txt', 'r') as f:  #using context manager to open     