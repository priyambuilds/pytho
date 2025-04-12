# a = 12
# b = 45
# c = 56

# average = (a + b + c)/3
# print("The average of a, b and c is", average)

# a = 3
# b = 5
# c = 34

# average = (a + b + c)/3
# print("The average of a, b and c is", average)

#this is very repetitive. we can use functions to avoid this.
#this function can be called any no of times anywhere in the program
def avg(): #function definition
    a = 12
    b = 45
    c = 56
    average = (a + b + c)/3
    print("The average of a, b and c is", average)
avg() #function call
avg()
avg()
avg()
avg()
avg()
avg()

#function with parameters
def goodday(name,ending):
    print("Good day", name)
    print("Have a great", ending)
goodday("Harry", "evening") #output: Good day Harry have a great evening
goodday("Shubham", "morning") #output: Good day Shubham have a great morning
goodday("Rohan", "afternoon") #output: Good day Rohan have a great afternoon    


#return statement
def goodday(name,ending):
    print("Good day", name)
    print("Have a great", ending)
    return "done" #assigning a value to the function
a = goodday("Harry", "evening") #output: Good day Harry have a great evening
print(a) #output: done

#default arguments. if no argument is passed, the default value is used.
def goodday(name,ending="thank you"):
    print("Good day", name)
    print(ending)
goodday("Harry") #output: Good day Harry thank you
goodday("Harry", "thanks") #output: Good day Harry thanks

