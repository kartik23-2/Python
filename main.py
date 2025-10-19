# #import 
# import math                     #importing math module or any other if it is in same directory
# from math import sqrt       #importing only specific function from module
# # import sys                                                                                        #importing sys module to get the path of python interpreter
# # sys.path.append('C:\\Users\\Kartik\\AppData\\Local\\Programs\\Python\\Python310\\Lib')            #adding path of module if not in same directory

# #CLASS AND OBJECTS
# #----------------------------------------------

# class Students():
#     no_of_student = 0
    
#     def __init__(self, name, student_no):
#         self.name = name
#         self.student_no = student_no
#         self.id = name + str(student_no) + '@akgec.ac.in'
    
#         Students.no_of_student += 1  #class variable to count number of students

#     def mail(self):  #this is method to return the mail id same as self.id is doing above , regular methods automatically passes the instance as first argument i.e, self
#         return self.id

#     @classmethod  #these are alternative constructors , they take class as first argument instead of instance
#     def from_str(cls, string):
#         name, student_no = string.split('-')
#         return cls(name, int(student_no))


#     @staticmethod  #static methods do not take instance or class as first argument
#     def is_adult(age):
#         return age > 18 
    
# class Monitor(Students):   #inheritance(it inherits all properties of Students class and we can overwrite them if needed)
#     def __init__(self, name, student_no):
#         super().__init__(name, student_no)  #calling parent class constructor to initialize name and student_no
#         self.student_no = 0  # This creates an INSTANCE variable with value 0






# print(Students.no_of_student)  

# stu_1 = Students("Kartik", 2410167)
# stu_2 = Students("Rahul", 2410168)

# stu_str_1 = "Ankit-2410169"   #using alternative constructor
# stu_3 = Students.from_str(stu_str_1)
# stu_4 = Monitor("Ankit", 2410169)
# print(Students.no_of_student)  #to check number of students after creating two objects

# print(stu_1.mail())         #calling method to return mail id

# print(stu_1.id)             #both are wways of getting mail id either by method or directly using self.id

# print("{}{}{}".format(stu_1.name, stu_1.student_no, '@akgec.ac.in'))  #another way of printing name and roll no

# print(Students.mail(stu_2))            #calling method using class name and passing object as argument

# print(stu_3)
# print(stu_3.mail())         #checking mail id of object created using alternative constructor

# print(stu_1.__dict__) #to get all the attributes of the object

# print(Students.is_adult(20))  #calling static method using class name
 
# print(stu_4.student_no)  #calling static method using subclass name





# #File objects
# #----------------------------------------------
# # f = open('test.txt', 'r')  #opening file in read mode
#        #OR
#   #CONTEXT MANAGER
# # with open('test.txt', 'w') as f:  #using context manager to open(it closes the file itself automatically)
# #       f.write("Hello World")         #writing to the file

# with open('test.txt', 'r') as f:  #using context manager to open(it closes the file itself automatically)
#     content = f.read()           #reading the content of file
#     print(content)               #printing the content of file

#     #readline() - reads single line from the file
#     #readlines() - reads all lines and returns list of lines
#     #write() - writes string to the file
#     #end = '' in print to avoid new line after printing

#     #various function like
#     # tell() - returns current position of file cursor
#     # seek() - changes the position of file cursor to given index
#     print(f"Length of content: {len(content)}")
#     print(f"Current cursor position: {f.tell()}")
#     f.seek(0)  #moving cursor to starting
#     print(f"Cursor position after seek(0): {f.tell()}")


#     with open('test.txt', 'r') as rf:
#         with open('copy.txt', 'w') as wf:
#             for line in rf:
#                 wf.write(line)   #copying content from one file to another  

# print(1+2)     
# print(int.__add__(1,2))  #both are same , just showing that everything is object in python including int
# print(str.__add__("1","1"))  #string concatenation using __add__ method of str class




#PROPERTY DECORATORS
#----------------------------------------------
class Students():
    no_of_student = 0
    
    def __init__(self, name, student_no):
        self.name = name
        self.student_no = student_no
        self.id = name + str(student_no) + '@akgec.ac.in'
    
        Students.no_of_student += 1  #class variable to count number of students

    @property   #decorator to make method behave like attribute
    def mail(self):  #this is method to return the mail id same as self.id is doing above , regular methods automatically passes the instance as first argument i.e, self
        return self.id
    
    @mail.setter   #setter for property decorator to set value
    def mail(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @mail.deleter   #deleter for property decorator to delete value
    def mail(self):
        self.first = None
        self.last = None
        print("Mail deleted")    


stu_1 = Students("Kartik", 2410167)
stu_1.mail = "Kartik Sharma"   #setting mail using setter
print(stu_1.first)      #accessing first name set by setter
print(stu_1.last)       #accessing last name set by setter
print(stu_1.mail)        #accessing mail as attribute without parentheses due to @property decorator 

del stu_1.mail        #deleting mail using deleter
print(stu_1.first)      #accessing first name after deleting mail


#GENERATORS
#----------------------------------------------
def square(n):
    for i in n:
        yield (i * i)
           #yield is used to create generator
numbers = square([1, 2, 3, 4, 5])
print(next(numbers))  #calling next() to get next value from generator
print(next(numbers))
#or
for num in numbers:
    print(num)


#comprehensions
#----------------------------------------------
# 

num = [1, 2, 3, 4, 5]
square_list  = []
for i in num:
    square_list.append(i * i)   #normal way of creating list
print(square_list)



# squared = [i * i for i in num]      #list comprehension
# print(squared)   
 
# s= set([1, 2, 3, 4, 5, 1, 2, 5, 6 , 25])
# print({i for i in s if i % 2 == 0})   #set comprehension to get even numbers

cities = ['New York', 'Mumbai', 'Paris']
country = ['USA', 'India', 'France']
z = zip(cities, country)   #zipping two lists   
print({city: cnty for city, cnty in z})   #dictionary comprehension