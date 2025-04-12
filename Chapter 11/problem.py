#Create a class (2-D vector) and use it to create another class representing a 3-D vector. 
class vector2d:
    def __init__(self, i, j):
        self.i = i
        self.j = j
    def show(self):
        print(f"{self.i}i + {self.j}j")

class vector3d(vector2d):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k
    def show(self):
        print(f"{self.i}i + {self.j}j + {self.k}k")


v2d = vector2d(1, 2)
v3d = vector3d(1, 2, 3)
v2d.show()
v3d.show()


#Create a class ‘Pets’ from a class ‘Animals’ and further create a class ‘Dog’ from ‘Pets’. Add a method ‘bark’ to class ‘Dog’.
class Animals:
    def __init__(self, name):
        self.name = name

class Pets(Animals):
    def __init__(self, name):
        super().__init__(name)

class Dog(Pets):
    def bark(self):
        print(f"{self.name} is barking")

dog = Dog("Buddy")
dog.bark()


#Create a class ‘Employee’ and add salary and increment properties to it.
#Write a method ‘salaryAfterIncrement’ method with a @property decorator with a setter which changes the value of increment based on the salary. 
class Employee:
    salary = 10000
    increment = 20
    @property
    def salaryAfterIncrement(self):
        return (self.salary + self.salary * (1 + self.increment/100))
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, new_salary):
        self.increment = ((new_salary / self.salary) - 1)*100 # new_salary / self.salary is the percentage of increment.

e = Employee()
e.salaryAfterIncrement = 12000
print(e.increment)