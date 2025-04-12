#tuple is a collection of items that are ordered and immutable.
a = (1, 2, 3, 4, 5)
print(type(a)) #output: <class 'tuple'>
a = (1,)
print(type(a)) #output: <class 'tuple'>

a = (1,2,122,13.34,False, "rohan", "aakash")
print(a)

#tuple methods
no = a.count(122)
print(no) #output: 1

i = a.index(122)
print(i) #output: 2

#tuple unpacking
a = (1, 2, 3, 4, 5)
print(a)

#unpacking, you can assign the values to the variables in the tuple.
my_tuple = (1, 2, 3, 4, 5)
a, b, c, d, e = my_tuple
print(a, b, c, d, e) #output: 1 2 3 4 5
