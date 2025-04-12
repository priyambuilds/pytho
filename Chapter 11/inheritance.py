# class Employee:
#     company = "Google"
#     def showDetails(self):
#         print(f"the name is {self.name} and the salary is {self.salary}")

# class Programmer(Employee):
#     company = "Youtube"
#     def showLanguage(self):
#         print(f"the name is {self.name} and the salary is {self.salary}")
#     def showlanguage(self):
#         print(f"the language is {self.language}")

# a = Employee()
# b = Programmer()
# print(a.company, b.company)

#this is a cumbersome way to write code, so we can use inheritance to make it more efficient.
class Employee:
     company = "Google"
     def showDetails(self):
         print(f"the name is {self.name} and the salary is {self.salary}")

class Programmer(Employee):
     company = "Youtube"
     def showLanguage(self):
         print(f"the language is {self.language}")

a = Employee()
b = Programmer()
print(a.company)
print(b.company)


