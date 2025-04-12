# constructor is a special method that is used to initialize the attributes of the class.
class Employee:
    language = "Python" #this is a class attribute
    salary = 100000

    def __init__(self, name, salary, language): #dunder method which is automatically called when an object is created.
        self.name = name
        self.salary = salary
        self.language = language
        print("i am creating an object")

    def get_info(self): #self is used so that we dont get an error when we call the method.
        print(f"The language is {self.language}. The salary is {self.salary}")

priyam = Employee("Priyam", 100000, "C++")
print(priyam.name, priyam.salary, priyam.language) #output will be Priyam 100000 C++
