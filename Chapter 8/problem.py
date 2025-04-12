#Write a program using functions to find greatest of three numbers. 

def greatest(num1,num2,num3):
    if num1>num2 and num1>num3:
        return num1
    elif num2>num1 and num2>num3:
        return num2
    else:
        return num3
    

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

print(f"The greatest number is {greatest(num1,num2,num3)}")

#Write a recursive function to calculate the sum of first n natural numbers.
'''
sum(1) = 1
sum(2) = 1+2 = 3
sum(3) = 1+2+3 = 6
sum(n) = 1+2+3+4+.....(n-1)+n
sum(n) = sum(n-1)+n
'''
    
def sum(n):
    if n == 1: #base condition is applied so that the function doesn't call itself infinitely.
        return 1
    return sum(n-1)+n

n = int(input("Enter a number: "))
print(f"The sum of first {n} natural numbers is {sum(n)}")

'''
Write a python function to print first n lines of the following pattern: 
*** 
**               
* 
for n = 3
'''
def pattern(n):
    if n == 0:
        print("")
        return
    pattern(n-1)
    print("*"*n)

n = int(input("Enter a number: "))
pattern(n)

#Write a python function which converts inches to cms.
def inches_to_cms(inches):
    return inches*2.54

inches = int(input("Enter the length in inches: "))
print(f"The length in cms is {inches_to_cms(inches)}")

#Write a python function to remove a given word from a list and strip it at the same time. 
def remove_and_strip(string,word):
    n = []
    for item in string:
        if not item == word:
            n.append(item.strip(word))
    return n

string = ["rahul","rohan","mohan","sohan","kaku"]
print(remove_and_strip(string,"an"))

#Write a python function to print multiplication table of a given number.
def multiplication_table(n):
    for i in range(1,11):
        print(f"{n}x{i}={n*i}")

n = int(input("Enter a number: "))
multiplication_table(n)

#Write a python function to print the sum of first n natural numbers.

