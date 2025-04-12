a = 10
def func():
    global a
    a = 3
    print(a) #output: 3, because the local variable a is used.

print(a) # before output: 10, because the global variable a is used.
func()
print(a) #after output: 3, because the global variable a is now changed to 3.