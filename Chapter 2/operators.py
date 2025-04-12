# Arithmetic operators
a = 7
e = 4
c = a+e
print(c)

# Assignment operators  
a = 4-2 #assign 4-2 in a
b = 6
b += 3 # increment the value of b by 3 and then assign it to b
b-= 3 # decrement the value of b by 3 and then assign it to b
b*= 3 # multiply the value of b by 3 and then assign it to b
b/= 3 # divide the value of b by 3 and then assign it to b
print(b)

# Comparison operators
d = 4
f = 5
print(d==f) # check if d is equal to f
print(d!=f) # check if d is not equal to f
print(d>f) # check if d is greater than f
print(d<f) # check if d is less than f
d = 5>3
e = 5<3
f = 5>=3
g = 5<=3
h = 5==5
i = 5!=5
j = 5 is 5
k = 5 is not 5
l = 5 in [1,2,3,4,5]
m = 5 not in [1,2,3,4,5]
print(d,e,f,g,h,i,j,k,l,m)

# Logical operators
#or operator (think if true as - here)
print("true or false", True or False) #true or false is true
print("true or true", True or True) #true or true is true
print("false or true", False or True) #false or true is true
print("false or false", False or False) #false or false is false
#and operator (think if false as - here)
print("true and false", True and False) #true and false is false
print("true and true", True and True) #true and true is true
print("false and true", False and True) #false and true is false
print("false and false", False and False) #false and false is false
# think of this as opposites
print(not(True)) #not true is false
print(not(False)) #not false is true

