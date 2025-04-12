class employee:
    a = 1
    @classmethod #this is used to show the class attribute directly
    def show(self):
        print(f"the class attribute of a is {self.a}")
    @property #this is used to change the instance attribute
    def name(self):
        return f"{self.fname} {self.lname}"
    @name.setter
    def name(self, value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

e = employee()
e. a = 45 #this is used to change the class attribute
e.name = "John Wick" #this is used to change the instance attribute
print(e.name)
e.show()
