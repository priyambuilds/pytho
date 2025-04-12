class employee:
     def __init__(self):
          print("Employee constructor")
     a = 1

class programmer(employee):
     def __init__(self):
          print("Programmer constructor")
     b = 2

class manager(programmer):
     def __init__(self):
          super().__init__() #this is used to call the constructor of the parent class
          print("Manager constructor")
     c = 3


o = manager()
print(o.a, o.b, o.c) #output Programmer constructor Manager constructor 1 2 3



