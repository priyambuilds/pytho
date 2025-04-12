class Employee:
     company = "Google"
     def showDetails(self):
         print(f"the name of the company is {self.company}")

class coder:
     language = "python"
     def showLanguage(self):
         print(f"the language is {self.language}")

class Programmer(Employee,coder):
     company = "Youtube"
     def showLanguage(self):
         print(f"the company is {self.company} and the language is {self.language}")
         
a = Employee()
b = Programmer()
b.showDetails()
b.showLanguage()

