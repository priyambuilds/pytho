# object oriented programming is a programming paradigm that uses objects and classes to represent and manipulate data.
#noun - class - employee
#adjective - attributes
#verb - methods - get_salary, get_name, get_language, increment, change_language

class Employee:
    # name = "Priyam" #this is an object attribute
    language = "Python" #this is a class attribute
    salary = 100000

priyam = Employee()
priyam.name = "Priyam" #this is an instance attribute
print(priyam.language, priyam.salary, priyam.name) #output will be Python 100000 Priyam

rohan = Employee()
rohan.name = "Rohan" #this is an instance attribute
print(rohan.language, rohan.salary, rohan.name) #output will be Python 100000 Rohan

#here name is object attribute and language and salary are class attributes

#instance vs class attributes
class Employee:
    # name = "Priyam" #this is an object attribute
    language = "Python" #this is a class attribute
    salary = 100000

priyam = Employee()
priyam.language = "C++"
print(priyam.language) #output will be C++
print(Employee.language) #output will be Python
#instance attributes take precedence over class attributes during assignment or retrival.

#self parameter
class Employee:
    language = "Python" #this is a class attribute
    salary = 100000

    def get_info(self): #self is used so that we dont get an error when we call the method.
        print(f"The language is {self.language}. The salary is {self.salary}")
    @staticmethod #this is used to create a static method. it is used when we dont want to pass any parameters. in simple words, it is used when we dont want to use self.
    def greet():
        print("Hello, how are you?")

priyam = Employee()
priyam.get_info() #output will be The language is Python. The salary is 100000
priyam.greet() #output will be Hello, how are you?

