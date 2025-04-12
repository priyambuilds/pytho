#Create a class “Programmer” for storing information of few programmers working at Microsoft. 
#The class should have the following attributes:
#name
#company
#salary
#language

class Programmer:
    def __init__(self, name, company, salary, language):
        self.name = name
        self.company = company
        self.salary = salary
        self.language = language

input_name = input("Enter the name of the programmer: ")
input_company = input("Enter the company of the programmer: ")
input_salary = int(input("Enter the salary of the programmer: "))
input_language = input("Enter the language of the programmer: ")

priyam = Programmer(input_name, input_company, input_salary, input_language)
print(priyam.name, priyam.company, priyam.salary, priyam.language)

#Write a class “Calculator” capable of finding square, cube and square root of a number.

class Calculator:
    def __init__(self, number):
        self.number = number

    def square(self):
        return self.number * self.number
    
    def cube(self):
        return self.number * self.number * self.number
    
    def square_root(self):
        return self.number ** 0.5   
    
input_number = int(input("Enter the number: "))

priyam = Calculator(input_number)
print(f"The square of {input_number} is {priyam.square()}")
print(f"The cube of {input_number} is {priyam.cube()}")
print(f"The square root of {input_number} is {priyam.square_root()}")

#Create a class with a class attribute a; create an object from it and set ‘a’ directly using ‘object.a = 0’. Does this change the class attribute? 

class Demo:
    a = 5

obj = Demo()
print(obj.a) #output will be 5, this is because the object attribute takes precedence over the class attribute.
obj.a = 0
print(obj.a) #output will be 0, this is because we have set the object attribute to 0.
print(Demo.a) #output will be 5, this is because the class attribute is not changed.

#Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) and get fare information of train running under Indian Railways. 
from random import randint
class Train:
    def __init__(self, train_no):
        self.train_no = train_no
        self.seats = 100
        
    def book(self, fro, to):
        print(f"Booking for {self.train_no} from {fro} to {to}")

    def get_status(self, fro, to):
        print(f"The number of seats available in {self.train_no} from {fro} to {to} is {randint(1, 100)}")

    def get_fare(self, fro, to):
        print(f"The train {self.train_no} is rinning on time from {fro} to {to} and the fare is {randint(5555, 2332)}")
        
t = Train(12345)
t.book("Delhi", "Mumbai")
t.get_status("Delhi", "Mumbai")
t.get_fare("Delhi", "Mumbai")
