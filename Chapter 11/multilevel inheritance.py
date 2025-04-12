class employee:
     company = "Google"
     a = 1

class programmer(employee):
     b = 2

class manager(programmer):
     c = 3

o = employee()
print(o.a) #output 1, prints the attribute of the class employee
#print(o.b) #output error

o = programmer()
print(o.a, o.b) #output 1,2, prints the attribute of the class employee and programmer

o = manager()
print(o.a, o.b, o.c) #output 1,2,3, prints the attribute of the class employee, programmer and manager


