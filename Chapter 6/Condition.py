#if elif else ladder

a = int(input("enter your age: "))
#multiple if statements
#if startement no one and 2
if(a%2 == 0):
    print("even")
if(a%2 != 0):
    print("odd")
#end of if statement no one and 2
# if statement no 3
if a >= 18:
    print("you are an adult")
elif a <= 0:
    print("invalid")
else:
    print("you are a minor")
#end of if statement no 3
print("end of program")




